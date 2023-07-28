from .ffi import ffi, lib as xcb
from .types import chararr, atomNameRequestTC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ctx import Ctx
    from .window import Window

#!: a lot of this is copied and slightly edited from qtile
# http://standards.freedesktop.org/wm-spec/latest/ar01s05.html#idm139870830002400
WindowTypes = {
    "_NET_WM_WINDOW_TYPE_DESKTOP": "desktop",
    "_NET_WM_WINDOW_TYPE_DOCK": "dock",
    "_NET_WM_WINDOW_TYPE_TOOLBAR": "toolbar",
    "_NET_WM_WINDOW_TYPE_MENU": "menu",
    "_NET_WM_WINDOW_TYPE_UTILITY": "utility",
    "_NET_WM_WINDOW_TYPE_SPLASH": "splash",
    "_NET_WM_WINDOW_TYPE_DIALOG": "dialog",
    "_NET_WM_WINDOW_TYPE_DROPDOWN_MENU": "dropdown",
    "_NET_WM_WINDOW_TYPE_POPUP_MENU": "menu",
    "_NET_WM_WINDOW_TYPE_TOOLTIP": "tooltip",
    "_NET_WM_WINDOW_TYPE_NOTIFICATION": "notification",
    "_NET_WM_WINDOW_TYPE_COMBO": "combo",
    "_NET_WM_WINDOW_TYPE_DND": "dnd",
    "_NET_WM_WINDOW_TYPE_NORMAL": "normal",
}

# http://standards.freedesktop.org/wm-spec/latest/ar01s05.html#idm139870829988448
net_wm_states = (
    "_NET_WM_STATE_MODAL",
    "_NET_WM_STATE_STICKY",
    "_NET_WM_STATE_MAXIMIZED_VERT",
    "_NET_WM_STATE_MAXIMIZED_HORZ",
    "_NET_WM_STATE_SHADED",
    "_NET_WM_STATE_SKIP_TASKBAR",
    "_NET_WM_STATE_SKIP_PAGER",
    "_NET_WM_STATE_HIDDEN",
    "_NET_WM_STATE_FULLSCREEN",
    "_NET_WM_STATE_ABOVE",
    "_NET_WM_STATE_BELOW",
    "_NET_WM_STATE_DEMANDS_ATTENTION",
    "_NET_WM_STATE_FOCUSED",
)

WindowStates = {
    None: "normal",
    "_NET_WM_STATE_FULLSCREEN": "fullscreen",
    "_NET_WM_STATE_DEMANDS_ATTENTION": "urgent",
}

# Maps property names to types and formats.
PropertyMap = {
    # ewmh properties
    "_NET_DESKTOP_GEOMETRY": ("CARDINAL", 32),
    "_NET_SUPPORTED": ("ATOM", 32),
    "_NET_SUPPORTING_WM_CHECK": ("WINDOW", 32),
    "_NET_WM_NAME": ("UTF8_STRING", 8),
    "_NET_WM_PID": ("CARDINAL", 32),
    "_NET_CLIENT_LIST": ("WINDOW", 32),
    "_NET_CLIENT_LIST_STACKING": ("WINDOW", 32),
    "_NET_NUMBER_OF_DESKTOPS": ("CARDINAL", 32),
    "_NET_CURRENT_DESKTOP": ("CARDINAL", 32),
    "_NET_DESKTOP_NAMES": ("UTF8_STRING", 8),
    "_NET_DESKTOP_VIEWPORT": ("CARDINAL", 32),
    "_NET_WORKAREA": ("CARDINAL", 32),
    "_NET_ACTIVE_WINDOW": ("WINDOW", 32),
    "_NET_WM_DESKTOP": ("CARDINAL", 32),
    "_NET_WM_STRUT": ("CARDINAL", 32),
    "_NET_WM_STRUT_PARTIAL": ("CARDINAL", 32),
    "_NET_WM_WINDOW_OPACITY": ("CARDINAL", 32),
    "_NET_WM_WINDOW_TYPE": ("ATOM", 32),
    "_NET_FRAME_EXTENTS": ("CARDINAL", 32),
    # Net State
    "_NET_WM_STATE": ("ATOM", 32),
    # Xembed
    "_XEMBED_INFO": ("_XEMBED_INFO", 32),
    # ICCCM
    "WM_STATE": ("WM_STATE", 32),
}

# NOTE: copied directly from main.py

handlers = {}


def handler(name):
    def decorator(fn):
        handlers[name] = fn

    return decorator


@handler('_NET_WM_STATE')
def WmState(ctx: 'Ctx', data, window):
    act = data[0]
    p1, p2 = data[1], data[2]
    _src = data[3]
    func = [0, 0, 0][act]  # 0 - remove, 1 - add, 2 - toggle
    for part in [p1, p2]:
        if part:
            request = xcb.xcb_get_atom_name(ctx.connection, part)
            reply = xcb.xcb_get_atom_name_reply(ctx.connection, request, ffi.NULL)
            _name = xcb.xcb_get_atom_name_name(reply)
            print([_name[a] for a in range(reply.name_len)])


class AtomStore:
    def __init__(self, ctx: 'Ctx') -> None:
        self.atoms = {}
        self.ctx: 'Ctx' = ctx
        self.handlers = {}
        requests = {}

        for handler in handlers.keys():
            requests[handler] = xcb.xcb_intern_atom(
                self.ctx.connection,
                False,
                len(handler),
                chararr(handler.encode('utf-8')),
            )

        for handler, request in requests.items():
            atom = xcb.xcb_intern_atom_reply(
                self.ctx.connection, request, ffi.NULL
            ).atom
            self.atoms[handler] = atom
            self.handlers[atom] = handlers[handler]

    def set(self):
        pass

    def handle(self, ctx: 'Ctx', event: int, data, window: int):
        if window not in self.atoms:
            self.atoms[window] = {}
        self.handlers[event](ctx, data, window)

    # def add(self, name='', atom=None):
    #     assert name or atom, 'Name or atom must be set!'
    #     if name:
    #         request = xcb.xcb_intern_atom(
    #             self.ctx.connection, False, len(name), chararr(name.encode('utf-8'))
    #         )
    #         atom = xcb.xcb_intern_atom_reply(
    #             self.ctx.connection, request, ffi.NULL
    #         ).atom
    #     else:
    #         request = xcb.xcb_get_atom_name(self.ctx.connection, atom)
    #         reply = xcb.xcb_get_atom_name_reply(self.ctx.connection, request, ffi.NULL)
    #         _name = xcb.xcb_get_atom_name_name(reply)
    #         name = ''
    #         for i in range(reply.name_len):
    #             name += chr(_name[i][0])  # kinda jank hack to get value
    #     self.atoms[name] = atom
