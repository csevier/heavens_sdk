from panda3d.core import Vec3, Mat4, Quat
from entity_geometry import VertexTangent, VertexUV
import math


class GeoGenerator:
    def __init__(self, map_data):
        self.map_data = map_data
        self.UP_VECTOR = Vec3(0, 0, 1)
        self.RIGHT_VECTOR = Vec3(0, 1, 0) # this will likely need changed for panda, forward is y.
        self.FORWARD_VECTOR = Vec3(1, 0, 0)
        self.smooth_normals = False
        self.wind_entity_idx = 0
        self.wind_brush_idx = 0
        self.wind_face_idx = 0
        self.wind_face_center = Vec3()
        self.wind_face_basis = Vec3()
        self.wind_face_normal = Vec3()
        self.EPSILON = 0.00001

    def sort_vertices_by_winding(self, lhs_in, rhs_in):
        face_inst = self.map_data.get_entities()[self.wind_entity_idx].brushes[self.wind_brush_idx].faces[self.wind_face_idx]
        face_geometry = self.map_data.entity_geo[self.wind_entity_idx].brushes[self.wind_brush_idx].faces[self.wind_face_idx]

        u = self.wind_face_basis.normalized()
        v = u.cross(self.wind_face_normal).normalized()

        local_lhs = lhs_in - self.wind_face_center
        lhs_pu = local_lhs.dot(u)
        lhs_pv = local_lhs.dot(v)

        local_rhs = rhs_in - self.wind_face_center
        rhs_pu = local_rhs.dot(u)
        rhs_pv = local_rhs.dot(v)

        lhs_angle = math.atan2(lhs_pv, lhs_pu)
        rhs_angle = math.atan2(rhs_pv, rhs_pu)

        if lhs_angle < rhs_angle:
            return -1
        elif lhs_angle > rhs_angle:
            return 1

        return 0

    def run(self):
        pass

    def generate_brush_vertices(self, entity_idx, brush_idx):
        pass

    def intersect_faces(self, f0, f1, f2, o_vertex):
        normal0 = f0.plane_normal
        normal1 = f1.plane_normal
        normal2 = f2.plane_normal

        denom = normal0.cross(normal1).dot(normal2)

        if denom < self.EPSILON:
            return False

        a = normal1.cross(normal2) * f0.plane_dist
        b = normal2.cross(normal0) * f1.plane_dist
        c = normal0.cross(normal1) * f2.plane_dist
        d = a + b
        e = d + c
        o_vertex = e / denom

        return True

    def vertex_in_hull(self, faces, vertex):
        for face in faces:
            proj = face.plane_normal.dot(vertex)

            if proj > face.plane_dist and abs(face.plane_dist - proj) > self.EPSILON:
                return False

        return True

    def get_standard_uv(self, vertex, face, texture_width, texture_height):
        uv_out = VertexUV()

        du = abs(face.plane_normal.dot(self.UP_VECTOR))
        dr = abs(face.plane_normal.dot(self.RIGHT_VECTOR))
        df = abs(face.plane_normal.dot(self.FORWARD_VECTOR))

        if du >= dr and du >= df:
            uv_out = VertexUV(vertex.x, -vertex.y)
        elif dr >= du and dr >= df:
            uv_out = VertexUV(vertex.x, -vertex.z)
        elif df >= du and df >=dr:
            uv_out = VertexUV(vertex.y, -vertex.z)

        angle = math.radians(face.uv_extra.rot)
        rotated = VertexUV()
        rotated.u = uv_out.u * math.cos(angle) - uv_out.v * math.sin(angle)
        rotated.v = uv_out.u * math.sin(angle) + uv_out.v * math.cos(angle)
        uv_out = rotated

        uv_out.u /= texture_width
        uv_out.v /= texture_height

        uv_out.u /= face.uv_extra.scale_x
        uv_out.v /= face.uv_extra.scale_y

        uv_out.u = face.uv_standard.u / texture_width
        uv_out.v = face.uv_standard.v / texture_height

        return uv_out

    def get_valve_uv(self, vertex, face, texture_width, texture_height):
        uv_out = VertexUV()
        u_axis = face.uv_valve.u.axis
        u_shift = face.uv_valve.u.offset
        v_axis = face.uv_valve.v.axis
        v_shift = face.uv_valve.v.offset

        uv_out.u = u_axis.dot(vertex)
        uv_out.v = v_axis.dot(vertex)

        uv_out.u /= texture_width
        uv_out.v /= texture_height

        uv_out.u /= face.uv_extra.scale_x
        uv_out.v /= face.uv_extra.scale_y

        uv_out.u += u_shift / texture_width
        uv_out.v += v_shift / texture_height

        return uv_out

    def get_standard_tangent(self, face):
        tangent_out = VertexTangent()
        du = face.plane_normal.dot(self.UP_VECTOR)
        dr = face.plane_normal.dot(self.RIGHT_VECTOR)
        df = face.plane_normal.dot(self.FORWARD_VECTOR)

        dua = abs(du)
        dra = abs(dr)
        dfa = abs(df)

        u_axis = None
        v_sign = 0

        if dua >= dra and dua >= dfa:
            u_axis = self.FORWARD_VECTOR
            v_sign = self.sign(du)
        elif dra >= dua and dra >= dfa:
            u_axis = self.FORWARD_VECTOR
            v_sign = -self.sign(dr)
        elif dfa >= dua and dfa >= dra:
            u_axis = self.RIGHT_VECTOR
            v_sign = self.sign(df)

        v_sign *= self.sign(face.uv_extra.scale_y)
        quat = Quat()
        quat.setFromAxisAngle(-face.uv_extra.rot * v_sign, face.plane_normal)
        # u_axis = vec3_rotate(u_axis, face->plane_normal, -face->uv_extra.rot * v_sign);
        u_axis = quat.xform(u_axis)

        tangent_out.x = u_axis.x
        tangent_out.y = u_axis.y
        tangent_out.z = u_axis.z
        tangent_out.w = v_sign

        return tangent_out

    def get_valve_tangent(self, face):
        tangent_out = VertexTangent()

        u_axis = face.uv_valve.u.axis.normalized()
        v_axis = face.uv_valve.v.axis.normalized()

        v_sign = -self.sign(face.plane_normal.cross(u_axis).dot(v_axis))
        tangent_out.x = u_axis.x
        tangent_out.y = u_axis.y
        tangent_out.z = u_axis.z
        tangent_out.w = v_sign

        return tangent_out

    def sign(self, v):
        if v > 0:
            return 1
        elif v < 0:
            return -1

        return 0

    def get_entities(self):
        return self.map_data.entity_geo

    def get_brush_vertex_count(self, entity_idx, brush_idx):
        brush = self.map_data.get_entities()[entity_idx].brushes[brush_idx]
        brush_geo = self.map_data.entity_geo[entity_idx].brushes[brush_idx]
        vertex_count = 0
        for face_idx, face in enumerate(brush.faces):
            face_geo = brush_geo.faces[face_idx]
            vertex_count += len(face_geo.vertices)

        return vertex_count

    def get_brush_index_count(self, entity_idx, brush_idx):
        brush = self.map_data.get_entities()[entity_idx].brushes[brush_idx]
        brush_geo = self.map_data.entity_geo[entity_idx].brushes[brush_idx]
        index_count = 0
        for face_idx, face in enumerate(brush.faces):
            face_geo = brush_geo.faces[face_idx]
            index_count += len(face_geo.indices)

        return index_count

