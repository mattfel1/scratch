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
  x68 = np.zeros(64, dtype='uint32')
  for b3 in range(0,64):
    x67 = b3;
    x68[b3] = x67
  
  base.x66_frame.sendFrame(x68.astype(dtype='uint64'))
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for FrameEnqDeqTest!") 
  instrumentation = open('./instrumentation.txt','w+')
  # Need to instrument List((x16,1), (x80,2))
  print('ArgIns: %d, ArgIOs: %d' % (1,2)) #( " " ,  " " ))
   # immediate parent hashmap now Map(1 -> x16), current node x16 is at depth 1
  x16_cycles = accel.X16_cycles_arg.get()
  time.sleep(0.0001)
  x16_iters = accel.X16_iters_arg.get()
  time.sleep(0.0001)
  x16_iters_per_parent = x16_iters / max(1,x16_iters)
  time.sleep(0.0001)
  x16_avg = x16_cycles / max(1,x16_iters)
  time.sleep(0.0001)
  print('  x16 - %d ( %d / %d ) [%d iters/parent execution]' % (x16_avg,x16_cycles,x16_iters,x16_iters_per_parent), end='')
  #instrumentation.write('  x16 - %d ( %d / %d ) [%d iters/parent execution]' % (x16_avg,x16_cycles,x16_iters,x16_iters_per_parent), end='')
  print('')
  instrumentation.write('')
   # immediate parent hashmap now Map(2 -> x80, 1 -> x16), current node x80 is at depth 2
  x80_cycles = accel.X80_cycles_arg.get()
  time.sleep(0.0001)
  x80_iters = accel.X80_iters_arg.get()
  time.sleep(0.0001)
  x80_iters_per_parent = x80_iters / max(1,x16_iters)
  time.sleep(0.0001)
  x80_avg = x80_cycles / max(1,x80_iters)
  time.sleep(0.0001)
  print('    x80 - %d ( %d / %d ) [%d iters/parent execution]' % (x80_avg,x80_cycles,x80_iters,x80_iters_per_parent), end='')
  #instrumentation.write('    x80 - %d ( %d / %d ) [%d iters/parent execution]' % (x80_avg,x80_cycles,x80_iters,x80_iters_per_parent), end='')
  print('')
  instrumentation.write('')
  instrumentation.close();
  x81 = np.zeros(64, dtype='uint32')
  x82 = base.x71_frame.getFrame()
  x81 = np.frombuffer(x82, dtype='uint8').astype(dtype='uint32')
  x85 = np.zeros(len(x68),dtype='uint32')
  for b19 in range(0,len(x68)):
    x83 = x68[b19]
    x84 = x83 + 5;
    x85[b19] = x84
  
  x86 = (str("Wanted:") + str("\n"));
  print(x86)
  x88 = len(x85)
  for b26 in range(0,x88,1):
    x89 = x85[b26]
    x90 = str(x89)
    x91 = (x90 + str(" "));
    print(x91)
  
  print(str("\n"))
  x95 = (str("Got:") + str("\n"));
  print(x95)
  x97 = len(x81)
  for b36 in range(0,x97,1):
    x98 = x81[b36]
    x99 = str(x98)
    x100 = (x99 + str(" "));
    print(x100)
  
  print(str("\n"))
  x107 = np.zeros(len(x81), dtype=bool)
  for b43 in range(len(x81)):
    x104 = x81[b43]
    x105 = x85[b43]
    x106 = x104 == x105;
    x107[b43] = x106
  
  x109 = np.zeros(len(x107),dtype='bool')
  for b48 in range(0,len(x107)):
    x108 = x107[b48]
    x109[b48] = x108
  
  x112 = 0
  if (len(x109) > 0): # Hack to handle reductions on things of length 0
    x112 = x109[0]
  else:
    x112 = 0
  
  for b51 in range(1,len(x109)):
    b52 = x109[b51]
    b53 = x112;
    x111 = b52 & b53;
    x112 = x111;
  
  x113 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:93:11: Assertion failure") + "\n=================\n"));
  if (True): assert(x112), "%s" % x113

