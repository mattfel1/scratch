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
from FrameSlave import FrameSlave
from FrameMaster import FrameMaster

def connect(base):
  base.x58_port = rogue.interfaces.stream.TcpClient('localhost', 8000 + (0+1)*2 + 0 * 512)
  base.x59_frame = FrameMaster()
  pyrogue.streamConnect(base.x59_frame, base.x58_port)
  base.x63_port = rogue.interfaces.stream.TcpClient('localhost', 8000 + (1+1)*2 + 0 * 512)
