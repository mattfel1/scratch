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
  x83 = base.frameIn
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
  # Need to instrument List((x20,1), (x102,2), (x119,2), (x118,3))
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
   # immediate parent hashmap now Map(2 -> x102, 1 -> x20), current node x102 is at depth 2
  x102_cycles = accel.X102_cycles_arg.get()
  time.sleep(0.0001)
  x102_iters = accel.X102_iters_arg.get()
  time.sleep(0.0001)
  x102_iters_per_parent = x102_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x102_avg = x102_cycles / max(1,x102_iters)
  time.sleep(0.0001)
  print('    x102 - %d ( %d / %d ) [%d iters/parent execution]' % (x102_avg,x102_cycles,x102_iters,x102_iters_per_parent), end='')
  #instrumentation.write('    x102 - %d ( %d / %d ) [%d iters/parent execution]' % (x102_avg,x102_cycles,x102_iters,x102_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x119, 1 -> x20), current node x119 is at depth 2
  x119_cycles = accel.X119_cycles_arg.get()
  time.sleep(0.0001)
  x119_iters = accel.X119_iters_arg.get()
  time.sleep(0.0001)
  x119_iters_per_parent = x119_iters / max(1,x20_iters)
  time.sleep(0.0001)
  x119_avg = x119_cycles / max(1,x119_iters)
  time.sleep(0.0001)
  print('    x119 - %d ( %d / %d ) [%d iters/parent execution]' % (x119_avg,x119_cycles,x119_iters,x119_iters_per_parent), end='')
  #instrumentation.write('    x119 - %d ( %d / %d ) [%d iters/parent execution]' % (x119_avg,x119_cycles,x119_iters,x119_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x119, 1 -> x20, 3 -> x118), current node x118 is at depth 3
  x118_cycles = accel.X118_cycles_arg.get()
  time.sleep(0.0001)
  x118_iters = accel.X118_iters_arg.get()
  time.sleep(0.0001)
  x118_iters_per_parent = x118_iters / max(1,x119_iters)
  time.sleep(0.0001)
  x118_avg = x118_cycles / max(1,x118_iters)
  time.sleep(0.0001)
  print('      x118 - %d ( %d / %d ) [%d iters/parent execution]' % (x118_avg,x118_cycles,x118_iters,x118_iters_per_parent), end='')
  #instrumentation.write('      x118 - %d ( %d / %d ) [%d iters/parent execution]' % (x118_avg,x118_cycles,x118_iters,x118_iters_per_parent), end='')
  x118_stalled = accel.X118_stalled_arg.get()
  x118_idle = accel.X118_idle_arg.get()
  print(' <# stalled: %d, #idle: %d>' % (x118_stalled,x118_idle), end='')
  #instrumentation.write(' <# stalled: %d, #idle: %d>' % (x118_stalled,x118_idle), end='')
  print('')
  instrumentation.write('')
  instrumentation.close();
  x120 = np.zeros(8, dtype='uint64')
  x121 = base.frameOut.getFrame()
  x122 = np.array([50462976,117835012,185207048,252579084,319951120,387323156,454695192,522067228], dtype='uint64')
  x123 = (str("Wanted:") + str("\n"));
  print(x123)
  x125 = len(x122)
  for b27 in range(0,x125,1):
    x126 = x122[b27]
    x127 = str(x126)
    x128 = (x127 + str(" "));
    print(x128)
  
  print(str("\n"))
  x132 = (str("Got:") + str("\n"));
  print(x132)
  x134 = len(x120)
  for b37 in range(0,x134,1):
    x135 = x120[b37]
    x136 = str(x135)
    x137 = (x136 + str(" "));
    print(x137)
  
  print(str("\n"))
  x144 = np.zeros(len(x120), dtype=bool)
  for b44 in range(len(x120)):
    x141 = x120[b44]
    x142 = x122[b44]
    x143 = x141 == x142;
    x144[b44] = x143
  
  x146 = np.zeros(len(x144),dtype='bool')
  for b49 in range(0,len(x144)):
    x145 = x144[b49]
    x146[b49] = x145
  
  x149 = 0
  if (len(x146) > 0): # Hack to handle reductions on things of length 0
    x149 = x146[0]
  else:
    x149 = 0
  
  for b52 in range(1,len(x146)):
    b53 = x146[b52]
    b54 = x149;
    x148 = b53 & b54;
    x149 = x148;
  
  x150 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:43:11: Assertion failure") + "\n=================\n"));
  if (True): assert(x149), "%s" % x150

