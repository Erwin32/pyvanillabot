from ctypes import *
import math
from offsets.Offsets import *

from pyvanillabot.processmanager import ProcessManager as PM
from pyvanillabot.wowobject import WowObject
from pyvanillabot.globals import BlackMagic

FieldsOffset = c_uint(0x8)
PlayerHealthOffset = c_uint(0x68)
XposOffset = c_uint(0x898)
YposOffset = c_uint(XposOffset + 0x4)
ZposOffset = c_uint(XposOffset + 0x8)
RotationOffset = c_uint(0x8A8)
UnitNameOffset1 = c_uint(0xA24)
UnitNameOffset2 = c_uint(0x60)
ObjNameOffset1 = c_uint(0x1CC)
ObjNameOffset2 = c_uint(0xB4)

BaseStaticPointer = c_uint(0x89ACC0 + 0x8)
MaskOffset = c_uint(0x024)
BaseOffset = c_uint(0x1c)
StringOffset = c_uint(0x020)

TargetDesc = 0x40 / 4,
HealthDesc = 0x58 / 4,
ManaDesc = 0x5c / 4,
MaxHealthDesc = 0x70 / 4,
MaxManaDesc = 0x74 / 4,
LevelDesc = 0x88 / 4,

class Player(WowObject):

    def __init__(self):
        self.Guid = 0xB8
        self.BaseAddress = PM.GetObjBaseFromGuid(self.Guid)
        self.FieldsAddress = BlackMagic.ReadUInt(self.BaseAddress + FieldsOffset)

        self.Name = PM.PlayerNameFromGuid(self.Guid)

        self.Xpos = BlackMagic.ReadFloat(self.BaseAddress + XposOffset)
        self.Ypos = BlackMagic.ReadFloat(self.BaseAddress + YposOffset)
        self.Zpos = BlackMagic.ReadFloat(self.BaseAddress + ZposOffset)
        self.Rotation = BlackMagic.ReadFloat(self.BaseAddress + RotationOffset)

        self.MaxHealth = BlackMagic.ReadUInt(self.FieldsAddress + (MaxHealthDesc * 4))
        self.CurHealth = BlackMagic.ReadUInt(self.FieldsAddress + (CurHealthDesc * 4))
        self.MaxMana = BlackMagic.ReadUInt(self.FieldsAddress + (MaxHealthDesc * 4))
        self.CurMana = BlackMagic.ReadUInt(self.FieldsAddress + (MaxHealthDesc * 4))
        self.Level = BlackMagic.ReadUInt(self.FieldsAddress + (LevelDesc * 4))

    def get_addr(self, force_refresh=False):
        if self.BaseAddress is None or force_refresh:
            self.BaseAddress = c_uint(GameReader.get_mem_addr(self.GUID))
        return self.BaseAddress

    def get_descriptor(self, force_refresh=False):
        if self.descriptor is None or force_refresh:
            self.descriptor = c_uint(GameReader.read_wow_mem(self.BaseAddress + DescriptorOffset))
        return self.descriptor

    def get_health(self, force_refresh=False):
        if self.health is None or force_refresh:
            self.health = c_uint(GameReader.read_wow_mem(self.descriptor + PlayerHealthOffset))
        return self.health

    def get_name(self):
        mask = GameReader.read_wow_mem(WowBaseAddress + BaseStaticPointer + MaskOffset)
        base = GameReader.read_wow_mem(WowBaseAddress + BaseStaticPointer + BaseStaticPointer)
        short_guid = self.GUID&0xFFFFFFFF
        if mask == 0xFFFFFFFF:
            return ""

        offset = 12 * (mask&short_guid)
        current = GameReader.read_wow_mem(WowBaseAddress + offset + 8)
        offset = GameReader.read_wow_mem(WowBaseAddress + offset)
        if current&0x1 == 0x1:
            return ""

        test_guid = GameReader.read_wow_mem(current)
        while test_guid != short_guid:
            current = GameReader.read_wow_mem(current + offset + 4)
            if current&0x1 == 0x1:
                return ""
            test_guid = GameReader.read_wow_mem(current)

        # should be char[20]
        return GameReader.read_wow_mem(current + 0x20)


    def get_location(self):
        self.Xpos = c_uint(GameReader.read_wow_mem(self.BaseAddress + XLocOffset))
        self.Ypos = c_uint(GameReader.read_wow_mem(self.BaseAddress + YLocOffset))
        self.Zpos = c_uint(GameReader.read_wow_mem(self.BaseAddress + ZLocOffset))
        return (self.Xpos, self.Ypos, self.Zpos)

    def get_facing_dir(self):
        self.rotation = c_uint(GameReader.read_wow_mem(self.BaseAddress + RotationOffset))
        return self.rotation

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

    def get_unit_name(self):
        unit_addr = GameReader.get_mem_addr(self.GUID)
        name_addr_1 = GameReader.read_wow_mem(addr + UnitNameOffset1)
        name_addr_2 = GameReader.read_wow_mem(name1 + UnitNameOffset2)

        # should be of type char[20]
        return GameReader.read_wow_mem(name_addr_2)

    def get_unit_name(self):
        obj_addr = GameReader.get_mem_addr(self.GUID)
        name_addr_1 = GameReader.read_wow_mem(addr + ObjNameOffset1)
        name_addr_2 = GameReader.read_wow_mem(name1 + ObjNameOffset2)

        # should be of type char[20]
        return GameReader.read_wow_mem(name_addr_2)
