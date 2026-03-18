from .utils import packBytes


class ShellCode:
    def WarpShellcode(BaseB, HomewardCall):
        shellcode = bytearray(b"\x48\xb9" + packBytes(BaseB))  # movabs rcx, [BaseB]
        shellcode.extend(b"\xba\x01\x00\x00\x00")  # mov edx, 1
        shellcode.extend(b"\x48\x83\xec\x38")  # sub rsp, 38
        shellcode.extend(
            b"\xff\x15\x02\x00\x00\x00\xeb\x08" + packBytes(HomewardCall)
        )  # call HomewardCall
        shellcode.extend(b"\x48\x83\xc4\x38")  # add rsp, 38
        shellcode.extend(b"\xc3")  # ret
        return shellcode
