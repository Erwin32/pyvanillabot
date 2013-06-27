class Globals(object):

    def __init__(self):

        self.ClientConnection = None
        self.ClientConnectionOffset = None
        self.ClientConnectionPointer = None
        self.CurMgr = None

        self.PlayerBaseOffset = self.get_player_base_offset()
        self._player_base_offset= None

    def get_player_base_offset(self):

        if self._player_base_offset:
            return self._player_base_offset

        if ProcessManager.WowProcess:
            try:
                _player_base_offset = ProcessManager.WowProcess.ReadUInt(
                                        ProcessManager.WowProcess.ReadUInt(
                                            ProcessManager.WowProcess.ReadUInt))


