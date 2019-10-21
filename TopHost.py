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
  x87 = base.frameIn
  x89 = np.zeros(64, dtype='uint32')
  for b3 in range(0,64):
    x88 = b3;
    x89[b3] = x88
  
  base.frameIn.sendFrame(x89)
  x92 = base.frameOut
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for FrameLoadStoreTest!") 
  instrumentation = open('./instrumentation.txt','w+')
  # Need to instrument List((x17,1), (x126,2), (x102,3), (x101,4), (x110,3), (x125,3), (x124,4))
  print('ArgIns: %d, ArgIOs: %d' % (1,2)) #( " " ,  " " ))
   # immediate parent hashmap now Map(1 -> x17), current node x17 is at depth 1
  x17_cycles = accel.X17_cycles_arg.get()
  time.sleep(0.0001)
  x17_iters = accel.X17_iters_arg.get()
  time.sleep(0.0001)
  x17_iters_per_parent = x17_iters / max(1,x17_iters)
  time.sleep(0.0001)
  x17_avg = x17_cycles / max(1,x17_iters)
  time.sleep(0.0001)
  print('  x17 - %d ( %d / %d ) [%d iters/parent execution]' % (x17_avg,x17_cycles,x17_iters,x17_iters_per_parent), end='')
  #instrumentation.write('  x17 - %d ( %d / %d ) [%d iters/parent execution]' % (x17_avg,x17_cycles,x17_iters,x17_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x126, 1 -> x17), current node x126 is at depth 2
  x126_cycles = accel.X126_cycles_arg.get()
  time.sleep(0.0001)
  x126_iters = accel.X126_iters_arg.get()
  time.sleep(0.0001)
  x126_iters_per_parent = x126_iters / max(1,x17_iters)
  time.sleep(0.0001)
  x126_avg = x126_cycles / max(1,x126_iters)
  time.sleep(0.0001)
  print('    x126 - %d ( %d / %d ) [%d iters/parent execution]' % (x126_avg,x126_cycles,x126_iters,x126_iters_per_parent), end='')
  #instrumentation.write('    x126 - %d ( %d / %d ) [%d iters/parent execution]' % (x126_avg,x126_cycles,x126_iters,x126_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x126, 1 -> x17, 3 -> x102), current node x102 is at depth 3
  x102_cycles = accel.X102_cycles_arg.get()
  time.sleep(0.0001)
  x102_iters = accel.X102_iters_arg.get()
  time.sleep(0.0001)
  x102_iters_per_parent = x102_iters / max(1,x126_iters)
  time.sleep(0.0001)
  x102_avg = x102_cycles / max(1,x102_iters)
  time.sleep(0.0001)
  print('      x102 - %d ( %d / %d ) [%d iters/parent execution]' % (x102_avg,x102_cycles,x102_iters,x102_iters_per_parent), end='')
  #instrumentation.write('      x102 - %d ( %d / %d ) [%d iters/parent execution]' % (x102_avg,x102_cycles,x102_iters,x102_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x126, 4 -> x101, 1 -> x17, 3 -> x102), current node x101 is at depth 4
  x101_cycles = accel.X101_cycles_arg.get()
  time.sleep(0.0001)
  x101_iters = accel.X101_iters_arg.get()
  time.sleep(0.0001)
  x101_iters_per_parent = x101_iters / max(1,x102_iters)
  time.sleep(0.0001)
  x101_avg = x101_cycles / max(1,x101_iters)
  time.sleep(0.0001)
  print('        x101 - %d ( %d / %d ) [%d iters/parent execution]' % (x101_avg,x101_cycles,x101_iters,x101_iters_per_parent), end='')
  #instrumentation.write('        x101 - %d ( %d / %d ) [%d iters/parent execution]' % (x101_avg,x101_cycles,x101_iters,x101_iters_per_parent), end='')
  x101_stalled = accel.X101_stalled_arg.get()
  x101_idle = accel.X101_idle_arg.get()
  print(' <# stalled: %d, #idle: %d>' % (x101_stalled,x101_idle), end='')
  #instrumentation.write(' <# stalled: %d, #idle: %d>' % (x101_stalled,x101_idle), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x126, 4 -> x101, 1 -> x17, 3 -> x110), current node x110 is at depth 3
  x110_cycles = accel.X110_cycles_arg.get()
  time.sleep(0.0001)
  x110_iters = accel.X110_iters_arg.get()
  time.sleep(0.0001)
  x110_iters_per_parent = x110_iters / max(1,x126_iters)
  time.sleep(0.0001)
  x110_avg = x110_cycles / max(1,x110_iters)
  time.sleep(0.0001)
  print('      x110 - %d ( %d / %d ) [%d iters/parent execution]' % (x110_avg,x110_cycles,x110_iters,x110_iters_per_parent), end='')
  #instrumentation.write('      x110 - %d ( %d / %d ) [%d iters/parent execution]' % (x110_avg,x110_cycles,x110_iters,x110_iters_per_parent), end='')
  x110_stalled = accel.X110_stalled_arg.get()
  x110_idle = accel.X110_idle_arg.get()
  print(' <# stalled: %d, #idle: %d>' % (x110_stalled,x110_idle), end='')
  #instrumentation.write(' <# stalled: %d, #idle: %d>' % (x110_stalled,x110_idle), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x126, 4 -> x101, 1 -> x17, 3 -> x125), current node x125 is at depth 3
  x125_cycles = accel.X125_cycles_arg.get()
  time.sleep(0.0001)
  x125_iters = accel.X125_iters_arg.get()
  time.sleep(0.0001)
  x125_iters_per_parent = x125_iters / max(1,x126_iters)
  time.sleep(0.0001)
  x125_avg = x125_cycles / max(1,x125_iters)
  time.sleep(0.0001)
  print('      x125 - %d ( %d / %d ) [%d iters/parent execution]' % (x125_avg,x125_cycles,x125_iters,x125_iters_per_parent), end='')
  #instrumentation.write('      x125 - %d ( %d / %d ) [%d iters/parent execution]' % (x125_avg,x125_cycles,x125_iters,x125_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x126, 4 -> x124, 1 -> x17, 3 -> x125), current node x124 is at depth 4
  x124_cycles = accel.X124_cycles_arg.get()
  time.sleep(0.0001)
  x124_iters = accel.X124_iters_arg.get()
  time.sleep(0.0001)
  x124_iters_per_parent = x124_iters / max(1,x125_iters)
  time.sleep(0.0001)
  x124_avg = x124_cycles / max(1,x124_iters)
  time.sleep(0.0001)
  print('        x124 - %d ( %d / %d ) [%d iters/parent execution]' % (x124_avg,x124_cycles,x124_iters,x124_iters_per_parent), end='')
  #instrumentation.write('        x124 - %d ( %d / %d ) [%d iters/parent execution]' % (x124_avg,x124_cycles,x124_iters,x124_iters_per_parent), end='')
  x124_stalled = accel.X124_stalled_arg.get()
  x124_idle = accel.X124_idle_arg.get()
  print(' <# stalled: %d, #idle: %d>' % (x124_stalled,x124_idle), end='')
  #instrumentation.write(' <# stalled: %d, #idle: %d>' % (x124_stalled,x124_idle), end='')
  print('')
  instrumentation.write('')
  instrumentation.close();
  x127 = np.zeros(64, dtype='uint32')
  x128 = base.frameOut.getFrame()
  x127 = np.frombuffer(x128, dtype='uint32')
  x129 = (str("Wanted:") + str("\n"));
  print(x129)
  x131 = len(x89)
  for b23 in range(0,x131,1):
    x132 = x89[b23]
    x133 = str(x132)
    x134 = (x133 + str(" "));
    print(x134)
  
  print(str("\n"))
  x138 = (str("Got:") + str("\n"));
  print(x138)
  x140 = len(x127)
  for b33 in range(0,x140,1):
    x141 = x127[b33]
    x142 = str(x141)
    x143 = (x142 + str(" "));
    print(x143)
  
  print(str("\n"))
  x150 = np.zeros(len(x127), dtype=bool)
  for b40 in range(len(x127)):
    x147 = x127[b40]
    x148 = x89[b40]
    x149 = x147 == x148;
    x150[b40] = x149
  
  x152 = np.zeros(len(x150),dtype='bool')
  for b45 in range(0,len(x150)):
    x151 = x150[b45]
    x152[b45] = x151
  
  x155 = 0
  if (len(x152) > 0): # Hack to handle reductions on things of length 0
    x155 = x152[0]
  else:
    x155 = 0
  
  for b48 in range(1,len(x152)):
    b49 = x152[b48]
    b50 = x155;
    x154 = b49 & b50;
    x155 = x154;
  
  x156 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:80:11: Assertion failure") + "\n=================\n"));
  if (True): assert(x155), "%s" % x156

