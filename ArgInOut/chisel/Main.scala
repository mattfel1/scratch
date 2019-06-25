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

object Main {
  def main(top: AccelTop): Unit = {
    top.io <> DontCare
    val x32_x = top.io.argIns(api.X_arg)
    val x33_y = Wire(new MultiArgOut(1)); x33_y.port.map(_.bits := DontCare); x33_y.port.map(_.valid := DontCare); x33_y.output.echo := DontCare
    top.io.argOuts(top.io_numArgIOs_reg + 0).port.valid := x33_y.port.map(_.valid).reduce{_||_}
    top.io.argOuts(top.io_numArgIOs_reg + 0).port.bits := Mux1H(x33_y.port.map(_.valid), x33_y.port.map(_.bits))
    x33_y.port.map(_.ready := top.io.argOuts(top.io_numArgIOs_reg + 0).port.ready)
    x33_y.output.echo := top.io.argOuts(top.io_numArgIOs_reg + 0).echo
    val retime_counter = Module(new SingleCounter(1, Some(0), Some(top.max_latency), Some(1), false)); retime_counter.io <> DontCare // Counter for masking out the noise that comes out of ShiftRegister in the first few cycles of the app
    retime_counter.io.setup.saturate := true.B; retime_counter.io.input.reset := top.reset.toBool; retime_counter.io.input.enable := true.B;
    val rr = getRetimed(retime_counter.io.output.done, 1, true.B) // break up critical path by delaying this 
    val breakpoints = Wire(Vec(top.io_numArgOuts_breakpts max 1, Bool())); breakpoints.zipWithIndex.foreach{case(b,i) => b.suggestName(s"breakpoint" + i)}; breakpoints := DontCare
    val instrctrs = List.fill[InstrCtr](api.numCtrls)(Wire(new InstrCtr()))
    val done_latch = Module(new SRFF())
    val RootController = new RootController_kernel(List(x33_y), List(x32_x) , None, List(), -1, 1, 1, List(1), List(32), breakpoints, instrctrs.toList, rr)
    RootController.baseEn := top.io.enable && rr && ~done_latch.io.output
    RootController.resetMe := getRetimed(top.accelReset, 1)
    RootController.mask := true.B
    RootController.sm.io.parentAck := top.io.done
    RootController.sm.io.enable := RootController.baseEn & !top.io.done & true.B
    done_latch.io.input.reset := RootController.resetMe
    done_latch.io.input.asyn_reset := RootController.resetMe
    top.io.done := done_latch.io.output
    RootController.sm.io.ctrDone := risingEdge(RootController.sm.io.ctrInc)
    RootController.backpressure := true.B | RootController.sm.io.doneLatch
    RootController.forwardpressure := true.B | RootController.sm.io.doneLatch
    RootController.sm.io.enableOut.zip(RootController.smEnableOuts).foreach{case (l,r) => r := l}
    RootController.sm.io.break := false.B
    RootController.mask := true.B & true.B
    RootController.configure("RootController", None, None, isSwitchCase = false)
    RootController.kernel()
    done_latch.io.input.set := RootController.done
    Instrument.connect(top, instrctrs)
    Ledger.finish()
  }
}
