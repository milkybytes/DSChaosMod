from ChaosHandler.Effect import BaseEffect
from pymem import memory

from ..Memory import BaseAddress, packBytes


class WarpToBonfire(BaseEffect):
    name = "Warp to Bonfire"

    @classmethod
    async def start(cls, pm, module):
        BaseB = BaseAddress.BaseB(pm, module)
        HomewardCall = BaseAddress.HomewardCall(pm, module)

        shellcode = bytearray(b"\x48\xB9" + packBytes(BaseB))  # movabs rcx, [BaseB]
        shellcode.extend(b"\xBA\x01\x00\x00\x00")  # mov edx, 1
        shellcode.extend(b"\x48\x83\xEC\x38")  # sub rsp, 38
        shellcode.extend(
            b"\xFF\x15\x02\x00\x00\x00\xEB\x08" + packBytes(HomewardCall)
        )  # call HomewardCall
        shellcode.extend(b"\x48\x83\xC4\x38")  # add rsp, 38
        shellcode.extend(b"\xC3")  # ret

        BonFireTP = pm.allocate(128)
        memory.write_bytes(
            pm.process_handle, BonFireTP, bytes(shellcode), len(shellcode)
        )
        pm.start_thread(BonFireTP)
        pm.free(BonFireTP)
