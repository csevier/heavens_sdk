class FacePoints:
    def __init__(self, v0, v1, v2):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2


class StandardUV:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class ValveTextureAxis:
    def __init__(self, axis, offset):
        self.axis = axis
        self.offset = offset


class ValveUV:
    def __init__(self, valve_texture_u, valve_texture_v):
        self.u = valve_texture_u
        self.v = valve_texture_v


class FaceUVExtra:
    def __init__(self, rot, scale_x, scale_y):
        self.rot = rot
        self.scale_x = scale_x
        self.scale_y = scale_y


class Face:
    def __init__(self, plane_points, plane_normal, plane_distance, texture_index, is_valve_uv, valve_uv, standard_uv, uv_extra):
        self.plane_points = plane_points
        self.plane_normal = plane_normal
        self.plane_distance = plane_distance
        self.texture_index = texture_index
        self.is_valve_uv = is_valve_uv
        self.valve_uv = valve_uv
        self.standard_uv = standard_uv
        self.uv_extra = uv_extra
