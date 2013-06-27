import math
from pyvanillabot.wow_object import WowObject

class LocalPlayer(WowObject):


    def set_facing_location(self, target_x, target_y):
        tempangle = math.atan2((target_x - self.Xpos), (target_y - self.Ypos))

        if tempangle < 0:
            target_angle = tempangle + (2 * math.pi)
        else:
            target_angle = tempangle

        if not (self.rotation - target_angle) < 0.014:
            # make sure it is written as a float
            GameReader.write_wow_mem(self.BaseAddress + RotationOffset, target_angle)
            self.rotation = target_angle
