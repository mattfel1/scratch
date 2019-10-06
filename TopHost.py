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
import surf.axi as axi

import time
import math
import random
import struct
import numpy as np

def execute(accel, cliargs):
  accel.Reset.set(1)
  accel.Enable.set(0)
  time.sleep(0.01)
  accel.Reset.set(0)
  print("Starting TopHost.py...")
  x133 = cliargs;
  x134 = x133[1]
  x135 = int(x134)
  x136 = x133[0]
  x137 = int(x136)
  * x138 = new (x135);
  for b5 in range(0,x135):
    x138[b5] = b5
  
  x139 = 0;
  accel.SIZE_arg.set(x135)
  print("Wrote %d to x139!" % x135)
  time.sleep(0.001)
  x141 = x139;
  x142 = self._reqFrame(x141, True)
  set this SRCFPGA_ptr
  c1->setArg(SRCFPGA_ptr, x142, false);
  print("Allocate mem of size x141 at %p\n" % x142_ptr);
  x143 = x139;
  x144 = self._reqFrame(x143, True)
  set this DSTFPGA_ptr
  c1->setArg(DSTFPGA_ptr, x144, false);
  print("Allocate mem of size x143 at %p\n" % x144_ptr);
  x146 = 0;
  accel.X_arg.set(x137)
  print("Wrote %d to x146!" % x137)
  time.sleep(0.001)
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 500 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py!")
  x219 = [None for _ in range(x143)]
  x223 = [None for _ in range((*x138).size())]
  for b42 in range(0,(*x138).size()):
    x221 = x138[b42]
    x222 = x221 * x137;
    x223[b42] = x222
  
  print(str("Sent in: \n"))
  for b47 in range(0,x135,1):
    x225 = x223[b47]
    x226 = str(x225)
    x227 = (x226 + str(" "));
    print(x227)
  
  print(str("Got out: \n"))
  for b54 in range(0,x135,1):
    x231 = x219[b54]
    x232 = str(x231)
    x233 = (x232 + str(" "));
    print(x233)
  
  print(str("\n"))
  * x240 = new ((*x219).size());
  for (int b61 = 0; b61 < (*x219).size(); b61++) { 
    x237 = x219[b61]
    x238 = x223[b61]
    x239 = x237 == x238;
    (*x240)[b61] = x239;
  }
   x243;
  if ((*x240).size() > 0) { // Hack to handle reductions on things of length 0
    x243 = (*x240)[0];
  }
  else {
    x243 = 0;
  }
  for (int b66 = 1; b66 < (*x240).size(); b66++) {
     b67 = (*x240)[b66];
     b68 = x243;
    x242 = b67 & b68;
    x243 = x242;
  }
  x244 = str(x243)
  x245 = (str("PASS: ") + x244);
  x246 = (x245 + str(" (SimpleTileLoadStore)"));
  x247 = (x246 + str("\n"));
  print(x247)
  x249 = ("\n=================\n" + (str("TileLoadStoreSimple.scala:61:11: Assertion failure") + "\n=================\n"));
  if (true): assert(x243), "%s" % x249

