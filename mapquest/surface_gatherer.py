from enum import Enum
class Surface:
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices


class SurfaceSplitType(Enum):
    NONE = 0
    ENTITY = 1
    BRUSH = 2


class SurfaceGatherer:
    def __init__(self):
        self.surfaces = []

    def set_split_type(self, split_type):
        pass

    def set_brush_filter_texture(self, texture_name):
        pass

    def set_face_filter_texture(self, texture_name):
        pass

    def set_entity_index_filter(self, entity_idx):
        pass

    def set_texture_filter(self, name):
        pass

    def set_worldspawn_layer_filter(self, filter):
        pass

    def run(self):
        pass

    def fetch(self):
        pass

    def filter_entity(self, entity_idx):
        pass

    def filter_brush(self, entity_idx, brush_idx):
        pass

    def filter_face(self, entity_idx, brush_idx, face_idx):
        pass

    def add_surface(self):
        pass

    def reset_state(self):
        pass

    def reset_params(self):
        pass