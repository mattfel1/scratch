#!/usr/bin/env python
import pyrogue as pr

class AccelTop(pr.Device):
    def __init__(   self,
            name        = 'AccelTop',
            description = 'Spatial Top Module SW',
            **kwargs):
        super().__init__(name=name, description=description, **kwargs)
        self.add(pr.RemoteVariable(
            name         = 'Enable',
            description  = 'Enable signal for App',
            offset       =  0x000,
            bitSize      =  1,
            bitOffset    =  0,
            mode         = 'RW',
        ))
        self.add(pr.RemoteVariable(
            name         = 'Reset',
            description  = 'Reset signal for App',
            offset       =  0x000,
            bitSize      =  1,
            bitOffset    =  1,
            mode         = 'RW',
        ))

        self.add(pr.RemoteVariable(
            name         = 'Done',
            description  = 'App Done',
            offset       =  0x004,
            bitSize      =  32,
            bitOffset    =  0,
            mode         = 'RO',
        ))


##### ArgIns
        self.add(pr.RemoteVariable(name = 'X_arg', description = 'argIn', offset = 8, bitSize = 32, bitOffset = 0, mode = 'RW',))

##### DRAM Ptrs:

##### ArgIOs

##### ArgOuts
        self.add(pr.RemoteVariable(name = 'Y_arg', description = 'argIn', offset = 12, bitSize = 32, bitOffset = 0, mode = 'RO',))

##### Instrumentation Counters
        self.add(pr.RemoteVariable(name = 'X17_cycles_arg', description = 'cycs', offset = 16, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X17_iters_arg', description = 'numiters', offset = 20, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X53_cycles_arg', description = 'cycs', offset = 16, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X53_iters_arg', description = 'numiters', offset = 20, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X57_cycles_arg', description = 'cycs', offset = 16, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X57_iters_arg', description = 'numiters', offset = 20, bitSize = 32, bitOffset = 0, mode = 'RO',))

##### Early Exits
