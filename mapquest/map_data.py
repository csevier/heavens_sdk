class TextureData:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height


class WorldSpawnLayer:
    def __init__(self, texture_idx, build_visuals):
        self.texture_idx = texture_idx
        self.build_visuals = build_visuals


class MapData:
    def __init__(self):
        self.entities = []
        self.entity_geo = []
        self.textures = []
        self.world_spawn_layers = []

    def reset(self):
        pass

    def register_worldspawn_layer(self, name, build_visuals):
        pass

    def find_worldspawn_layer(self, texture_idx):
        pass

    def get_worldspawn_layer_count(self):
        pass

    def get_worldspawn_layers(self):
        pass

    def register_texture(self, name):
        pass

    def set_texture_size(self, name, height, width):
        pass

    def get_texture_count(self):
        pass

    def get_textures(self):
        pass

    def find_texture(self, name):
        pass

    def get_texture(self, texture_idx):
        pass

    def set_spawn_type_by_classname(self, name, spawn_type):
        pass

    def print_entities(self):
        pass

    def get_entity_count(self):
        pass

    def get_entities(self):
        pass

    def get_entity_property(self, entity_idx, key):
        pass