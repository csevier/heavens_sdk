from direct.showbase.ShowBase import ShowBase
from panda3d.core import (WindowProperties,
                          loadPrcFileData,
                          GeomVertexFormat,
                          GeomVertexData,
                          Geom,
                          GeomVertexWriter,
                          GeomTriangles,
                          GeomNode)

from direct.directtools.DirectGeometry import LineNodePath
from fps_character import FPSCharacter
from sprite import Sprite
import sys
from mapquest.map_parser import MapParser
from mapquest.geo_generator import  GeoGenerator
loadPrcFileData("", "show-frame-rate-meter #t")
loadPrcFileData("", "sync-video #t")
# loadPrcFileData("", "want-directtools #t")
# loadPrcFileData("", "want-tk #t")


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
        self.load_map("qodot_test.map")

    def load_map(self, map_name):
        mp = MapParser()
        mp.parser_load(f"./mapquest/test_maps/{map_name}")
        mp.map_data.load_texture_data()
        geo_gen = GeoGenerator(mp.map_data)
        geo_gen.run()
        print("loaded starting panda conversion")
        for entity_idx, entity_geo in enumerate(mp.map_data.entity_geo):
            for brush_idx, brush in enumerate(entity_geo.brushes):
                for face_idx, face in enumerate(brush.faces):
                    vdata = GeomVertexData('name', GeomVertexFormat.getV3n3t2(), Geom.UHStatic)
                    vertex = GeomVertexWriter(vdata, 'vertex')
                    normal = GeomVertexWriter(vdata, 'normal')
                    texcoord = GeomVertexWriter(vdata, 'texcoord')
                    prim = GeomTriangles(Geom.UHStatic)
                    for vert in face.vertices:
                        vertex.addData3(vert.vertex.x, vert.vertex.y, vert.vertex.z)
                        normal.addData3(vert.normal.x, vert.normal.y, vert.normal.z)
                        texcoord.addData2(vert.uv.u, vert.uv.v)
                    for indice in face.indices:
                        prim.addVertex(indice)

                    prim.closePrimitive()
                    geom = Geom(vdata)
                    geom.addPrimitive(prim)
                    node = GeomNode('brush_face')
                    node.addGeom(geom)
                    texture_id = mp.map_data.get_entities()[entity_idx].brushes[brush_idx].faces[face_idx].texture_idx
                    texture = mp.map_data.get_texture(texture_id)
                    np = base.render.attachNewNode(node)
                    # set texture
                    np.setTexture(texture.p3d_texture, 1)
                    np.setScale(0.01)
                    np.setTwoSided(True)


Heaven().run()
