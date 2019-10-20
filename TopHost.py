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
  x80 = base.frameIn
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
  # Need to instrument List((x20,1), (x99,2), (x113,2), (x112,3))
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
   # immediate parent hashmap now Map(2 -> x99, 1 -> x20), current node x99 is at depth 2
  x99_cycles = accel.X99_cycles_arg.get()
  time.sleep(0.0001)
  x99_iters = accel.X99_iters_arg.get()
  time.sleep(0.0001)
  x99_iters_per_parent = x99_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x99_avg = x99_cycles / max(1,x99_iters)
  time.sleep(0.0001)
  print('    x99 - %d ( %d / %d ) [%d iters/parent execution]' % (x99_avg,x99_cycles,x99_iters,x99_iters_per_parent), end='')
  #instrumentation.write('    x99 - %d ( %d / %d ) [%d iters/parent execution]' % (x99_avg,x99_cycles,x99_iters,x99_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x113, 1 -> x20), current node x113 is at depth 2
  x113_cycles = accel.X113_cycles_arg.get()
  time.sleep(0.0001)
  x113_iters = accel.X113_iters_arg.get()
  time.sleep(0.0001)
  x113_iters_per_parent = x113_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x113_avg = x113_cycles / max(1,x113_iters)
  time.sleep(0.0001)
  print('    x113 - %d ( %d / %d ) [%d iters/parent execution]' % (x113_avg,x113_cycles,x113_iters,x113_iters_per_parent), end='')
  #instrumentation.write('    x113 - %d ( %d / %d ) [%d iters/parent execution]' % (x113_avg,x113_cycles,x113_iters,x113_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x113, 1 -> x20, 3 -> x112), current node x112 is at depth 3
  x112_cycles = accel.X112_cycles_arg.get()
  time.sleep(0.0001)
  x112_iters = accel.X112_iters_arg.get()
  time.sleep(0.0001)
  x112_iters_per_parent = x112_iters / max(1,x113_iters)
  time.sleep(0.0001)
  x112_avg = x112_cycles / max(1,x112_iters)
  time.sleep(0.0001)
  print('      x112 - %d ( %d / %d ) [%d iters/parent execution]' % (x112_avg,x112_cycles,x112_iters,x112_iters_per_parent), end='')
  #instrumentation.write('      x112 - %d ( %d / %d ) [%d iters/parent execution]' % (x112_avg,x112_cycles,x112_iters,x112_iters_per_parent), end='')
  x112_stalled = accel.X112_stalled_arg.get()
  x112_idle = accel.X112_idle_arg.get()
  print(' <# stalled: %d, #idle: %d>' % (x112_stalled,x112_idle), end='')
  #instrumentation.write(' <# stalled: %d, #idle: %d>' % (x112_stalled,x112_idle), end='')
  print('')
  instrumentation.write('')
  instrumentation.close();
  x114 = np.zeros(8, dtype='uint64')
  x115 = base.frameOut.getFrame()
  x116 = np.array([50462976,117835012,185207048,252579084,319951120,387323156,454695192,522067228], dtype='uint64')
  x117 = (str("Wanted:") + str("\n"));
  print(x117)
  x119 = len(x116)
  for b27 in range(0,x119,1):
    x120 = x116[b27]
    x121 = str(x120)
    x122 = (x121 + str(" "));
    print(x122)
  
  print(str("\n"))
  x126 = (str("Got:") + str("\n"));
  print(x126)
  x128 = len(x114)
  for b37 in range(0,x128,1):
    x129 = x114[b37]
    x130 = str(x129)
    x131 = (x130 + str(" "));
    print(x131)
  
  print(str("\n"))
  x138 = np.zeros(len(x114), dtype=bool)
  for b44 in range(len(x114)):
    x135 = x114[b44]
    x136 = x116[b44]
    x137 = x135 == x136;
    x138[b44] = x137
  
  x140 = np.zeros(len(x138),dtype='bool')
  for b49 in range(0,len(x138)):
    x139 = x138[b49]
    x140[b49] = x139
  
  x143 = 0
  if (len(x140) > 0): # Hack to handle reductions on things of length 0
    x143 = x140[0]
  else:
    x143 = 0
  
  for b52 in range(1,len(x140)):
    b53 = x140[b52]
    b54 = x143;
    x142 = b53 & b54;
    x143 = x142;
  
  x144 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:43:11: Assertion failure") + "\n=================\n"));
  if (True): assert(x143), "%s" % x144

