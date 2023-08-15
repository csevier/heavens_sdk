from weapon import Weapon
from panda3d.core import GeomNode,Vec3, CollisionNode, CollisionRay, CollisionHandlerQueue, CollisionTraverser


class HitscanWeapon(Weapon):
    def __init__(self,
                 name="default_hitscan_weapon",
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
        hit_scan = CollisionNode('hit_scan')
        hit_scan_np = base.camera.attachNewNode(hit_scan)
        hit_scan_ray = CollisionRay()
        hit_scan_ray.setFromLens(base.camNode, 0, 0)
        hit_scan.addSolid(hit_scan_ray)
        queue_handler = CollisionHandlerQueue()
        traverser = CollisionTraverser('hit_scan_traverser')
        traverser.addCollider(hit_scan_np, queue_handler)
        traverser.showCollisions(base.render)
        traverser.traverse(base.render)
        if queue_handler.getNumEntries() > 0:
            # This is so we get the closest object
            queue_handler.sortEntries()
            shot_object = queue_handler.getEntry(0).getIntoNodePath()

        hit_scan_np.remove_node()
