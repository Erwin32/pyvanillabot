class ClickToMove:
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

class ObjectType:
    OT_NONE = 0
    OT_ITEM = 1
    OT_CONTAINER = 2
    OT_UNIT = 3
    OT_PLAYER = 4
    OT_GAMEOBJ = 5
    OT_DYNOBJ = 6
    OT_CORPSE = 7

class GameObjectType:
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


