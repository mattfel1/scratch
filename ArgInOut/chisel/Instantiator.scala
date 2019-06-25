package top

import accel._
import fringe._
import chisel3.core.Module
import chisel3._
import chisel3.util._
import chisel3.iotesters.{ChiselFlatSpec, Driver, PeekPokeTester}

import scala.collection.mutable.ListBuffer
/**
 * Top test harness
 */
class TopUnitTester(c: Top)(implicit args: Array[String]) extends ArgsTester(c) {
}

object Instantiator extends CommonMain {
  type DUTType = Top
  
  def dut = () => {
    // Non-memory Streams
    val streamInsInfo = List()
    val streamOutsInfo = List()
    
    // Scalars
    val numArgIns_reg = 1
    val numArgOuts_reg = 1
    val numArgIOs_reg = 0
    //x32_x = argIns(0) ( x )
    //x33_y = argOuts(0) ( y )
    val io_argOutLoopbacksMap: scala.collection.immutable.Map[Int,Int] = Map()
    
    // Memory streams
    val loadStreamInfo = List() 
    val storeStreamInfo = List() 
    val gatherStreamInfo = List() 
    val scatterStreamInfo = List() 
    val numArgIns_mem = 0
    // Heap
    val numAllocators = 0
    
    // Instrumentation
    val numArgOuts_instr = 2
    val numCtrls = 1
    val numArgOuts_breakpts = 0
    /* Breakpoint Contexts:
    */
    val w = if (this.target == "zcu") 32 else if (this.target == "VCS" || this.target == "ASIC") 8 else 32
    val numArgIns = numArgIns_mem  + numArgIns_reg + numArgIOs_reg
    val numArgOuts = numArgOuts_reg + numArgIOs_reg + numArgOuts_instr + numArgOuts_breakpts
    val numArgIOs = numArgIOs_reg
    val numArgInstrs = numArgOuts_instr
    val numArgBreakpts = numArgOuts_breakpts
    new Top(this.target, () => Module(new AccelTop(w, numArgIns, numArgOuts, numArgIOs, numArgOuts_instr + numArgBreakpts, numAllocators, loadStreamInfo, storeStreamInfo, gatherStreamInfo, scatterStreamInfo, streamInsInfo, streamOutsInfo)))
  }
  def tester = { c: DUTType => new TopUnitTester(c) }
}
