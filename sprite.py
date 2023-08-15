from direct.showbase.DirectObject import DirectObject
from panda3d.core import (CardMaker,
                          TransparencyAttrib,
                          SequenceNode,
                          SamplerState,
                          CollisionBox,
                          CollisionNode,
                          NodePath)


class Sprite(NodePath):
    def __init__(self):
        super().__init__("sprite")
        self.setup()
    def setup(self):
        self.reparentTo(base.render)
        sn = SequenceNode("sprite")
        sn.setFrameRate(2)
        sequence = self.attachNewNode(sn)
        cm = CardMaker("card1")
        frame1 = sequence.attachNewNode(cm.generate())
        frame1.setPos(frame1, (-0.5, 0, 0))
        cm = CardMaker("card2")
        frame2 = sequence.attachNewNode(cm.generate())
        frame2.setPos(frame2, (-0.5, 0, 0))
        text = base.loader.loadTexture("textures/boss1.png")
        text2 = base.loader.loadTexture("textures/boss2.png")
        text.setMagfilter(SamplerState.FT_nearest)
        text.setMinfilter(SamplerState.FT_nearest)
        text2.setMagfilter(SamplerState.FT_nearest)
        text2.setMinfilter(SamplerState.FT_nearest)
        frame1.setTexture(text)
        frame1.setTransparency(TransparencyAttrib.MAlpha)
        frame2.setTexture(text2)
        frame2.setTransparency(TransparencyAttrib.MAlpha)
        sequence.node().loop(True)
        sequence.setBillboardAxis()
        cn = CollisionNode("sprite")
        cs = CollisionBox((0, 0, 0.5), 0.5, 0.5, 0.5)
        cn.addSolid(cs)
        self.attachNewNode(cn)
