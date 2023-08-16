from enum import Enum


class Surface:
    def __init__(self, vertices=None, indices=None):
        if vertices is None:
            self.vertices = []
        else:
            self.vertices = vertices

        if indices is None:
            self.indices = []
        else:
            self.indices = indices


class SurfaceSplitType(Enum):
    NONE = 0
    ENTITY = 1
    BRUSH = 2


class SurfaceGatherer:
    def __init__(self, map_data):
        self.map_data = map_data
        self.split_type = SurfaceSplitType.NONE
        self.entity_filter_idx = -1
        self.texture_filter_idx = -1
        self.brush_filter_texture_idx = -1
        self.face_filter_texture_idx = -1
        self.filter_worldspawn_layers = True
        self.out_surfaces = []

    def set_split_type(self, split_type):
        self.split_type = split_type

    def set_entity_index_filter(self, entity_idx):
        self.entity_filter_idx = entity_idx

    def set_texture_filter(self, texture_name):
        self.texture_filter_idx = self.map_data.find_texture(texture_name)

    def set_brush_filter_texture(self, texture_name):
        self.brush_filter_texture_idx = self.map_data.find_texture(texture_name)

    def set_face_filter_texture(self, texture_name):
        self.face_filter_texture_idx = self.map_data.find_texture(texture_name)

    def set_worldspawn_layer_filter(self, world_spawn_filter):
        self.filter_worldspawn_layers = world_spawn_filter

    def run(self):
        pass

    def fetch(self):
        return self.out_surfaces

    def filter_entity(self, entity_idx):
        entity = self.map_data.get_entities()[entity_idx] # wtf?

        if self.entity_filter_idx != -1 and self.entity_filter_idx != entity_idx:
            return True

        return False

    def filter_brush(self, entity_idx, brush_idx):
        brush = self.map_data.get_entities()[entity_idx].brushes[brush_idx]
        if self.brush_filter_texture_idx != -1:
            fully_textured = True
            for face in brush.faces:
                if face.texture_idx != self.brush_filter_texture_idx:
                    fully_textured = False
                    break

            if fully_textured:
                return True

        for face in brush.faces:
            for layer in self.map_data.worldspawn_layers:
                if face.texture_idx == layer.texture_idx:
                    return self.filter_worldspawn_layers

        return False

    def filter_face(self, entity_idx, brush_idx, face_idx):
        pass

    def add_surface(self):
        pass

    def reset_state(self):
        self.out_surfaces.clear()

    def reset_params(self):
        self.split_type = SurfaceSplitType.NONE
        self.entity_filter_idx = -1
        self.texture_filter_idx = -1
        self.brush_filter_idx = -1
        self.face_filter_texture_idx = -1
        self.filter_worldspawn_layers = True