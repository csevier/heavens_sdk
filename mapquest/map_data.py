class TextureData:
    def __init__(self, name="", width=0, height=0):
        self.name = name
        self.width = width
        self.height = height


class WorldSpawnLayer:
    def __init__(self, texture_idx=0, build_visuals=False):
        self.texture_idx = texture_idx
        self.build_visuals = build_visuals


class MapData:
    def __init__(self):
        self.entities = []
        self.entity_geo = []
        self.textures = []
        self.worldspawn_layers = []

    def reset(self):
        self.entities.clear()
        self.entity_geo.clear()
        self.textures.clear()
        self.worldspawn_layers.clear()

    def register_worldspawn_layer(self, name, build_visuals):
        wsl = WorldSpawnLayer()
        wsl.texture_idx = self.find_texture(name)
        wsl.build_visuals = build_visuals

    def find_worldspawn_layer(self, texture_idx):
        for index, wsl in enumerate(self.worldspawn_layers):
            if wsl.texture_idx == texture_idx:
                return index
        return -1

    def get_worldspawn_layer_count(self):
       return len(self.worldspawn_layers)

    def get_worldspawn_layers(self):
        return self.worldspawn_layers

    def register_texture(self, name):
        for index, text in enumerate(self.textures):
            if text.name == name:
                return index
        td = TextureData(name)
        self.textures.append(td)
        return len(self.textures) - 1

    def set_texture_size(self, name, height, width):
        for index, text in enumerate(self.textures):
            if text.name == name:
                text.width = width
                text.height = height

    def get_texture_count(self):
        return len(self.textures)

    def get_textures(self):
        return self.textures

    def get_texture(self, texture_idx):
        return self.textures[texture_idx]

    def find_texture(self, name):
        for index, text in enumerate(self.textures):
            if text.name == name:
                return index
        return -1

    def set_spawn_type_by_classname(self, key, spawn_type):
        for entity in self.entities:
            if len(entity.properties) == 0:
                continue

            if entity.properties["classname"] == key:
                entity.spawn_type = spawn_type

    def print_entities(self):
        for entity in self.entities:
            print(entity)

    def get_entity_count(self):
        return len(self.entities)

    def get_entities(self):
        return self.entities

    def get_entity_property(self, entity_idx, key):
        return self.entities[entity_idx].properties[key]