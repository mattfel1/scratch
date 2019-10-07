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

##### DRAM Ptrs:
        self.add(pr.RemoteVariable(name = 'IN_ptr', description = 'dram ptr', offset = 8, bitSize = 32, bitOffset = 0, mode = 'RW',))

##### ArgIOs

##### ArgOuts
        self.add(pr.RemoteVariable(name = 'X255_arg', description = 'argIn', offset = 12, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X256_arg', description = 'argIn', offset = 16, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X257_arg', description = 'argIn', offset = 20, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X258_arg', description = 'argIn', offset = 24, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X259_arg', description = 'argIn', offset = 28, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X260_arg', description = 'argIn', offset = 32, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X261_arg', description = 'argIn', offset = 36, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X262_arg', description = 'argIn', offset = 40, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X263_arg', description = 'argIn', offset = 44, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X264_arg', description = 'argIn', offset = 48, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X265_arg', description = 'argIn', offset = 52, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X266_arg', description = 'argIn', offset = 56, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X267_arg', description = 'argIn', offset = 60, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X268_arg', description = 'argIn', offset = 64, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X269_arg', description = 'argIn', offset = 68, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X270_arg', description = 'argIn', offset = 72, bitSize = 32, bitOffset = 0, mode = 'RO',))

##### Instrumentation Counters

##### Early Exits
