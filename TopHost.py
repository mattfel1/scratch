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
  x77 = base.frameIn
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
  # Need to instrument List((x20,1), (x96,2), (x107,2), (x106,3))
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
   # immediate parent hashmap now Map(2 -> x96, 1 -> x20), current node x96 is at depth 2
  x96_cycles = accel.X96_cycles_arg.get()
  time.sleep(0.0001)
  x96_iters = accel.X96_iters_arg.get()
  time.sleep(0.0001)
  x96_iters_per_parent = x96_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x96_avg = x96_cycles / max(1,x96_iters)
  time.sleep(0.0001)
  print('    x96 - %d ( %d / %d ) [%d iters/parent execution]' % (x96_avg,x96_cycles,x96_iters,x96_iters_per_parent), end='')
  #instrumentation.write('    x96 - %d ( %d / %d ) [%d iters/parent execution]' % (x96_avg,x96_cycles,x96_iters,x96_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x107, 1 -> x20), current node x107 is at depth 2
  x107_cycles = accel.X107_cycles_arg.get()
  time.sleep(0.0001)
  x107_iters = accel.X107_iters_arg.get()
  time.sleep(0.0001)
  x107_iters_per_parent = x107_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x107_avg = x107_cycles / max(1,x107_iters)
  time.sleep(0.0001)
  print('    x107 - %d ( %d / %d ) [%d iters/parent execution]' % (x107_avg,x107_cycles,x107_iters,x107_iters_per_parent), end='')
  #instrumentation.write('    x107 - %d ( %d / %d ) [%d iters/parent execution]' % (x107_avg,x107_cycles,x107_iters,x107_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x107, 1 -> x20, 3 -> x106), current node x106 is at depth 3
  x106_cycles = accel.X106_cycles_arg.get()
  time.sleep(0.0001)
  x106_iters = accel.X106_iters_arg.get()
  time.sleep(0.0001)
  x106_iters_per_parent = x106_iters / max(1,x107_iters)
  time.sleep(0.0001)
  x106_avg = x106_cycles / max(1,x106_iters)
  time.sleep(0.0001)
  print('      x106 - %d ( %d / %d ) [%d iters/parent execution]' % (x106_avg,x106_cycles,x106_iters,x106_iters_per_parent), end='')
  #instrumentation.write('      x106 - %d ( %d / %d ) [%d iters/parent execution]' % (x106_avg,x106_cycles,x106_iters,x106_iters_per_parent), end='')
  x106_stalled = accel.X106_stalled_arg.get()
  x106_idle = accel.X106_idle_arg.get()
  print(' <# stalled: %d, #idle: %d>' % (x106_stalled,x106_idle), end='')
  #instrumentation.write(' <# stalled: %d, #idle: %d>' % (x106_stalled,x106_idle), end='')
  print('')
  instrumentation.write('')
  instrumentation.close();
  x108 = np.zeros(8, dtype='uint64')
  # x109 in get x77 to x108
  x110 = np.array([50462976,117835012,185207048,252579084,319951120,387323156,454695192,522067228], dtype='uint64')
  x111 = (str("Wanted:") + str("\n"));
  print(x111)
  x113 = len(x110)
  for b27 in range(0,x113,1):
    x114 = x110[b27]
    x115 = str(x114)
    x116 = (x115 + str(" "));
    print(x116)
  
  print(str("\n"))
  x120 = (str("Got:") + str("\n"));
  print(x120)
  x122 = len(x108)
  for b37 in range(0,x122,1):
    x123 = x108[b37]
    x124 = str(x123)
    x125 = (x124 + str(" "));
    print(x125)
  
  print(str("\n"))
  x132 = np.zeros(len(x108), dtype=bool)
  for b44 in range(len(x108)):
    x129 = x108[b44]
    x130 = x110[b44]
    x131 = x129 == x130;
    x132[b44] = x131
  
  x134 = np.zeros(len(x132),dtype='bool')
  for b49 in range(0,len(x132)):
    x133 = x132[b49]
    x134[b49] = x133
  
  x137 = 0
  if (len(x134) > 0): # Hack to handle reductions on things of length 0
    x137 = x134[0]
  else:
    x137 = 0
  
  for b52 in range(1,len(x134)):
    b53 = x134[b52]
    b54 = x137;
    x136 = b53 & b54;
    x137 = x136;
  
  x138 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:43:11: Assertion failure") + "\n=================\n"));
  if (True): assert(x137), "%s" % x138

