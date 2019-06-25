package accel
import fringe._
import fringe.templates.memory._
import fringe.templates._
import fringe.Ledger._
import fringe.utils._
import fringe.utils.implicits._
import fringe.templates.math._
import fringe.templates.counters._
import fringe.templates.vector._
import fringe.SpatialBlocks._
import fringe.templates.memory._
import fringe.templates.memory.implicits._
import fringe.templates.retiming._
import emul.ResidualGenerator._
import api._
import chisel3._
import chisel3.util._
import Args._
import scala.collection.immutable._

object Instrument {
  def connect(top: AccelTop, instrctrs: List[InstrCtr]): Unit = {
    top.io.argOuts(api.ROOTCONTROLLER_cycles_arg).port.bits := instrctrs(ROOTCONTROLLER_instrctr).cycs
    top.io.argOuts(api.ROOTCONTROLLER_cycles_arg).port.valid := top.io.enable
    top.io.argOuts(api.ROOTCONTROLLER_iters_arg).port.bits := instrctrs(ROOTCONTROLLER_instrctr).iters
    top.io.argOuts(api.ROOTCONTROLLER_iters_arg).port.valid := top.io.enable
    val numArgOuts_breakpts = 0
  }
}
