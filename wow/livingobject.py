#import math
from pyvanillabot.constants import *
from pyvanillabot.manager.process_manager import ProcessManager as PM
import pyvanillabot.globals
from pyvanillabot.wow.wowobject import WowObject

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

class LivingObject(WowObject):

    def __init__(self, base_address):
        super(LivingObject, self).__init__(base_address)

        self.DescAddress = self.get_descriptor_address()
        self.Name = self.get_name()

        self.Xpos = self.BlackMagic.ReadFloat(self.BaseAddress + XposOffset)
        self.Ypos = self.BlackMagic.ReadFloat(self.BaseAddress + YposOffset)
        self.Zpos = self.BlackMagic.ReadFloat(self.BaseAddress + ZposOffset)
        self.Rotation = self.BlackMagic.ReadFloat(self.BaseAddress + RotationOffset)

        self.MaxHealth = self.BlackMagic.ReadUInt(self.FieldsAddress + (MaxHealthDesc * 4))
        self.CurHealth = self.BlackMagic.ReadUInt(self.FieldsAddress + (CurHealthDesc * 4))
        self.MaxMana = self.BlackMagic.ReadUInt(self.FieldsAddress + (MaxHealthDesc * 4))
        self.CurMana = self.BlackMagic.ReadUInt(self.FieldsAddress + (MaxHealthDesc * 4))
        self.Level = self.BlackMagic.ReadUInt(self.FieldsAddress + (LevelDesc * 4))

    def get_base_address(self, force_refresh=False):
        if self.BaseAddress is None or force_refresh:
            BaseAddress = self.BlackMagic.ReadUInt(self.Guid)
            return BaseAddress
        else:
            return self.BaseAddress

    def get_descriptor_address(self, force_refresh=False):
        if self.DescAddress is None or force_refresh:
            desc_addr = self.BlackMagic.ReadUInt(self.BaseAddress + DataPtr)
            return desc_addr
        else:
            return self.DescAddress

    def get_name(self):
        if self.Type == 4:
            name_db_ptr = Wow.BaseAddress + UnitName.PlayerNameCachePointer
            base = self.BlackMagic.ReadUInt(name_db_ptr)
            test_guid = self.BlackMagic.ReadUInt64(base + UnitName.PlayerNameGuidOffset)

            while (test_guid != self.Guid):
                base = self.BlackMagic.ReadUInt(base)
                test_guid = self.BlackMagic.ReadUInt64(base + UnitName.PlayerNameGuidOffset)

            name = PM.read_ascii_string(base + UnitName.PlayerNameStringOffset)
            return name
        if self.Type == 3:
            base = PM.GetObjBaseFromGuid(self.Guid)
            unitname_1 = self.BlackMagic.ReadUInt(base + UnitName.UnitNameOffset1)
            unitname_2 = self.BlackMagic.ReadUInt(unitname_1 + UnitName.UnitNameOffset2)

            name = PM.read_ascii_string(unitname_2)
            return name

