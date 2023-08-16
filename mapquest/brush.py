from panda3d.core import Vec3


class Brush:
    def __init__(self, faces=None, center=Vec3()):
        if faces is None:
            self.faces = []
        else:
            self.faces = faces
        self.center = center

