class Static:
    LocalTargetGUID = 0x74e2d8
    LocalPlayerGUID = 0x741e30

class ObjectManager:
    CurMgrPointer = 0x00741414
    CurMgrOffset = 0xAC
    NextObject = 0x3c
    FirstObject = 0xAC
    LocalGUID = 0xC0

class UnitName:
    ItemType = WowObject.DataPTR + 0x54

    PlayerNameCachePointer = 0x80E230
    PlayerNameGUIDOffset = 0xc
    PlayerNameStringOffset = 0x14

class WowObject:
    DataPTR = 0x8
    Type = 0x14
    Guid = 0x30
    X = 0x898
    Y = X + 0x4
    Z = X + 0x8
    RotationOffset = X + 0x10
    GameObjectY = 0x2C4  #*DataPTR (0x288) + 0x3c
    GameObjectX = GameObjectY + 0x4
    GameObjectZ = GameObjectY + 0x8
    Speed = 0xA34
