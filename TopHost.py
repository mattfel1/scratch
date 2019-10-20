#!/usr/bin/env python3
import setupLibPaths

import sys
import argparse
import rogue
import rogue.hardware.axi
import rogue.interfaces.stream
import rogue.interfaces.memory

import pyrogue as pr
import pyrogue.gui
import pyrogue.utilities.prbs
import pyrogue.interfaces.simulation

import axipcie  as pcie
# import rogue.axi as axi

import time
import math
import random
import struct
import numpy as np

def execute(base, cliargs):
  accel = base.Fpga.SpatialBox
  accel.Reset.set(1)
  accel.Enable.set(0)
  time.sleep(0.01)
  accel.Reset.set(0)
  print("Starting TopHost.py...")
  x81 = base.frameIn
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for FrameStoreTest!") 
  instrumentation = open('./instrumentation.txt','w+')
  # Need to instrument List((x20,1), (x100,2), (x115,2), (x114,3))
  print('ArgIns: %d, ArgIOs: %d' % (1,2)) #( " " ,  " " ))
   # immediate parent hashmap now Map(1 -> x20), current node x20 is at depth 1
  x20_cycles = accel.X20_cycles_arg.get()
  time.sleep(0.0001)
  x20_iters = accel.X20_iters_arg.get()
  time.sleep(0.0001)
  x20_iters_per_parent = x20_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x20_avg = x20_cycles / max(1,x20_iters)
  time.sleep(0.0001)
  print('  x20 - %d ( %d / %d ) [%d iters/parent execution]' % (x20_avg,x20_cycles,x20_iters,x20_iters_per_parent), end='')
  #instrumentation.write('  x20 - %d ( %d / %d ) [%d iters/parent execution]' % (x20_avg,x20_cycles,x20_iters,x20_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x100, 1 -> x20), current node x100 is at depth 2
  x100_cycles = accel.X100_cycles_arg.get()
  time.sleep(0.0001)
  x100_iters = accel.X100_iters_arg.get()
  time.sleep(0.0001)
  x100_iters_per_parent = x100_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x100_avg = x100_cycles / max(1,x100_iters)
  time.sleep(0.0001)
  print('    x100 - %d ( %d / %d ) [%d iters/parent execution]' % (x100_avg,x100_cycles,x100_iters,x100_iters_per_parent), end='')
  #instrumentation.write('    x100 - %d ( %d / %d ) [%d iters/parent execution]' % (x100_avg,x100_cycles,x100_iters,x100_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x115, 1 -> x20), current node x115 is at depth 2
  x115_cycles = accel.X115_cycles_arg.get()
  time.sleep(0.0001)
  x115_iters = accel.X115_iters_arg.get()
  time.sleep(0.0001)
  x115_iters_per_parent = x115_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x115_avg = x115_cycles / max(1,x115_iters)
  time.sleep(0.0001)
  print('    x115 - %d ( %d / %d ) [%d iters/parent execution]' % (x115_avg,x115_cycles,x115_iters,x115_iters_per_parent), end='')
  #instrumentation.write('    x115 - %d ( %d / %d ) [%d iters/parent execution]' % (x115_avg,x115_cycles,x115_iters,x115_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x115, 1 -> x20, 3 -> x114), current node x114 is at depth 3
  x114_cycles = accel.X114_cycles_arg.get()
  time.sleep(0.0001)
  x114_iters = accel.X114_iters_arg.get()
  time.sleep(0.0001)
  x114_iters_per_parent = x114_iters / max(1,x115_iters)
  time.sleep(0.0001)
  x114_avg = x114_cycles / max(1,x114_iters)
  time.sleep(0.0001)
  print('      x114 - %d ( %d / %d ) [%d iters/parent execution]' % (x114_avg,x114_cycles,x114_iters,x114_iters_per_parent), end='')
  #instrumentation.write('      x114 - %d ( %d / %d ) [%d iters/parent execution]' % (x114_avg,x114_cycles,x114_iters,x114_iters_per_parent), end='')
  x114_stalled = accel.X114_stalled_arg.get()
  x114_idle = accel.X114_idle_arg.get()
  print(' <# stalled: %d, #idle: %d>' % (x114_stalled,x114_idle), end='')
  #instrumentation.write(' <# stalled: %d, #idle: %d>' % (x114_stalled,x114_idle), end='')
  print('')
  instrumentation.write('')
  instrumentation.close();
  x116 = np.zeros(8, dtype='uint64')
  x117 = base.frameOut.getFrame()
  x118 = np.array([50462976,117835012,185207048,252579084,319951120,387323156,454695192,522067228], dtype='uint64')
  x119 = (str("Wanted:") + str("\n"));
  print(x119)
  x121 = len(x118)
  for b27 in range(0,x121,1):
    x122 = x118[b27]
    x123 = str(x122)
    x124 = (x123 + str(" "));
    print(x124)
  
  print(str("\n"))
  x128 = (str("Got:") + str("\n"));
  print(x128)
  x130 = len(x116)
  for b37 in range(0,x130,1):
    x131 = x116[b37]
    x132 = str(x131)
    x133 = (x132 + str(" "));
    print(x133)
  
  print(str("\n"))
  x140 = np.zeros(len(x116), dtype=bool)
  for b44 in range(len(x116)):
    x137 = x116[b44]
    x138 = x118[b44]
    x139 = x137 == x138;
    x140[b44] = x139
  
  x142 = np.zeros(len(x140),dtype='bool')
  for b49 in range(0,len(x140)):
    x141 = x140[b49]
    x142[b49] = x141
  
  x145 = 0
  if (len(x142) > 0): # Hack to handle reductions on things of length 0
    x145 = x142[0]
  else:
    x145 = 0
  
  for b52 in range(1,len(x142)):
    b53 = x142[b52]
    b54 = x145;
    x144 = b53 & b54;
    x145 = x144;
  
  x146 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:43:11: Assertion failure") + "\n=================\n"));
  if (True): assert(x145), "%s" % x146

