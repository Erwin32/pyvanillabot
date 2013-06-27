from pyvanillabot.wow.wowobject import WowObject

# TODO or is it 0x288
DataPtr = 0x8
Xpointer = DataPtr + 0x3C
Ypointer = Xpointer + 0x4
Zpointer = Xpointer + 0x8

class WorldObject(WowObject):

    def __init__(self, base_address):
        super(WorldObject, self).__init__(base_address)

        self.Xpos = self.BlackMagic.ReadFloat(self.BaseAddress + Xpointer)
        self.Ypos = self.BlackMagic.ReadFloat(self.BaseAddress + Ypointer)
        self.Zpos = self.BlackMagic.ReadFloat(self.BaseAddress + Zpointer)

        self.DescAddress = self.BlackMagic.ReadUInt(self.BaseAddress + DataPtr)
        self.Name = self.get_name()
        self.ObjectType = self.get_obj_type()

    def get_name(self):
        name1 = self.BlackMagic.ReadUInt(self.BaseAddress + ObjectName1)
        name2 = self.BlackMagic.ReadUInt(name1 + ObjectName2)
        return self.BlackMagic.ReadASCIIString(name2)

    def get_object_type(self):
        obj_type = self.BlackMagic.ReadUInt(self.BaseAddress + ItemTypePointer)
        return obj_type

    def get_name_from_guid(self):
        name1 = self.BlackMagic.ReadUInt(self.BaseAddress + )
        return self.BlackMagic.ReadASCIIString()
