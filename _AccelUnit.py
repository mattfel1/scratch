#!/usr/bin/env python
import pyrogue as pr
import rogue.protocols
import numpy as np

class AccelUnit(pr.Device,rogue.interfaces.stream.Slave):
    def __init__(   self,
            name        = 'AccelUnit',
            description = 'Spatial Top Module SW',
            **kwargs):
        rogue.interfaces.stream.Slave.__init__(self)
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
        self.add(pr.RemoteVariable(name = 'OUT_ptr', description = 'dram ptr', offset = 12, bitSize = 32, bitOffset = 0, mode = 'RW',))

##### ArgIOs

##### ArgOuts

##### Instrumentation Counters
        self.add(pr.RemoteVariable(name = 'X17_cycles_arg', description = 'cycs', offset = 16, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X17_iters_arg', description = 'numiters', offset = 20, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X126_cycles_arg', description = 'cycs', offset = 24, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X126_iters_arg', description = 'numiters', offset = 28, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X102_cycles_arg', description = 'cycs', offset = 32, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X102_iters_arg', description = 'numiters', offset = 36, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X101_cycles_arg', description = 'cycs', offset = 40, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X101_iters_arg', description = 'numiters', offset = 44, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X101_stalled_arg', description = 'stalled', offset = 48, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X101_idle_arg', description = 'idle', offset = 52, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X110_cycles_arg', description = 'cycs', offset = 56, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X110_iters_arg', description = 'numiters', offset = 60, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X110_stalled_arg', description = 'stalled', offset = 64, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X110_idle_arg', description = 'idle', offset = 68, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X125_cycles_arg', description = 'cycs', offset = 72, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X125_iters_arg', description = 'numiters', offset = 76, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X124_cycles_arg', description = 'cycs', offset = 80, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X124_iters_arg', description = 'numiters', offset = 84, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X124_stalled_arg', description = 'stalled', offset = 88, bitSize = 32, bitOffset = 0, mode = 'RO',))
        self.add(pr.RemoteVariable(name = 'X124_idle_arg', description = 'idle', offset = 92, bitSize = 32, bitOffset = 0, mode = 'RO',))

##### Early Exits
    # Unused code for testing how to receive a frame in SW
    def _acceptFrame(self,frame):
        p = bytearray(frame.getPayload())
        frame.read(p,0)
        print(len(p))
        my_mask = np.arange(36)
        if(len(p)>100):
              my_mask = np.append(my_mask,np.arange(int(len(p)/2),int(len(p)/2)+36))
              my_mask = np.append(my_mask,np.arange(len(p)-36,len(p)))

        to_print = np.array(p)[-1:]
        #print(np.array(p)[:96],to_print) #comment out for long term test
        print(np.array(p)[my_mask])
        print('--------------------------')
