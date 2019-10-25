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
from FrameContainer import FrameContainer

def connect(base):
  base.x91_frame = FrameContainer()
  pyrogue.streamConnect(base.x91_frame, base.x90_port)
  base.x96_frame = FrameContainer()
  pyrogue.streamConnect(base.x96_frame, base.x95_port)

