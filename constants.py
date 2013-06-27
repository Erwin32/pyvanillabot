class ClickToMoveConst:
    LeftClick = 0x1
    Face = 0x2
    Stop_ThrowsException = 0x3
    Move = 0x4
    NpcInteract = 0x5
    Loot = 0x6
    ObjInteract = 0x7
    Skin = 0x9
    AttackPosition = 0xA
    AttackGuid = 0xB
    ConstantFace = 0xC
    FaceOther = 0x8

class ObjectTypeConst:
    OT_NONE = 0
    OT_ITEM = 1
    OT_CONTAINER = 2
    OT_UNIT = 3
    OT_PLAYER = 4
    OT_GAMEOBJ = 5
    OT_DYNOBJ = 6
    OT_CORPSE = 7

class GameObjectTypeConst:
    Door = 0
    Button = 1
    QuestGiver = 2
    Chest = 3
    Binder = 4
    Generic = 5
    Trap = 6
    Chair = 7
    SpellFocus = 8
    Text = 9
    Goober = 0xa
    Transport = 0xb
    AreaDamage = 0xc
    Camera = 0xd
    WorldObj = 0xe
    MapObjTransport = 0xf
    DuelArbiter = 0x10
    FishingNode = 0x11
    Ritual = 0x12
    Mailbox = 0x13
    AuctionHouse = 0x14
    SpellCaster = 0x16
    MeetingStone = 0x17
    Unkown18 = 0x18
    FishingPool = 0x19
    FORCEDWORD = 0xFFFFFFFF

class StaticPointers:
    LocalTargetGUID = 0x74e2d8
    LocalPlayerGUID = 0x741e30

class ObjectManagerPointers:
    CurMgrPointer = 0x00741414
    CurMgrOffset = 0xAC
    NextObject = 0x3c
    FirstObject = 0xAC
    LocalGUID = 0xC0

class UnitNamePointers:
    # pointing to itemtype of object description
    ObjectName1 = 0x214
    ItemType = 0x2DC  #*DataPTR (0x288) + 0x54
    ObjectName2 = 0x8
    UnitName1 = 0xB30
    UnitName2 = 0x0

    PlayerNameCachePointer = 0x80E230
    PlayerNameGUIDOffset = 0xc
    PlayerNameStringOffset = 0x14

class WowObjectPointers:
    DataPTR = 0x8
    Type = 0x14
    Guid = 0x30
    Y = 0x9b8
    X = Y + 0x4
    Z = Y + 0x8
    #FIXME unsure if RotationOffset is correct
    RotationOffset = X + 0x10
    GameObjectY = 0x2C4  #*DataPTR (0x288) + 0x3c
    GameObjectX = GameObjectY + 0x4
    GameObjectZ = GameObjectY + 0x8
    Speed = 0xA34

class WowUnitDescriptors:
        Charm = 0x18 / 4
        Summon = 0x20 / 4
        CharmedBy = 0x28 / 4
        SummonedBy = 0x30 / 4
        CreatedBy = 0x38 / 4
        Target = 0x40 / 4
        ChannelObject = 0x50 / 4
        Health = 0x58 / 4
        Power = 0x5c / 4
        MaxHealth = 0x70 / 4
        MaxPower = 0x74 / 4
        Level = 0x88 / 4
