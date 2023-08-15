from direct.showbase.ShowBase import ShowBase
from panda3d.core import (WindowProperties,
                          loadPrcFileData)

from direct.directtools.DirectGeometry import LineNodePath
from fps_character import FPSCharacter
from sprite import Sprite
import sys
loadPrcFileData("", "show-frame-rate-meter #t")
loadPrcFileData("", "sync-video #t")


class Heaven(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # Set properties of the Panda3D window
        props = WindowProperties()
        props.set_size(1080, 670)
        props.setCursorHidden(True)
        props.setMouseMode(WindowProperties.M_relative)
        base.win.requestProperties(props)
        self.draw_origin()
        self.accept("p", self.toggleWireframe)
        self.accept("q", sys.exit)
        self.player = FPSCharacter()
        self.enemy = Sprite()
        self.enemy2 = Sprite()
        self.enemy2.setPos(self.enemy2, (4, 0, 0))
        self.enemy3 = Sprite()
        self.enemy3.setPos(self.enemy3, (8, 0, 0))

    def draw_origin(self):
        x = [(-1000,0,0), (1000,0,0)]
        y = [(0,-1000,0), (0,1000,0)]
        z = [(0,0,-1000), (0,0,1000)]
        self.global_x = LineNodePath(name="global_x", parent=self.render, thickness=1.0, colorVec=(1, 0, 0, 1))
        self.global_x.drawLines([x])
        self.global_x.create()
        self.global_y = LineNodePath(name="global_y", parent=self.render, thickness=1.0, colorVec=(0, 1, 0, 1))
        self.global_y.drawLines([y])
        self.global_y.create()
        self.global_z = LineNodePath(name="global_z", parent=self.render, thickness=1.0, colorVec=(0, 0, 1, 1))
        self.global_z.drawLines([z])
        self.global_z.create()


Heaven().run()
