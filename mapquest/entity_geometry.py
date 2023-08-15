class VertexUV:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class VertexTangent:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


class FaceVertex:
    def __init__(self, vertex, normal, uv, tangent):
        self.vertex = vertex
        self.normal = normal
        self.uv = uv
        self.tangent = tangent


class FaceGeometry:
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices


class BrushGeometry:
    def __init__(self, faces):
        self.faces = faces


class EntityGeometry:
    def __init__(self, brushes):
        self.brushes = brushes



