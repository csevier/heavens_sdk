from direct.showbase.DirectObject import DirectObject
from panda3d.core import Vec3
from direct.directtools.DirectUtil import CLAMP
from direct.gui.OnscreenText import OnscreenText
from melee_weapon import MeleeWeapon
from hitscan_weapon import HitscanWeapon


class FPSCharacter(DirectObject):
    def __init__(self):
        super().__init__()
        self.input_map = {"left_mouse_down": False,
                          "right_mouse_down": False,
                          "w": False,
                          "a": False,
                          "s": False,
                          "d": False, }
        self._setup_default_weapons()
        self._setup_camera()


    def _setup_camera(self):
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        base.disableMouse()
        base.taskMgr.add(self._handle_gimbal)
        self.gimbal_x = base.render.attachNewNode("gimbal_x")
        self.gimbal_y = self.gimbal_x.attachNewNode("gimbal_y")
        base.camera.reparentTo(self.gimbal_y)
        self.accept("w", self.update_input, ["w", True])
        self.accept("a", self.update_input, ["a", True])
        self.accept("s", self.update_input, ["s", True])
        self.accept("d", self.update_input, ["d", True])
        self.accept("w-up", self.update_input, ["w", False])
        self.accept("a-up", self.update_input, ["a", False])
        self.accept("s-up", self.update_input, ["s", False])
        self.accept("d-up", self.update_input, ["d", False])
        self.accept("mouse1", self.use)
        self.accept("wheel_up", self.change_weapon, extraArgs=[self.current_weapon + 1])
        self.accept("wheel_down",self.change_weapon, extraArgs=[self.current_weapon - 1])
        self.accept("1", self.change_weapon, extraArgs=[0])
        self.accept("2", self.change_weapon, extraArgs=[1])
        self.gimbal_x.setPos(self.gimbal_x, (0, -1, .5))
        self.crosshair = OnscreenText(text='+')

    def change_weapon(self, index):
        if index > -1 and index < self.weapons.getNumChildren():
            self.weapons.getChild(self.current_weapon).hide()
            self.current_weapon = index
            self.weapons.getChild(self.current_weapon).show()


    def _setup_default_weapons(self):
        self.weapons = base.render2d.attachNewNode("weapons")
        self.weapons.setPos(0, 0, -1)
        axe = MeleeWeapon(name="axe", texture_glob_pattern="axe_*.png", position=(-.5, 0, 0))
        gun = HitscanWeapon(name="gun", texture_glob_pattern="gun*.png", scale=0.2)
        axe.reparentTo(self.weapons)
        gun.reparentTo(self.weapons)
        axe.hide()
        gun.hide()
        self.current_weapon = 0
        self.change_weapon(0)

    def _handle_gimbal(self, task):
        if base.mouseWatcherNode.hasMouse():
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
            delta_x = self.last_mouse_x - x
            delta_y = self.last_mouse_y - y
            self.last_mouse_x = x
            self.last_mouse_y = y
            velocity = Vec3()
            if self.input_map["w"]:
                velocity += Vec3.forward()
            if self.input_map["s"]:
                velocity += Vec3.back()
            if self.input_map["a"]:
                velocity += Vec3.left()
            if self.input_map["d"]:
                velocity += Vec3.right()
            velocity = velocity.normalized()

            self.gimbal_x.setH(self.gimbal_x, delta_x * 10000 * globalClock.get_dt())
            pitch = -(delta_y * 10000 * globalClock.get_dt())
            projected_pitch = self.gimbal_y.getP() + pitch
            if projected_pitch > 90:
                self.gimbal_y.setP(90)
            elif projected_pitch < -90:
                self.gimbal_y.setP(-90)
            else:
                self.gimbal_y.setP(self.gimbal_y, pitch)

            self.gimbal_x.setPos(self.gimbal_x, velocity * 5 * globalClock.get_dt())

        return task.cont

    def update_input(self, letter, value):
        self.input_map[letter] = value

    def _zoom_in(self):
        fov = base.camNode.getLens().getFov()
        base.camNode.getLens().setFov(CLAMP(fov.x - 5, 25, 90))

    def _zoom_out(self):
        fov = base.camNode.getLens().getFov()
        base.camNode.getLens().setFov(CLAMP(fov.x + 5, 25, 90))

    def use(self):
        self.weapons.getChild(self.current_weapon).node().getPythonTag("weapon").use()




