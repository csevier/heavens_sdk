from weapon import Weapon
from panda3d.core import Vec3, CollisionBox, CollisionNode, GeomNode, CollisionHandlerQueue , CollisionTraverser


class MeleeWeapon(Weapon):
    def __init__(self,
                 name="default_weapon",
                 texture_glob_pattern="*.png",
                 frame_rate=24,
                 position=Vec3(0, 0, 0),
                 scale=1):
        super().__init__(name,
                         texture_glob_pattern,
                         frame_rate,
                         position,
                         scale)
        self.setPythonTag("weapon", self)

    def use(self):
        super().use()
        hitbox = CollisionNode('melee_swipe')
        hitbox_np = base.camera.attachNewNode(hitbox)
        cb = CollisionBox((0,1,0), 1, 1 ,1)
        hitbox.addSolid(cb)
        queue_handler = CollisionHandlerQueue()
        traverser = CollisionTraverser('melee_traverser')
        traverser.addCollider(hitbox_np, queue_handler)
        traverser.showCollisions(base.render)
        traverser.traverse(base.render)
        if queue_handler.getNumEntries() > 0:
            # This is so we get the closest object
            queue_handler.sortEntries()
            hit_object = queue_handler.getEntry(0).getIntoNodePath()

        hitbox_np.remove_node()
