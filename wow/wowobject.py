import pyvanillabot.globals

GuidPointer = 0x8
TypePointer = 0x14

class WowObject(object):

    def __init__(self, base_address):
        self.BlackMagic = pyvanillabot.globals.BlackMagic()

        self.BaseAddress = base_address
        self.Guid = self.BlackMagic.ReadUInt64(self.BaseAddress + GuidPointer)
        # TODO this might need to be ReadUShort()
        self.Type = self.BlackMagic.ReadUInt(self.BaseAddress + TypePointer)

        self.DescAddress = None
        self.Name = None
        self.Xpos = None
        self.Ypos = None
        self.Zpos = None
