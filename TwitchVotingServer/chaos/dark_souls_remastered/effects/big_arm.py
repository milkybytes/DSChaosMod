from chaos.dark_souls_remastered.dsr_effect import DSREffect
from chaos.dark_souls_remastered.memory import BaseAddress, Pointer
from pymem import memory


class BigArm(DSREffect):
    name = "Big Arm Mode"
    config_alias = "big_arm"
    print("in the big arm class")
    async def _set_arm_size(self, size):
        BaseB = BaseAddress.BaseB(self.pm, self.module)
        arm_pointer = Pointer.Player.Arm.arm_size(self.pm, BaseB)
        memory.write_float(self.pm.process_handle, arm_pointer, size)
        print("setting arm size")
    async def _on_start(self):
        await self._set_arm_size(20)
        await self.tick(self.seconds)

    async def _on_stop(self):
        await self._set_arm_size(0)


