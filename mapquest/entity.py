from enum import Enum
from panda3d.core import Vec3


class EntitySpawnType(Enum):
    WORLDSPAWN = 0
    MERGE_WORLDSPAWN = 1
    ENTITY = 2
    GROUP = 3


class Entity:
    def __init__(self):
        self.properties = {}
        self.brushes = []
        self.center = Vec3()
        self.spawn_type = EntitySpawnType.WORLDSPAWN
