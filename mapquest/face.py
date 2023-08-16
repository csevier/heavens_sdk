from panda3d.core import Vec3


class FacePoints:
    def __init__(self, v0=Vec3(), v1=Vec3(), v2=Vec3()):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2


class StandardUV:
    def __init__(self, u=0.0, v=0.0):
        self.u = u
        self.v = v


class ValveTextureAxis:
    def __init__(self, axis=Vec3(), offset=0.0):
        self.axis = axis
        self.offset = offset


class ValveUV:
    def __init__(self, valve_texture_u=ValveTextureAxis(), valve_texture_v=ValveTextureAxis()):
        self.u = valve_texture_u
        self.v = valve_texture_v


class FaceUVExtra:
    def __init__(self, rot=0.0, scale_x=0.0, scale_y=0.0):
        self.rot = rot
        self.scale_x = scale_x
        self.scale_y = scale_y


class Face:
    def __init__(self, plane_points=FacePoints(),
                 plane_normal=Vec3(),
                 plane_distance=0.0,
                 texture_index=0,
                 is_valve_uv=False,
                 uv_valve=ValveUV(),
                 uv_standard=StandardUV(),
                 uv_extra=FaceUVExtra()):
        self.plane_points = plane_points
        self.plane_normal = plane_normal
        self.plane_distance = plane_distance
        self.texture_index = texture_index
        self.is_valve_uv = is_valve_uv
        self.uv_valve = uv_valve
        self.uv_standard = uv_standard
        self.uv_extra = uv_extra
