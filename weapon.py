from panda3d.core import (CardMaker,
                          TransparencyAttrib,
                          SequenceNode,
                          SamplerState,
                          NodePath,
                          Vec3)

import glob


class Weapon(NodePath):
    def __init__(self,
                 name="default_weapon",
                 texture_glob_pattern="*.png",
                 frame_rate=24,
                 position=Vec3(0, 0, 0),
                 scale=1):
        super().__init__(name)
        self.setPythonTag("weapon", self)
        self.texture_locations = glob.glob(f"textures/{texture_glob_pattern}")
        self.texture_locations.sort()
        self.textures = [base.loader.loadTexture(file) for file in self.texture_locations]
        self.sequence = SequenceNode(self.getName())
        self.sequence.setFrameRate(frame_rate)
        self.seqNP = self.attachNewNode(self.sequence)
        self.setPos(position)
        self.setScale(scale)
        cm = CardMaker(self.getName())
        for texture in self.textures:
            texture.setMagfilter(SamplerState.FT_nearest)
            texture.setMinfilter(SamplerState.FT_nearest)
            frame = self.seqNP.attachNewNode(cm.generate())
            frame.setTexture(texture)
            frame.setTransparency(TransparencyAttrib.MAlpha)

        self.setup()

    def setup(self): # override defaults here
        pass

    def use(self):
        self.sequence.play(0, self.sequence.getNumFrames())


