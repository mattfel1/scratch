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
  x61 = np.zeros(64, dtype='uint32')
  for b3 in range(0,64):
    x60 = b3;
    x61[b3] = x60
  
  base.x59_frame.sendFrame(x61.astype(dtype='uint64'))
