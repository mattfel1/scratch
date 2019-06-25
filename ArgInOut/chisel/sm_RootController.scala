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

/** Hierarchy: x9 **/
/** BEGIN None RootController **/
class RootController_kernel(
  list_x33_y: List[MultiArgOut],
  list_x32_x: List[UInt],
  parent: Option[Kernel], cchain: List[CounterChainInterface], childId: Int, nMyChildren: Int, ctrcopies: Int, ctrPars: List[Int], ctrWidths: List[Int], breakpoints: Vec[Bool], instrctrs: List[InstrCtr], rr: Bool
) extends Kernel(parent, cchain, childId, nMyChildren, ctrcopies, ctrPars, ctrWidths) {
  
  val me = this
  val sm = Module(new InnerControl(Sequenced, false   , latency = 2.0.toInt, myName = "RootController_sm")); sm.io <> DontCare
  val iiCtr = Module(new IICounter(1.0.toInt, 2 + fringe.utils.log2Up(1.0.toInt), "RootController_iiCtr"))
  
  abstract class RootController_module(depth: Int)(implicit stack: List[KernelHash]) extends Module {
    val io = IO(new Bundle {
      val in_x32_x = Input(UInt(64.W))
      val in_x33_y = new MultiArgOut(1)
      val in_instrctrs = Vec(api.numCtrls, Output(new InstrCtr()))
      val in_breakpoints = Vec(api.numArgOuts_breakpts, Output(Bool()))
      val sigsIn = Input(new InputKernelSignals(1, 1, List(1), List(32)))
      val sigsOut = Output(new OutputKernelSignals(1, 1))
      val rr = Input(Bool())
    })
    def x32_x = {io.in_x32_x} 
    def x33_y = {io.in_x33_y} ; io.in_x33_y := DontCare
  }
  def connectWires0(module: RootController_module)(implicit stack: List[KernelHash]): Unit = {
    module.io.in_x32_x <> x32_x
    x33_y.connectLedger(module.io.in_x33_y)
    module.io.in_x33_y.port.zip(x33_y.port).foreach{case (l,r) => l.ready := r.ready}
  }
  val x33_y = list_x33_y(0)
  val x32_x = list_x32_x(0)
  def kernel(): Unit = {
    Ledger.enter(this.hashCode, "RootController")
    implicit val stack = ControllerStack.stack.toList
    class RootController_concrete(depth: Int)(implicit stack: List[KernelHash]) extends RootController_module(depth) {
      io.sigsOut := DontCare
      val breakpoints = io.in_breakpoints; breakpoints := DontCare
      val instrctrs = io.in_instrctrs; instrctrs := DontCare
      val rr = io.rr
      val cycles = Module(new InstrumentationCounter())
      val iters = Module(new InstrumentationCounter())
      cycles.io.enable := io.sigsIn.baseEn
      iters.io.enable := risingEdge(io.sigsIn.done)
      Ledger.tieInstrCtr(instrctrs.toList, ROOTCONTROLLER_instrctr, cycles.io.count, iters.io.count, 0.U, 0.U)
      val x37_rd_x32 = Wire(new FixedPoint(true, 32, 0))
      x37_rd_x32.r := x32_x.r
      val x38_sum = Wire(new FixedPoint(true, 32, 0)).suggestName("""x38_sum""")
      x38_sum.r := Math.add(x37_rd_x32,4L.FP(true, 32, 0),Some(1.0), true.B, Truncate, Wrapping, "x38_sum").r
      x33_y.connectWPort(0, util.Cat(util.Fill(32, x38_sum.msb), x38_sum.r), true.B & getRetimed(io.sigsIn.datapathEn & io.sigsIn.iiDone, 1.0.toInt, io.sigsIn.backpressure))
    }
    val module = Module(new RootController_concrete(sm.p.depth)); module.io := DontCare
    connectWires0(module)
    Ledger.connectInstrCtrs(instrctrs, module.io.in_instrctrs)
    Ledger.connectBreakpoints(breakpoints, module.io.in_breakpoints)
    module.io.rr := rr
    module.io.sigsIn := me.sigsIn
    me.sigsOut := module.io.sigsOut
    Ledger.exit()
  }
}
/** END AccelScope RootController **/
