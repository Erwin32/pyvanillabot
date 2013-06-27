from ctypes import *
import os

from pyvanillabot.constants import *

import clr
clr.AddReference("BlackMagic.dll")
from Magic import BlackMagic

PROCESS_ALL_ACCESS = 0x1F0FFF

class StaticPointers:
    LocalTargetGUID = 0x74e2d8
    LocalPlayerGUID = 0x741e30

class ObjectManagerPointers:
    CurMgrPointer = 0x00741414
    CurMgrOffset = 0xAC
    NextObject = 0x3c
    FirstObject = 0xAC
    LocalGUID = 0xC0

class GameReader(object):

    def __init__(self):

        self.Process = None

        self.BaseAddress = None
        self.StaticClientConnection = self.BaseAddress + ObjectManagerPointers.CurMgrPointer

        self.PlayerGUID = c_uint(0xB8)
        self.CurrentTargetGUID = c_uint(self.BaseAddress)

        # created from the BaseAddress of wow
        self.ClientConnection = c_uint(self.BaseAddress + 0x8BF1A8)
        self.ObjManager = c_uint(self.BaseAddress + 0x462C)
        # Offsets required to find items
        self.FirstObjOffset = c_uint(0xB4)
        self.NextObjOffset = c_uint(0x3C)
        self.GameObjTypeOffset = c_uint(0x14)
        self.GameObjGUIDOffset = c_uint(0x30)

        self.FirstObj = c_uint(0)

        self.TotalWowObjs = c_uint(0)

    def read_ascii_string(address):
        return BlackMagic.ReadASCIIString(address, 50)

    def get_addr_from_guid(self, guid):
        next_obj = self.read_wow_mem(self.ObjManager + self.FirstObjOffset)
        obj_type = self.read_wow_mem(next_obj + self.GameObjTypeOffset)

        while (obj_type <= 7 and obj_type > 0):
            obj_guid = self.read_wow_mem(self.next_obj + self.GameObjGUIDOffset)
            if obj_guid == guid:
                return next_object
            else:
                next_obj = self.read_wow_mem(self.ObjManager + self.FirstObjOffset)
                obj_type = self.read_wow_mem(next_obj + self.GameObjTypeOffset)
        return 0;

    def get_wow_pid():
        hwnd = win32ui.FindWindow(None, "World of Warcraft").GetSafeHwnd()
        return win32process.GetWindowThreadProcessId(HWND)[1]

    def load_addresses(self, pid):
        self.ClientConnection = BlackMagic.ReadUInt(self.StaticClientConnection)
        self.FirstObj = BlackMagic.ReadUInt(self.ClientConnection + self.FirstObjOffset)

        LocalPlayer.Guid = BlackMagic.ReadUInt64(self.BaseAddress + StaticPointers.LocalPlayerGUID)
        LocalTarget.Guid = BlackMagic.ReadUInt64(self.BaseAddress + StaticPointers.LocalTargetGUID)

        if LocalPlayer.Guid == 0:
            return True
        else:
            return False


    def inject_process(self, force_refresh=False):
        if self.Process is None or force_refresh:
            self.Process = win32api.OpenProcess(PROCESS_ALL_ACCESS, 0, pid)
        return self.Process

    def read_wow_mem(self, address, length=None, use_ctypes=False):
        if use_ctypes:
            pass
        else:
            rPM = ctypes.WinDLL('kernel32', use_last_error=True).ReadProcessMemory
            rPM.argtypes = [wintypes.HANDLE, wintypes.LPCVOID, wintypes.LPVOID,
                            ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
            rPM.restype = wintypes.BOOL

        _buffer = ctypes.create_string_buffer(64)
        if length is None:
            length = ctypes.c_size_t()

        return c_uint(rPM(self.Process, address, _buffer, 64, ctypes.byref(length)))

    def write_wow_mem(self, address, length=None)
        wPM = ctypes.WinDLL('kernel32', use_last_error=True).WriteProcessMemory
        wPM.argtypes = [wintypes.HANDLE, wintypes.LPCVOID, wintypes.LPVOID,
                        ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
        wPM.restype = wintypes.BOOL

        _buffer = ctypes.create_string_buffer(64)
        if length is None:
            length = ctypes.c_size_t()

        wPM(self.Process, address, _buffer, 64, ctypes.byref(length))
