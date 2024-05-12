from _cffi_backend import _CDataBase
from xcb_cffi import lib, ffi
from .base import Base, parseArgs

NULL = ffi.NULL

# types

# skipping Xcbkeysymbols, because its not fully defined

# skipping ExtensionInfoT, because its not fully defined

class XcbAtomEnumT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbAtomT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbButtonIndexT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbButtonPressEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.child: int = obj.child
        self.detail: int = obj.detail
        self.event: int = obj.event
        self.eventX: int = obj.event_x
        self.eventY: int = obj.event_y
        self.pad0: int = obj.pad0
        self.responseType: int = obj.response_type
        self.root: int = obj.root
        self.rootX: int = obj.root_x
        self.rootY: int = obj.root_y
        self.sameScreen: int = obj.same_screen
        self.sequence: int = obj.sequence
        self.state: int = obj.state
        self.time: int = obj.time

class XcbButtonT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbClientMessageDataT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.data16: _CDataBase = obj.data16
        self.data32: _CDataBase = obj.data32
        self.data8: _CDataBase = obj.data8

class XcbClientMessageEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.data: _CDataBase = obj.data
        self.format: int = obj.format
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.type: int = obj.type
        self.window: int = obj.window

class XcbColormapT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbConfigWindowT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbConfigureNotifyEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.aboveSibling: int = obj.above_sibling
        self.borderWidth: int = obj.border_width
        self.event: int = obj.event
        self.height: int = obj.height
        self.overrideRedirect: int = obj.override_redirect
        self.pad0: int = obj.pad0
        self.pad1: int = obj.pad1
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.width: int = obj.width
        self.window: int = obj.window
        self.x: int = obj.x
        self.y: int = obj.y

class XcbConfigureRequestEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.borderWidth: int = obj.border_width
        self.height: int = obj.height
        self.parent: int = obj.parent
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.sibling: int = obj.sibling
        self.stackMode: int = obj.stack_mode
        self.valueMask: int = obj.value_mask
        self.width: int = obj.width
        self.window: int = obj.window
        self.x: int = obj.x
        self.y: int = obj.y

# skipping XcbConnectionT, because its not fully defined

class XcbCreateNotifyEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.borderWidth: int = obj.border_width
        self.height: int = obj.height
        self.overrideRedirect: int = obj.override_redirect
        self.pad0: int = obj.pad0
        self.pad1: int = obj.pad1
        self.parent: int = obj.parent
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.width: int = obj.width
        self.window: int = obj.window
        self.x: int = obj.x
        self.y: int = obj.y

class XcbCursorT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbCwT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbDestroyNotifyEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.event: int = obj.event
        self.pad0: int = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.window: int = obj.window

class XcbDrawableT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbEnterNotifyEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.child: int = obj.child
        self.detail: int = obj.detail
        self.event: int = obj.event
        self.eventX: int = obj.event_x
        self.eventY: int = obj.event_y
        self.mode: int = obj.mode
        self.responseType: int = obj.response_type
        self.root: int = obj.root
        self.rootX: int = obj.root_x
        self.rootY: int = obj.root_y
        self.sameScreenFocus: int = obj.same_screen_focus
        self.sequence: int = obj.sequence
        self.state: int = obj.state
        self.time: int = obj.time

# skipping XcbErrorsContextT, because its not fully defined

class XcbEventMaskT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbExposeEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.count: int = obj.count
        self.height: int = obj.height
        self.pad0: int = obj.pad0
        self.pad1: _CDataBase = obj.pad1
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.width: int = obj.width
        self.window: int = obj.window
        self.x: int = obj.x
        self.y: int = obj.y

# skipping XcbExtensionT, because its not fully defined

class XcbFocusInEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.detail: int = obj.detail
        self.event: int = obj.event
        self.mode: int = obj.mode
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbFontT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbGcT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbGcontextT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbGenericErrorT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.errorCode: int = obj.error_code
        self.fullSequence: int = obj.full_sequence
        self.majorCode: int = obj.major_code
        self.minorCode: int = obj.minor_code
        self.pad: _CDataBase = obj.pad
        self.pad0: int = obj.pad0
        self.resourceId: int = obj.resource_id
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbGenericEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.fullSequence: int = obj.full_sequence
        self.pad: _CDataBase = obj.pad
        self.pad0: int = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbGetAtomNameCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbGetAtomNameReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.length: int = obj.length
        self.nameLen: int = obj.name_len
        self.pad0: int = obj.pad0
        self.pad1: _CDataBase = obj.pad1
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbGetAtomNameRequestT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.atom: int = obj.atom
        self.length: int = obj.length
        self.majorOpcode: int = obj.major_opcode
        self.pad0: int = obj.pad0

class XcbGetGeometryCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbGetGeometryReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.borderWidth: int = obj.border_width
        self.depth: int = obj.depth
        self.height: int = obj.height
        self.length: int = obj.length
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.root: int = obj.root
        self.sequence: int = obj.sequence
        self.width: int = obj.width
        self.x: int = obj.x
        self.y: int = obj.y

class XcbGetImageCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbGetImageReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.depth: int = obj.depth
        self.length: int = obj.length
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.visual: int = obj.visual

class XcbGetKeyboardMappingCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbGetKeyboardMappingReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.keysymsPerKeycode: int = obj.keysyms_per_keycode
        self.length: int = obj.length
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbGetModifierMappingCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbGetModifierMappingReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.keycodesPerModifier: int = obj.keycodes_per_modifier
        self.length: int = obj.length
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbGetPropertyCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbGetPropertyReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.bytesAfter: int = obj.bytes_after
        self.format: int = obj.format
        self.length: int = obj.length
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.type: int = obj.type
        self.valueLen: int = obj.value_len

class XcbGetPropertyTypeT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbGetWindowAttributesCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbGetWindowAttributesReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.Class: int = obj._class
        self.allEventMasks: int = obj.all_event_masks
        self.backingPixel: int = obj.backing_pixel
        self.backingPlanes: int = obj.backing_planes
        self.backingStore: int = obj.backing_store
        self.bitGravity: int = obj.bit_gravity
        self.colormap: int = obj.colormap
        self.doNotPropagateMask: int = obj.do_not_propagate_mask
        self.length: int = obj.length
        self.mapIsInstalled: int = obj.map_is_installed
        self.mapState: int = obj.map_state
        self.overrideRedirect: int = obj.override_redirect
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.saveUnder: int = obj.save_under
        self.sequence: int = obj.sequence
        self.visual: int = obj.visual
        self.winGravity: int = obj.win_gravity
        self.yourEventMask: int = obj.your_event_mask

class XcbGxT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbImageFormatT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbImageOrderT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbImageT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.base: _CDataBase = obj.base
        self.bitOrder: int = obj.bit_order
        self.bpp: int = obj.bpp
        self.byteOrder: int = obj.byte_order
        self.data: _CDataBase = obj.data
        self.depth: int = obj.depth
        self.format: int = obj.format
        self.height: int = obj.height
        self.planeMask: int = obj.plane_mask
        self.scanlinePad: int = obj.scanline_pad
        self.size: int = obj.size
        self.stride: int = obj.stride
        self.unit: int = obj.unit
        self.width: int = obj.width

class XcbInputFocusT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbInternAtomCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbInternAtomReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.atom: int = obj.atom
        self.length: int = obj.length
        self.pad0: int = obj.pad0
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbKeyPressEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.child: int = obj.child
        self.detail: int = obj.detail
        self.event: int = obj.event
        self.eventX: int = obj.event_x
        self.eventY: int = obj.event_y
        self.pad0: int = obj.pad0
        self.responseType: int = obj.response_type
        self.root: int = obj.root
        self.rootX: int = obj.root_x
        self.rootY: int = obj.root_y
        self.sameScreen: int = obj.same_screen
        self.sequence: int = obj.sequence
        self.state: int = obj.state
        self.time: int = obj.time

# skipping XcbKeySymbolsT, because its not fully defined

class XcbKeycodeT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbKeysymT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbLineStyleT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbMapNotifyEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.event: int = obj.event
        self.overrideRedirect: int = obj.override_redirect
        self.pad0: int = obj.pad0
        self.pad1: _CDataBase = obj.pad1
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.window: int = obj.window

class XcbMapRequestEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.pad0: int = obj.pad0
        self.parent: int = obj.parent
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.window: int = obj.window

class XcbMapStateT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbModMaskT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbMotionNotifyEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.child: int = obj.child
        self.detail: int = obj.detail
        self.event: int = obj.event
        self.eventX: int = obj.event_x
        self.eventY: int = obj.event_y
        self.pad0: int = obj.pad0
        self.responseType: int = obj.response_type
        self.root: int = obj.root
        self.rootX: int = obj.root_x
        self.rootY: int = obj.root_y
        self.sameScreen: int = obj.same_screen
        self.sequence: int = obj.sequence
        self.state: int = obj.state
        self.time: int = obj.time

class XcbPixmapT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbPropModeT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbQueryExtensionCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbQueryExtensionReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.firstError: int = obj.first_error
        self.firstEvent: int = obj.first_event
        self.length: int = obj.length
        self.majorOpcode: int = obj.major_opcode
        self.pad0: int = obj.pad0
        self.present: int = obj.present
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence

class XcbQueryPointerCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbQueryPointerReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.child: int = obj.child
        self.length: int = obj.length
        self.mask: int = obj.mask
        self.pad0: _CDataBase = obj.pad0
        self.responseType: int = obj.response_type
        self.root: int = obj.root
        self.rootX: int = obj.root_x
        self.rootY: int = obj.root_y
        self.sameScreen: int = obj.same_screen
        self.sequence: int = obj.sequence
        self.winX: int = obj.win_x
        self.winY: int = obj.win_y

class XcbQueryTreeCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbQueryTreeReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.childrenLen: int = obj.children_len
        self.length: int = obj.length
        self.pad0: int = obj.pad0
        self.pad1: _CDataBase = obj.pad1
        self.parent: int = obj.parent
        self.responseType: int = obj.response_type
        self.root: int = obj.root
        self.sequence: int = obj.sequence

class XcbRandrCrtcChangeIteratorT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.data: _CDataBase = obj.data
        self.index: int = obj.index
        self.rem: int = obj.rem

# skipping XcbRandrCrtcChangeT, because its not fully defined

class XcbRandrCrtcT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbRandrGetCrtcInfoCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbRandrGetCrtcInfoReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.height: int = obj.height
        self.length: int = obj.length
        self.mode: int = obj.mode
        self.numOutputs: int = obj.num_outputs
        self.numPossibleOutputs: int = obj.num_possible_outputs
        self.responseType: int = obj.response_type
        self.rotation: int = obj.rotation
        self.rotations: int = obj.rotations
        self.sequence: int = obj.sequence
        self.status: int = obj.status
        self.timestamp: int = obj.timestamp
        self.width: int = obj.width
        self.x: int = obj.x
        self.y: int = obj.y

class XcbRandrGetScreenResourcesCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbRandrGetScreenResourcesReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.configTimestamp: int = obj.config_timestamp
        self.length: int = obj.length
        self.namesLen: int = obj.names_len
        self.numCrtcs: int = obj.num_crtcs
        self.numModes: int = obj.num_modes
        self.numOutputs: int = obj.num_outputs
        self.pad0: int = obj.pad0
        self.pad1: _CDataBase = obj.pad1
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.timestamp: int = obj.timestamp

class XcbRandrModeT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

# skipping XcbRandrNotifyDataT, because its not fully defined

# skipping XcbRandrNotifyEventT, because its not fully defined

class XcbRandrNotifyMaskT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbRandrNotifyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

# skipping XcbRandrOutputChangeT, because its not fully defined

# skipping XcbRandrOutputPropertyT, because its not fully defined

class XcbRandrOutputT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

# skipping XcbRandrProviderChangeT, because its not fully defined

# skipping XcbRandrProviderPropertyT, because its not fully defined

class XcbRandrProviderT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

# skipping XcbRandrResourceChangeT, because its not fully defined

class XcbRectangleT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.height: int = obj.height
        self.width: int = obj.width
        self.x: int = obj.x
        self.y: int = obj.y

class XcbScreenT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.allowedDepthsLen: int = obj.allowed_depths_len
        self.backingStores: int = obj.backing_stores
        self.blackPixel: int = obj.black_pixel
        self.currentInputMasks: int = obj.current_input_masks
        self.defaultColormap: int = obj.default_colormap
        self.heightInMillimeters: int = obj.height_in_millimeters
        self.heightInPixels: int = obj.height_in_pixels
        self.maxInstalledMaps: int = obj.max_installed_maps
        self.minInstalledMaps: int = obj.min_installed_maps
        self.root: int = obj.root
        self.rootDepth: int = obj.root_depth
        self.rootVisual: int = obj.root_visual
        self.saveUnders: int = obj.save_unders
        self.whitePixel: int = obj.white_pixel
        self.widthInMillimeters: int = obj.width_in_millimeters
        self.widthInPixels: int = obj.width_in_pixels

class XcbSendEventDestT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbSetupT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.bitmapFormatBitOrder: int = obj.bitmap_format_bit_order
        self.bitmapFormatScanlinePad: int = obj.bitmap_format_scanline_pad
        self.bitmapFormatScanlineUnit: int = obj.bitmap_format_scanline_unit
        self.imageByteOrder: int = obj.image_byte_order
        self.length: int = obj.length
        self.maxKeycode: int = obj.max_keycode
        self.maximumRequestLength: int = obj.maximum_request_length
        self.minKeycode: int = obj.min_keycode
        self.motionBufferSize: int = obj.motion_buffer_size
        self.pad0: int = obj.pad0
        self.pad1: _CDataBase = obj.pad1
        self.pixmapFormatsLen: int = obj.pixmap_formats_len
        self.protocolMajorVersion: int = obj.protocol_major_version
        self.protocolMinorVersion: int = obj.protocol_minor_version
        self.releaseNumber: int = obj.release_number
        self.resourceIdBase: int = obj.resource_id_base
        self.resourceIdMask: int = obj.resource_id_mask
        self.rootsLen: int = obj.roots_len
        self.status: int = obj.status
        self.vendorLen: int = obj.vendor_len

class XcbShm(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.addr: _CDataBase = obj.addr
        self.id: int = obj.id

class XcbShmGetImageCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbShmGetImageReplyT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.depth: int = obj.depth
        self.length: int = obj.length
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.size: int = obj.size
        self.visual: int = obj.visual

class XcbShmSegT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbStackModeT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbTimestampT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbUnmapNotifyEventT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.event: int = obj.event
        self.fromConfigure: int = obj.from_configure
        self.pad0: int = obj.pad0
        self.pad1: _CDataBase = obj.pad1
        self.responseType: int = obj.response_type
        self.sequence: int = obj.sequence
        self.window: int = obj.window

class XcbVisualidT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbVoidCookieT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return
        self.sequence: int = obj.sequence

class XcbWindowClassT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbWindowEnumT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

class XcbWindowT(Base):
    def __init__(self, obj):
        self.obj = obj
        if obj == ffi.NULL:
            return

# funcs and vars

XCBAtomAny: int = lib.XCB_ATOM_ANY
XCBAtomArc: int = lib.XCB_ATOM_ARC
XCBAtomAtom: int = lib.XCB_ATOM_ATOM
XCBAtomBitmap: int = lib.XCB_ATOM_BITMAP
XCBAtomCapHeight: int = lib.XCB_ATOM_CAP_HEIGHT
XCBAtomCardinal: int = lib.XCB_ATOM_CARDINAL
XCBAtomColormap: int = lib.XCB_ATOM_COLORMAP
XCBAtomCopyright: int = lib.XCB_ATOM_COPYRIGHT
XCBAtomCursor: int = lib.XCB_ATOM_CURSOR
XCBAtomCutBuffer0: int = lib.XCB_ATOM_CUT_BUFFER0
XCBAtomCutBuffer1: int = lib.XCB_ATOM_CUT_BUFFER1
XCBAtomCutBuffer2: int = lib.XCB_ATOM_CUT_BUFFER2
XCBAtomCutBuffer3: int = lib.XCB_ATOM_CUT_BUFFER3
XCBAtomCutBuffer4: int = lib.XCB_ATOM_CUT_BUFFER4
XCBAtomCutBuffer5: int = lib.XCB_ATOM_CUT_BUFFER5
XCBAtomCutBuffer6: int = lib.XCB_ATOM_CUT_BUFFER6
XCBAtomCutBuffer7: int = lib.XCB_ATOM_CUT_BUFFER7
XCBAtomDrawable: int = lib.XCB_ATOM_DRAWABLE
XCBAtomEndSpace: int = lib.XCB_ATOM_END_SPACE
XCBAtomFamilyName: int = lib.XCB_ATOM_FAMILY_NAME
XCBAtomFont: int = lib.XCB_ATOM_FONT
XCBAtomFontName: int = lib.XCB_ATOM_FONT_NAME
XCBAtomFullName: int = lib.XCB_ATOM_FULL_NAME
XCBAtomInteger: int = lib.XCB_ATOM_INTEGER
XCBAtomItalicAngle: int = lib.XCB_ATOM_ITALIC_ANGLE
XCBAtomMaxSpace: int = lib.XCB_ATOM_MAX_SPACE
XCBAtomMinSpace: int = lib.XCB_ATOM_MIN_SPACE
XCBAtomNone: int = lib.XCB_ATOM_NONE
XCBAtomNormSpace: int = lib.XCB_ATOM_NORM_SPACE
XCBAtomNotice: int = lib.XCB_ATOM_NOTICE
XCBAtomPixmap: int = lib.XCB_ATOM_PIXMAP
XCBAtomPoint: int = lib.XCB_ATOM_POINT
XCBAtomPointSize: int = lib.XCB_ATOM_POINT_SIZE
XCBAtomPrimary: int = lib.XCB_ATOM_PRIMARY
XCBAtomQuadWidth: int = lib.XCB_ATOM_QUAD_WIDTH
XCBAtomRectangle: int = lib.XCB_ATOM_RECTANGLE
XCBAtomResolution: int = lib.XCB_ATOM_RESOLUTION
XCBAtomResourceManager: int = lib.XCB_ATOM_RESOURCE_MANAGER
XCBAtomRgbBestMap: int = lib.XCB_ATOM_RGB_BEST_MAP
XCBAtomRgbBlueMap: int = lib.XCB_ATOM_RGB_BLUE_MAP
XCBAtomRgbColorMap: int = lib.XCB_ATOM_RGB_COLOR_MAP
XCBAtomRgbDefaultMap: int = lib.XCB_ATOM_RGB_DEFAULT_MAP
XCBAtomRgbGrayMap: int = lib.XCB_ATOM_RGB_GRAY_MAP
XCBAtomRgbGreenMap: int = lib.XCB_ATOM_RGB_GREEN_MAP
XCBAtomRgbRedMap: int = lib.XCB_ATOM_RGB_RED_MAP
XCBAtomSecondary: int = lib.XCB_ATOM_SECONDARY
XCBAtomStrikeoutAscent: int = lib.XCB_ATOM_STRIKEOUT_ASCENT
XCBAtomStrikeoutDescent: int = lib.XCB_ATOM_STRIKEOUT_DESCENT
XCBAtomString: int = lib.XCB_ATOM_STRING
XCBAtomSubscriptX: int = lib.XCB_ATOM_SUBSCRIPT_X
XCBAtomSubscriptY: int = lib.XCB_ATOM_SUBSCRIPT_Y
XCBAtomSuperscriptX: int = lib.XCB_ATOM_SUPERSCRIPT_X
XCBAtomSuperscriptY: int = lib.XCB_ATOM_SUPERSCRIPT_Y
XCBAtomUnderlinePosition: int = lib.XCB_ATOM_UNDERLINE_POSITION
XCBAtomUnderlineThickness: int = lib.XCB_ATOM_UNDERLINE_THICKNESS
XCBAtomVisualid: int = lib.XCB_ATOM_VISUALID
XCBAtomWeight: int = lib.XCB_ATOM_WEIGHT
XCBAtomWindow: int = lib.XCB_ATOM_WINDOW
XCBAtomWmClass: int = lib.XCB_ATOM_WM_CLASS
XCBAtomWmClientMachine: int = lib.XCB_ATOM_WM_CLIENT_MACHINE
XCBAtomWmCommand: int = lib.XCB_ATOM_WM_COMMAND
XCBAtomWmHints: int = lib.XCB_ATOM_WM_HINTS
XCBAtomWmIconName: int = lib.XCB_ATOM_WM_ICON_NAME
XCBAtomWmIconSize: int = lib.XCB_ATOM_WM_ICON_SIZE
XCBAtomWmName: int = lib.XCB_ATOM_WM_NAME
XCBAtomWmNormalHints: int = lib.XCB_ATOM_WM_NORMAL_HINTS
XCBAtomWmSizeHints: int = lib.XCB_ATOM_WM_SIZE_HINTS
XCBAtomWmTransientFor: int = lib.XCB_ATOM_WM_TRANSIENT_FOR
XCBAtomWmZoomHints: int = lib.XCB_ATOM_WM_ZOOM_HINTS
XCBAtomXHeight: int = lib.XCB_ATOM_X_HEIGHT
XCBButtonIndex1: int = lib.XCB_BUTTON_INDEX_1
XCBButtonIndex2: int = lib.XCB_BUTTON_INDEX_2
XCBButtonIndex3: int = lib.XCB_BUTTON_INDEX_3
XCBButtonIndex4: int = lib.XCB_BUTTON_INDEX_4
XCBButtonIndex5: int = lib.XCB_BUTTON_INDEX_5
XCBButtonIndexAny: int = lib.XCB_BUTTON_INDEX_ANY
XCBButtonPress: int = lib.XCB_BUTTON_PRESS
XCBButtonRelease: int = lib.XCB_BUTTON_RELEASE
XCBCirculateNotify: int = lib.XCB_CIRCULATE_NOTIFY
XCBCirculateRequest: int = lib.XCB_CIRCULATE_REQUEST
XCBClientMessage: int = lib.XCB_CLIENT_MESSAGE
XCBColormapNotify: int = lib.XCB_COLORMAP_NOTIFY
XCBConfigureNotify: int = lib.XCB_CONFIGURE_NOTIFY
XCBConfigureRequest: int = lib.XCB_CONFIGURE_REQUEST
XCBConfigWindowBorderWidth: int = lib.XCB_CONFIG_WINDOW_BORDER_WIDTH
XCBConfigWindowHeight: int = lib.XCB_CONFIG_WINDOW_HEIGHT
XCBConfigWindowSibling: int = lib.XCB_CONFIG_WINDOW_SIBLING
XCBConfigWindowStackMode: int = lib.XCB_CONFIG_WINDOW_STACK_MODE
XCBConfigWindowWidth: int = lib.XCB_CONFIG_WINDOW_WIDTH
XCBConfigWindowX: int = lib.XCB_CONFIG_WINDOW_X
XCBConfigWindowY: int = lib.XCB_CONFIG_WINDOW_Y
XCBCopyFromParent: int = lib.XCB_COPY_FROM_PARENT
XCBCreateNotify: int = lib.XCB_CREATE_NOTIFY
XCBCurrentTime: int = lib.XCB_CURRENT_TIME
XCBCwBackingPixel: int = lib.XCB_CW_BACKING_PIXEL
XCBCwBackingPlanes: int = lib.XCB_CW_BACKING_PLANES
XCBCwBackingStore: int = lib.XCB_CW_BACKING_STORE
XCBCwBackPixel: int = lib.XCB_CW_BACK_PIXEL
XCBCwBackPixmap: int = lib.XCB_CW_BACK_PIXMAP
XCBCwBitGravity: int = lib.XCB_CW_BIT_GRAVITY
XCBCwBorderPixel: int = lib.XCB_CW_BORDER_PIXEL
XCBCwBorderPixmap: int = lib.XCB_CW_BORDER_PIXMAP
XCBCwColormap: int = lib.XCB_CW_COLORMAP
XCBCwCursor: int = lib.XCB_CW_CURSOR
XCBCwDontPropagate: int = lib.XCB_CW_DONT_PROPAGATE
XCBCwEventMask: int = lib.XCB_CW_EVENT_MASK
XCBCwOverrideRedirect: int = lib.XCB_CW_OVERRIDE_REDIRECT
XCBCwSaveUnder: int = lib.XCB_CW_SAVE_UNDER
XCBCwWinGravity: int = lib.XCB_CW_WIN_GRAVITY
XCBDestroyNotify: int = lib.XCB_DESTROY_NOTIFY
XCBEnterNotify: int = lib.XCB_ENTER_NOTIFY
XCBEventMaskButton1Motion: int = lib.XCB_EVENT_MASK_BUTTON_1_MOTION
XCBEventMaskButton2Motion: int = lib.XCB_EVENT_MASK_BUTTON_2_MOTION
XCBEventMaskButton3Motion: int = lib.XCB_EVENT_MASK_BUTTON_3_MOTION
XCBEventMaskButton4Motion: int = lib.XCB_EVENT_MASK_BUTTON_4_MOTION
XCBEventMaskButton5Motion: int = lib.XCB_EVENT_MASK_BUTTON_5_MOTION
XCBEventMaskButtonMotion: int = lib.XCB_EVENT_MASK_BUTTON_MOTION
XCBEventMaskButtonPress: int = lib.XCB_EVENT_MASK_BUTTON_PRESS
XCBEventMaskButtonRelease: int = lib.XCB_EVENT_MASK_BUTTON_RELEASE
XCBEventMaskColorMapChange: int = lib.XCB_EVENT_MASK_COLOR_MAP_CHANGE
XCBEventMaskEnterWindow: int = lib.XCB_EVENT_MASK_ENTER_WINDOW
XCBEventMaskExposure: int = lib.XCB_EVENT_MASK_EXPOSURE
XCBEventMaskFocusChange: int = lib.XCB_EVENT_MASK_FOCUS_CHANGE
XCBEventMaskKeymapState: int = lib.XCB_EVENT_MASK_KEYMAP_STATE
XCBEventMaskKeyPress: int = lib.XCB_EVENT_MASK_KEY_PRESS
XCBEventMaskKeyRelease: int = lib.XCB_EVENT_MASK_KEY_RELEASE
XCBEventMaskLeaveWindow: int = lib.XCB_EVENT_MASK_LEAVE_WINDOW
XCBEventMaskNoEvent: int = lib.XCB_EVENT_MASK_NO_EVENT
XCBEventMaskOwnerGrabButton: int = lib.XCB_EVENT_MASK_OWNER_GRAB_BUTTON
XCBEventMaskPointerMotion: int = lib.XCB_EVENT_MASK_POINTER_MOTION
XCBEventMaskPointerMotionHint: int = lib.XCB_EVENT_MASK_POINTER_MOTION_HINT
XCBEventMaskPropertyChange: int = lib.XCB_EVENT_MASK_PROPERTY_CHANGE
XCBEventMaskResizeRedirect: int = lib.XCB_EVENT_MASK_RESIZE_REDIRECT
XCBEventMaskStructureNotify: int = lib.XCB_EVENT_MASK_STRUCTURE_NOTIFY
XCBEventMaskSubstructureNotify: int = lib.XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY
XCBEventMaskSubstructureRedirect: int = lib.XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT
XCBEventMaskVisibilityChange: int = lib.XCB_EVENT_MASK_VISIBILITY_CHANGE
XCBExpose: int = lib.XCB_EXPOSE
XCBFocusIn: int = lib.XCB_FOCUS_IN
XCBFocusOut: int = lib.XCB_FOCUS_OUT
XCBGcArcMode: int = lib.XCB_GC_ARC_MODE
XCBGcBackground: int = lib.XCB_GC_BACKGROUND
XCBGcCapStyle: int = lib.XCB_GC_CAP_STYLE
XCBGcClipMask: int = lib.XCB_GC_CLIP_MASK
XCBGcClipOriginX: int = lib.XCB_GC_CLIP_ORIGIN_X
XCBGcClipOriginY: int = lib.XCB_GC_CLIP_ORIGIN_Y
XCBGcDashList: int = lib.XCB_GC_DASH_LIST
XCBGcDashOffset: int = lib.XCB_GC_DASH_OFFSET
XCBGcFillRule: int = lib.XCB_GC_FILL_RULE
XCBGcFillStyle: int = lib.XCB_GC_FILL_STYLE
XCBGcFont: int = lib.XCB_GC_FONT
XCBGcForeground: int = lib.XCB_GC_FOREGROUND
XCBGcFunction: int = lib.XCB_GC_FUNCTION
XCBGcGraphicsExposures: int = lib.XCB_GC_GRAPHICS_EXPOSURES
XCBGcJoinStyle: int = lib.XCB_GC_JOIN_STYLE
XCBGcLineStyle: int = lib.XCB_GC_LINE_STYLE
XCBGcLineWidth: int = lib.XCB_GC_LINE_WIDTH
XCBGcPlaneMask: int = lib.XCB_GC_PLANE_MASK
XCBGcStipple: int = lib.XCB_GC_STIPPLE
XCBGcSubwindowMode: int = lib.XCB_GC_SUBWINDOW_MODE
XCBGcTile: int = lib.XCB_GC_TILE
XCBGcTileStippleOriginX: int = lib.XCB_GC_TILE_STIPPLE_ORIGIN_X
XCBGcTileStippleOriginY: int = lib.XCB_GC_TILE_STIPPLE_ORIGIN_Y
XCBGetPropertyTypeAny: int = lib.XCB_GET_PROPERTY_TYPE_ANY
XCBGeGeneric: int = lib.XCB_GE_GENERIC
XCBGrabAny: int = lib.XCB_GRAB_ANY
XCBGrabModeAsync: int = lib.XCB_GRAB_MODE_ASYNC
XCBGraphicsExposure: int = lib.XCB_GRAPHICS_EXPOSURE
XCBGravityNotify: int = lib.XCB_GRAVITY_NOTIFY
XCBGxAnd: int = lib.XCB_GX_AND
XCBGxAndInverted: int = lib.XCB_GX_AND_INVERTED
XCBGxAndReverse: int = lib.XCB_GX_AND_REVERSE
XCBGxClear: int = lib.XCB_GX_CLEAR
XCBGxCopy: int = lib.XCB_GX_COPY
XCBGxCopyInverted: int = lib.XCB_GX_COPY_INVERTED
XCBGxEquiv: int = lib.XCB_GX_EQUIV
XCBGxInvert: int = lib.XCB_GX_INVERT
XCBGxNand: int = lib.XCB_GX_NAND
XCBGxNoop: int = lib.XCB_GX_NOOP
XCBGxNor: int = lib.XCB_GX_NOR
XCBGxOr: int = lib.XCB_GX_OR
XCBGxOrInverted: int = lib.XCB_GX_OR_INVERTED
XCBGxOrReverse: int = lib.XCB_GX_OR_REVERSE
XCBGxSet: int = lib.XCB_GX_SET
XCBGxXor: int = lib.XCB_GX_XOR
XCBImageFormatXyBitmap: int = lib.XCB_IMAGE_FORMAT_XY_BITMAP
XCBImageFormatXyPixmap: int = lib.XCB_IMAGE_FORMAT_XY_PIXMAP
XCBImageFormatZPixmap: int = lib.XCB_IMAGE_FORMAT_Z_PIXMAP
XCBImageOrderLsbFirst: int = lib.XCB_IMAGE_ORDER_LSB_FIRST
XCBImageOrderMsbFirst: int = lib.XCB_IMAGE_ORDER_MSB_FIRST
XCBInputFocusFollowKeyboard: int = lib.XCB_INPUT_FOCUS_FOLLOW_KEYBOARD
XCBInputFocusNone: int = lib.XCB_INPUT_FOCUS_NONE
XCBInputFocusParent: int = lib.XCB_INPUT_FOCUS_PARENT
XCBInputFocusPointerRoot: int = lib.XCB_INPUT_FOCUS_POINTER_ROOT
XCBKeymapNotify: int = lib.XCB_KEYMAP_NOTIFY
XCBKeyPress: int = lib.XCB_KEY_PRESS
XCBKeyRelease: int = lib.XCB_KEY_RELEASE
XCBLeaveNotify: int = lib.XCB_LEAVE_NOTIFY
XCBLineStyleDoubleDash: int = lib.XCB_LINE_STYLE_DOUBLE_DASH
XCBLineStyleOnOffDash: int = lib.XCB_LINE_STYLE_ON_OFF_DASH
XCBLineStyleSolid: int = lib.XCB_LINE_STYLE_SOLID
XCBMappingNotify: int = lib.XCB_MAPPING_NOTIFY
XCBMapNotify: int = lib.XCB_MAP_NOTIFY
XCBMapRequest: int = lib.XCB_MAP_REQUEST
XCBMapStateUnmapped: int = lib.XCB_MAP_STATE_UNMAPPED
XCBMapStateUnviewable: int = lib.XCB_MAP_STATE_UNVIEWABLE
XCBMapStateViewable: int = lib.XCB_MAP_STATE_VIEWABLE
XCBModMask1: int = lib.XCB_MOD_MASK_1
XCBModMask2: int = lib.XCB_MOD_MASK_2
XCBModMask3: int = lib.XCB_MOD_MASK_3
XCBModMask4: int = lib.XCB_MOD_MASK_4
XCBModMask5: int = lib.XCB_MOD_MASK_5
XCBModMaskAny: int = lib.XCB_MOD_MASK_ANY
XCBModMaskControl: int = lib.XCB_MOD_MASK_CONTROL
XCBModMaskLock: int = lib.XCB_MOD_MASK_LOCK
XCBModMaskShift: int = lib.XCB_MOD_MASK_SHIFT
XCBMotionNotify: int = lib.XCB_MOTION_NOTIFY
XCBNone: int = lib.XCB_NONE
XCBNoExposure: int = lib.XCB_NO_EXPOSURE
XCBPropertyNotify: int = lib.XCB_PROPERTY_NOTIFY
XCBPropModeAppend: int = lib.XCB_PROP_MODE_APPEND
XCBPropModePrepend: int = lib.XCB_PROP_MODE_PREPEND
XCBPropModeReplace: int = lib.XCB_PROP_MODE_REPLACE
XCBRandrNotify: int = lib.XCB_RANDR_NOTIFY
XCBRandrNotifyCrtcChange: int = lib.XCB_RANDR_NOTIFY_CRTC_CHANGE
XCBRandrNotifyMaskCrtcChange: int = lib.XCB_RANDR_NOTIFY_MASK_CRTC_CHANGE
XCBRandrNotifyMaskOutputChange: int = lib.XCB_RANDR_NOTIFY_MASK_OUTPUT_CHANGE
XCBRandrNotifyMaskOutputProperty: int = lib.XCB_RANDR_NOTIFY_MASK_OUTPUT_PROPERTY
XCBRandrNotifyMaskProviderChange: int = lib.XCB_RANDR_NOTIFY_MASK_PROVIDER_CHANGE
XCBRandrNotifyMaskProviderProperty: int = lib.XCB_RANDR_NOTIFY_MASK_PROVIDER_PROPERTY
XCBRandrNotifyMaskResourceChange: int = lib.XCB_RANDR_NOTIFY_MASK_RESOURCE_CHANGE
XCBRandrNotifyMaskScreenChange: int = lib.XCB_RANDR_NOTIFY_MASK_SCREEN_CHANGE
XCBRandrNotifyOutputChange: int = lib.XCB_RANDR_NOTIFY_OUTPUT_CHANGE
XCBRandrNotifyOutputProperty: int = lib.XCB_RANDR_NOTIFY_OUTPUT_PROPERTY
XCBRandrNotifyProviderChange: int = lib.XCB_RANDR_NOTIFY_PROVIDER_CHANGE
XCBRandrNotifyProviderProperty: int = lib.XCB_RANDR_NOTIFY_PROVIDER_PROPERTY
XCBRandrNotifyResourceChange: int = lib.XCB_RANDR_NOTIFY_RESOURCE_CHANGE
XCBReparentNotify: int = lib.XCB_REPARENT_NOTIFY
XCBResizeRequest: int = lib.XCB_RESIZE_REQUEST
XCBSelectionClear: int = lib.XCB_SELECTION_CLEAR
XCBSelectionNotify: int = lib.XCB_SELECTION_NOTIFY
XCBSelectionRequest: int = lib.XCB_SELECTION_REQUEST
XCBSendEventDestItemFocus: int = lib.XCB_SEND_EVENT_DEST_ITEM_FOCUS
XCBSendEventDestPointerWindow: int = lib.XCB_SEND_EVENT_DEST_POINTER_WINDOW
XCBStackModeAbove: int = lib.XCB_STACK_MODE_ABOVE
XCBStackModeBelow: int = lib.XCB_STACK_MODE_BELOW
XCBStackModeBottomIf: int = lib.XCB_STACK_MODE_BOTTOM_IF
XCBStackModeOpposite: int = lib.XCB_STACK_MODE_OPPOSITE
XCBStackModeTopIf: int = lib.XCB_STACK_MODE_TOP_IF
XCBUnmapNotify: int = lib.XCB_UNMAP_NOTIFY
XCBVisibilityNotify: int = lib.XCB_VISIBILITY_NOTIFY
XCBWindowClassCopyFromParent: int = lib.XCB_WINDOW_CLASS_COPY_FROM_PARENT
XCBWindowClassInputOnly: int = lib.XCB_WINDOW_CLASS_INPUT_ONLY
XCBWindowClassInputOutput: int = lib.XCB_WINDOW_CLASS_INPUT_OUTPUT
XCBWindowNone: int = lib.XCB_WINDOW_NONE
createShm = lambda *a: XcbShm(lib.create_shm(*parseArgs(a)))
removeShm = lambda *a: (lib.remove_shm(*parseArgs(a)))
xcbAuxGetScreen = lambda *a: XcbScreenT(lib.xcb_aux_get_screen(*parseArgs(a)))
xcbChangeProperty = lambda *a: XcbVoidCookieT(lib.xcb_change_property(*parseArgs(a)))
xcbChangeWindowAttributesChecked = lambda *a: XcbVoidCookieT(lib.xcb_change_window_attributes_checked(*parseArgs(a)))
xcbCloseFont = lambda *a: XcbVoidCookieT(lib.xcb_close_font(*parseArgs(a)))
xcbConfigureWindow = lambda *a: XcbVoidCookieT(lib.xcb_configure_window(*parseArgs(a)))
xcbConnect = lambda *a: (lib.xcb_connect(*parseArgs(a)))
xcbConnectionHasError = lambda *a: (lib.xcb_connection_has_error(*parseArgs(a)))
xcbCopyArea = lambda *a: XcbVoidCookieT(lib.xcb_copy_area(*parseArgs(a)))
xcbCreateGc = lambda *a: XcbVoidCookieT(lib.xcb_create_gc(*parseArgs(a)))
xcbCreateGlyphCursor = lambda *a: XcbVoidCookieT(lib.xcb_create_glyph_cursor(*parseArgs(a)))
xcbCreatePixmap = lambda *a: XcbVoidCookieT(lib.xcb_create_pixmap(*parseArgs(a)))
xcbCreateWindow = lambda *a: XcbVoidCookieT(lib.xcb_create_window(*parseArgs(a)))
xcbDeleteProperty = lambda *a: XcbVoidCookieT(lib.xcb_delete_property(*parseArgs(a)))
xcbDestroyWindow = lambda *a: XcbVoidCookieT(lib.xcb_destroy_window(*parseArgs(a)))
xcbDisconnect = lambda *a: (lib.xcb_disconnect(*parseArgs(a)))
xcbErrorsContextFree = lambda *a: (lib.xcb_errors_context_free(*parseArgs(a)))
xcbErrorsContextNew = lambda *a: (lib.xcb_errors_context_new(*parseArgs(a)))
xcbErrorsGetNameForError = lambda *a: (lib.xcb_errors_get_name_for_error(*parseArgs(a)))
xcbErrorsGetNameForMajorCode = lambda *a: (lib.xcb_errors_get_name_for_major_code(*parseArgs(a)))
xcbErrorsGetNameForMinorCode = lambda *a: (lib.xcb_errors_get_name_for_minor_code(*parseArgs(a)))
xcbFlush = lambda *a: (lib.xcb_flush(*parseArgs(a)))
xcbFreeCursor = lambda *a: XcbVoidCookieT(lib.xcb_free_cursor(*parseArgs(a)))
xcbFreePixmap = lambda *a: XcbVoidCookieT(lib.xcb_free_pixmap(*parseArgs(a)))
xcbGenerateId = lambda *a: (lib.xcb_generate_id(*parseArgs(a)))
xcbGetAtomName = lambda *a: XcbGetAtomNameCookieT(lib.xcb_get_atom_name(*parseArgs(a)))
xcbGetAtomNameName = lambda *a: (lib.xcb_get_atom_name_name(*parseArgs(a)))
xcbGetAtomNameReply = lambda *a: XcbGetAtomNameReplyT(lib.xcb_get_atom_name_reply(*parseArgs(a)))
xcbGetExtensionData = lambda *a: (lib.xcb_get_extension_data(*parseArgs(a)))
xcbGetFileDescriptor = lambda *a: (lib.xcb_get_file_descriptor(*parseArgs(a)))
xcbGetGeometry = lambda *a: XcbGetGeometryCookieT(lib.xcb_get_geometry(*parseArgs(a)))
xcbGetGeometryReply = lambda *a: XcbGetGeometryReplyT(lib.xcb_get_geometry_reply(*parseArgs(a)))
xcbGetImage = lambda *a: XcbGetImageCookieT(lib.xcb_get_image(*parseArgs(a)))
xcbGetImageData = lambda *a: (lib.xcb_get_image_data(*parseArgs(a)))
xcbGetImageDataLength = lambda *a: (lib.xcb_get_image_data_length(*parseArgs(a)))
xcbGetImageReply = lambda *a: XcbGetImageReplyT(lib.xcb_get_image_reply(*parseArgs(a)))
xcbGetKeyboardMapping = lambda *a: XcbGetKeyboardMappingCookieT(lib.xcb_get_keyboard_mapping(*parseArgs(a)))
xcbGetKeyboardMappingReply = lambda *a: XcbGetKeyboardMappingReplyT(lib.xcb_get_keyboard_mapping_reply(*parseArgs(a)))
xcbGetMaximumRequestLength = lambda *a: (lib.xcb_get_maximum_request_length(*parseArgs(a)))
xcbGetModifierMappingKeycodes = lambda *a: XcbKeycodeT(lib.xcb_get_modifier_mapping_keycodes(*parseArgs(a)))
xcbGetModifierMappingReply = lambda *a: XcbGetModifierMappingReplyT(lib.xcb_get_modifier_mapping_reply(*parseArgs(a)))
xcbGetModifierMappingUnchecked = lambda *a: XcbGetModifierMappingCookieT(lib.xcb_get_modifier_mapping_unchecked(*parseArgs(a)))
xcbGetProperty = lambda *a: XcbGetPropertyCookieT(lib.xcb_get_property(*parseArgs(a)))
xcbGetPropertyReply = lambda *a: XcbGetPropertyReplyT(lib.xcb_get_property_reply(*parseArgs(a)))
xcbGetPropertyValue = lambda *a: (lib.xcb_get_property_value(*parseArgs(a)))
xcbGetSetup = lambda *a: (lib.xcb_get_setup(*parseArgs(a)))
xcbGetWindowAttributes = lambda *a: XcbGetWindowAttributesCookieT(lib.xcb_get_window_attributes(*parseArgs(a)))
xcbGetWindowAttributesReply = lambda *a: XcbGetWindowAttributesReplyT(lib.xcb_get_window_attributes_reply(*parseArgs(a)))
xcbGrabButton = lambda *a: XcbVoidCookieT(lib.xcb_grab_button(*parseArgs(a)))
xcbGrabKey = lambda *a: XcbVoidCookieT(lib.xcb_grab_key(*parseArgs(a)))
xcbImageCreateNative = lambda *a: XcbImageT(lib.xcb_image_create_native(*parseArgs(a)))
xcbImageDestroy = lambda *a: (lib.xcb_image_destroy(*parseArgs(a)))
xcbImagePut = lambda *a: XcbVoidCookieT(lib.xcb_image_put(*parseArgs(a)))
xcbImageText8 = lambda *a: XcbVoidCookieT(lib.xcb_image_text_8(*parseArgs(a)))
xcbInternAtom = lambda *a: XcbInternAtomCookieT(lib.xcb_intern_atom(*parseArgs(a)))
xcbInternAtomReply = lambda *a: XcbInternAtomReplyT(lib.xcb_intern_atom_reply(*parseArgs(a)))
xcbKeySymbolsAlloc = lambda *a: (lib.xcb_key_symbols_alloc(*parseArgs(a)))
xcbKeySymbolsFree = lambda *a: (lib.xcb_key_symbols_free(*parseArgs(a)))
xcbKeySymbolsGetKeycode = lambda *a: XcbKeycodeT(lib.xcb_key_symbols_get_keycode(*parseArgs(a)))
xcbKillClient = lambda *a: XcbVoidCookieT(lib.xcb_kill_client(*parseArgs(a)))
xcbMapWindow = lambda *a: XcbVoidCookieT(lib.xcb_map_window(*parseArgs(a)))
xcbOpenFont = lambda *a: XcbVoidCookieT(lib.xcb_open_font(*parseArgs(a)))
xcbPollForEvent = lambda *a: XcbGenericEventT(lib.xcb_poll_for_event(*parseArgs(a)))
xcbPolyFillRectangle = lambda *a: XcbVoidCookieT(lib.xcb_poly_fill_rectangle(*parseArgs(a)))
xcbQueryExtensionReply = lambda *a: XcbQueryExtensionReplyT(lib.xcb_query_extension_reply(*parseArgs(a)))
xcbQueryExtensionUnchecked = lambda *a: XcbQueryExtensionCookieT(lib.xcb_query_extension_unchecked(*parseArgs(a)))
xcbQueryPointer = lambda *a: XcbQueryPointerCookieT(lib.xcb_query_pointer(*parseArgs(a)))
xcbQueryPointerReply = lambda *a: XcbQueryPointerReplyT(lib.xcb_query_pointer_reply(*parseArgs(a)))
xcbQueryTree = lambda *a: XcbQueryTreeCookieT(lib.xcb_query_tree(*parseArgs(a)))
xcbQueryTreeChildren = lambda *a: XcbWindowT(lib.xcb_query_tree_children(*parseArgs(a)))
xcbQueryTreeReply = lambda *a: XcbQueryTreeReplyT(lib.xcb_query_tree_reply(*parseArgs(a)))
xcbRandrGetCrtcInfo = lambda *a: XcbRandrGetCrtcInfoCookieT(lib.xcb_randr_get_crtc_info(*parseArgs(a)))
xcbRandrGetCrtcInfoReply = lambda *a: XcbRandrGetCrtcInfoReplyT(lib.xcb_randr_get_crtc_info_reply(*parseArgs(a)))
xcbRandrGetScreenResources = lambda *a: XcbRandrGetScreenResourcesCookieT(lib.xcb_randr_get_screen_resources(*parseArgs(a)))
xcbRandrGetScreenResourcesCrtcs = lambda *a: XcbRandrCrtcT(lib.xcb_randr_get_screen_resources_crtcs(*parseArgs(a)))
xcbRandrGetScreenResourcesCrtcsLength = lambda *a: (lib.xcb_randr_get_screen_resources_crtcs_length(*parseArgs(a)))
xcbRandrGetScreenResourcesReply = lambda *a: XcbRandrGetScreenResourcesReplyT(lib.xcb_randr_get_screen_resources_reply(*parseArgs(a)))
xcbRandrSelectInput = lambda *a: XcbVoidCookieT(lib.xcb_randr_select_input(*parseArgs(a)))
xcbSendEvent = lambda *a: XcbVoidCookieT(lib.xcb_send_event(*parseArgs(a)))
xcbSetInputFocus = lambda *a: XcbVoidCookieT(lib.xcb_set_input_focus(*parseArgs(a)))
xcbShmCreatePixmap = lambda *a: XcbVoidCookieT(lib.xcb_shm_create_pixmap(*parseArgs(a)))
xcbShmGetImageReply = lambda *a: XcbShmGetImageReplyT(lib.xcb_shm_get_image_reply(*parseArgs(a)))
xcbShmGetImageUnchecked = lambda *a: XcbShmGetImageCookieT(lib.xcb_shm_get_image_unchecked(*parseArgs(a)))
xcbShmPutImage = lambda *a: XcbVoidCookieT(lib.xcb_shm_put_image(*parseArgs(a)))
xcbTestFakeInput = lambda *a: XcbVoidCookieT(lib.xcb_test_fake_input(*parseArgs(a)))
xcbUngrabButton = lambda *a: XcbVoidCookieT(lib.xcb_ungrab_button(*parseArgs(a)))
xcbUngrabKey = lambda *a: XcbVoidCookieT(lib.xcb_ungrab_key(*parseArgs(a)))
xcbUnmapWindow = lambda *a: XcbVoidCookieT(lib.xcb_unmap_window(*parseArgs(a)))
xcbWaitForEvent = lambda *a: XcbGenericEventT(lib.xcb_wait_for_event(*parseArgs(a)))
