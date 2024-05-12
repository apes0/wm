from functools import partial
import numpy as np

from ..generic import GWindow, GKey, GButton, GMod
from .. import xcb
from xcb_cffi import ffi
import trio
from .types import uintarr, maxUVal
from typing import TYPE_CHECKING, Callable, Coroutine
from ...cfg import cfg
from ..events import (
    Event,
    focusChange,
)

from logging import DEBUG
from ...debcfg import log

if TYPE_CHECKING:
    from ...ctx import Ctx
    from ..events import Event


async def runAndWait(ctx: 'Ctx', events: list['Event'], fn: Callable):
    ev = trio.Event()

    async def wait(*args):
        ev.set()

    for event in events:
        event.addListener(wait)

    fn()
    xcb.xcbFlush(ctx.connection)

    await ev.wait()

    for event in events:
        event.removeListener(wait)


class Window(GWindow):
    def __init__(self, height, width, borderWidth, _id, ctx: 'Ctx') -> None:
        self.height: int = height
        self.width: int = width
        self.borderWidth: int = borderWidth
        self.x: int = 0
        self.y: int = 0
        self.id = _id
        self.ctx: 'Ctx' = ctx
        self.parent: Window | None = None
        self.focused: bool = False
        self.mapped: bool = False
        self.destroyed: bool = False
        self.ignore = True  # set by override redirect (also we assume the worst, so we set it to true)
        self.mine: bool = False

        # events:

        self.keyPress = Event('keyPress', GKey, GMod)
        self.keyRelease = Event('keyRelease', GKey, GMod)
        self.buttonPress = Event('buttonPress', GButton, GMod)
        self.buttonRelease = Event('buttonRelease', GButton, GMod)
        self.mapRequest = Event('mapRequest')
        self.mapNotify = Event('mapNotify')
        self.unmapNotify = Event('unmapNotify')
        self.destroyNotify = Event('destroyNotify')
        self.createNotify = Event('createNotify')
        self.configureNotify = Event('configureNotify')
        self.configureRequest = Event('configureRequest')
        self.enterNotify = Event('enterNotify')
        self.leaveNotify = Event('leaveNotify')
        self.redraw = Event('redraw')  # exposure notify for x

    async def map(self):
        fn = partial(xcb.xcbMapWindow, self.ctx.connection, self.id)
        await runAndWait(self.ctx, [self.mapNotify, self.enterNotify, self.redraw], fn)

        log('windows', DEBUG, f'mapped {self}')

        self.mapped = True

    async def unmap(self):
        fn = partial(xcb.xcbUnmapWindow, self.ctx.connection, self.id)
        await runAndWait(
            self.ctx, [self.unmapNotify, self.destroyNotify, self.leaveNotify], fn
        )

        log('windows', DEBUG, f'unmapped {self}')

        self.mapped = False

    async def setFocus(self, focus: bool):
        self.focused = focus
        color: int
        # act is the function to be called *after* everything is done
        # its used so that we dont have any conflicts
        act: Coroutine | None = None

        if focus:
            color = cfg.focusedColor
            xcb.xcbSetInputFocus(
                self.ctx.connection,
                xcb.XCBInputFocusNone,  # seemingly fine?
                self.id,
                xcb.XCBCurrentTime,
            )

            if not self.ctx.focused:
                # if there is not other window that is focused, we dont have anything to do
                act = focusChange.trigger(self.ctx, None, self)
                self.ctx.focused = self

            elif self.ctx.focused.id != self.id:
                # if there is a window that is focused, unfocus it first, then focus our window
                old: GWindow = self.ctx.focused

                async def fn():
                    focusChange.block = True
                    await old.setFocus(False)
                    focusChange.block = False

                    await focusChange.trigger(self.ctx, old, self)
                    self.ctx.focused = self

                act = fn()

        else:
            color = cfg.unfocusedColor
            # if the id of the focused is our id, and only then, we need to unfocus the window,
            # otherwise, if the ids arent the same, then we are already unfocused
            if self.ctx.focused and self.ctx.focused.id == self.id:
                act = focusChange.trigger(self.ctx, self, None)
                self.ctx.focused = None
                # print(f'unfocus on {self.id} with {color}')

        # ? maybe expose this to a separate function?
        xcb.xcbChangeWindowAttributesChecked(
            self.ctx.connection, self.id, xcb.XCBCwBorderPixel, uintarr([color])
        )

        xcb.xcbFlush(self.ctx.connection)

        if act:
            await act

        log('windows', DEBUG, f'set {self}\'s focus to {focus}')

        # no waiting to do here :)

    async def configure(
        self,
        newX: int | None = None,
        newY: int | None = None,
        newWidth: int | None = None,
        newHeight: int | None = None,
        newBorderWidth: int | None = None,
#        newStackMode: int | None = None # TODO: should we have this?
    ):
        compare = {
            (newX, 'x'): xcb.XCBConfigWindowX,
            (newY, 'y'): xcb.XCBConfigWindowY,
            (newWidth, 'width'): xcb.XCBConfigWindowWidth,
            (newHeight, 'height'): xcb.XCBConfigWindowHeight,
            (newBorderWidth, 'borderWidth'): xcb.XCBConfigWindowBorderWidth,
#            (newSibling, 'sibling'): xcb.XCBConfigWindowSibling, # TODO: what and how
#            (newStackMode, 'stackMode'): xcb.XCBConfigWindowStackMode,
        }

        vals = []
        changed = 0
        new: int | None
        for (new, currentName), change in compare.items():
            if not new:  # check if it was set as an argument
                continue
            new = max(0, new)  # if its negative, it will not work with ``uint``
            current = self.__dict__[currentName]
            if new != current:
                changed |= change
                vals.append(new)
                self.__dict__[currentName] = new

        vals = uintarr(vals)

        if not changed:
            return  # ? does this break shit - limp bizkit?

        fn = partial(
            xcb.xcbConfigureWindow,
            self.ctx.connection,
            self.id,
            changed,
            vals,
        )

        fn()
        xcb.xcbFlush(self.ctx.connection)

        log('windows', DEBUG, f'configured {self} with x={newX or self.x}, y={newY or self.y}, w={newWidth or self.width}, h={newHeight or self.height}, border width={newBorderWidth or self.borderWidth}')

    #        await runAndWait(self.ctx, [self.configureNotify], fn)

    async def toTop(self):
        xcb.xcbConfigureWindow(self.ctx.connection, self.id, xcb.XCBConfigWindowStackMode, uintarr([xcb.XCBStackModeAbove]))

    async def toBottom(self):
        xcb.xcbConfigureWindow(self.ctx.connection, self.id, xcb.XCBConfigWindowStackMode, uintarr([xcb.XCBStackModeBelow]))

    async def close(self):
        fn = partial(xcb.xcbDestroyWindow, self.ctx.connection, self.id)

        await runAndWait(self.ctx, [self.destroyNotify, self.leaveNotify], fn)
        
        log('windows', DEBUG, f'closed {self}')

    async def screenshot(self, x:int=0, y:int=0, width:int|None=None, height:int|None=None) -> np.ndarray:
        width = width or self.width
        height = height or self.height
        useShm = self.ctx.gctx.avail('MIT-SHM') # type: ignore

        if useShm:
            shm = xcb.createShm(self.ctx.connection, height*width*4) # TODO: get the *actual* depth here

            resp = xcb.xcbShmGetImageReply(
                self.ctx.connection,
                xcb.xcbShmGetImageUnchecked(self.ctx.connection, self.id, x, y, width, height, maxUVal('int'), xcb.XCBImageFormatZPixmap, shm.id, 0),
                xcb.NULL
            )

            depth = resp.size//(width*height) # TODO: i know you can do this better lol

            out = ffi.buffer(shm.addr, resp.size)
        else:
            resp = xcb.xcbGetImageReply(
                self.ctx.connection,
                xcb.xcbGetImage(self.ctx.connection, xcb.XCBImageFormatZPixmap, self.id, x, y, width, height, maxUVal('int')),
                xcb.NULL
            )

            dat = xcb.xcbGetImageData(resp)

            depth: int = xcb.xcbGetImageDataLength(resp)//(width*height) # TODO: same as above here

            out = ffi.buffer(dat, width*height*depth)

        out: np.ndarray = np.frombuffer(out, np.uint8)
        if useShm:
            out = out.copy() # if this isnt here, we get a segfault loool
            # i think this happens because numpy tries to reference the, now freed, memory
            # (probably because memcpy-ing before doing anything is slower lol)
            xcb.removeShm(self.ctx.connection, shm)
        out = out.reshape((height, width, depth))
        return out


    async def kill(self):
        # the nuclear option
        # ? should we wait for something here lol?
        xcb.xcbKillClient(self.ctx.connection, self.id)
        xcb.xcbFlush(self.ctx.connection)
        
        log('windows', DEBUG, f'killed {self}')
