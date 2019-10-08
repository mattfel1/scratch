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

def execute(base, cliargs):
  accel = base.Fpga.SpatialBox
  accel.Reset.set(1)
  accel.Enable.set(0)
  time.sleep(0.01)
  accel.Reset.set(0)
  print("Starting TopHost.py...")
  x34 = cliargs;
  x35 = 0;
  x37 = x34[0]
  x38 = int(x37)
  accel.X_arg.set(x38)
  print("Wrote %d to x35!" % x38)
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
  x43 = accel.Y_arg.get()
  time.sleep(0.001)
  x44 = x38 + 4;
  x45 = str(x44)
  x46 = (str("expected: ") + x45);
  x47 = (x46 + str("\n"));
  print(x47)
  x49 = str(x43)
  x50 = (str("result: ") + x49);
  x51 = (x50 + str("\n"));
  print(x51)
  x53 = x44 == x43;
  x54 = str(x53)
  x55 = (str("PASS: ") + x54);
  x56 = (x55 + str(" (InOutArg)"));
  x57 = (x56 + str("\n"));
  print(x57)
  x59 = ("\n=================\n" + (str("ArgInOut.scala:30:11: Assertion failure") + "\n=================\n"));
  if (true): assert(x53), "%s" % x59

