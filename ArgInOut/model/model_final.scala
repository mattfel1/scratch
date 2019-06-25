package model
import models.Runtime._

object AppRuntimeModel_final extends App {
  def build_model(): ControllerModel = {
    val x9 = new ControllerModel(9, InnerControl, Left(Sequenced), CChainModel(Seq()), 2, 1, Ctx("x9", "18", "Accel {", "x9 = AccelScope(Block(Const(())))"))
    x9
  }
  
  override def main(args: Array[String]): Unit = {
    begin("/local/ssd/home/mattfel/sp_fixes/spatial/./gen/VCS/ArgInOut///results_final")
    if (args.size >= 1 && (args.contains("noninteractive") || args.contains("ni"))) {
        interactive = false
        val idx = {0 max args.indexOf("noninteractive")} + {0 max args.indexOf("ni")}
        cliParams = args.drop(idx+1).takeWhile{_ != "tune"}.map(_.toInt)
        emit(s"Noninteractive Args: ${cliParams.mkString(" ")}") 
    }
    else {
      println(s"Suggested args: List()")
    }
    val allTuneParams: Seq[Map[String, Any]] = if (args.size >= 1 && (args.contains("tune"))) {
        retune = true
        val indices: Seq[Int] = args.zipWithIndex.filter(_._1 == "tune").map(_._2)
        indices.map{idx => args.drop(idx+1).takeWhile{x => x != "noninteractive" && x != "ni" && x != "tune"}.grouped(2).map{x => (x(0) -> {try {x(1).toInt} catch {case _: Throwable => x(1)}} )}.toMap}
    } else {Seq(Map[String, Any]())}
    isFinal = true
    val root = build_model()
    root.initializeAskMap(AskMap.map)
    root.loadPreviousAskMap(PreviousAskMap.map) // Load previous run's askmap
    emit(s"[final] Structure for app ArgInOut")
    allTuneParams.foreach{tuneTo => 
        tuneParams = tuneTo
        root.printStructure()
        root.execute()
        emit(s"[final] Runtime results for app ArgInOut")
        root.printResults()
        root.storeAskMap("/local/ssd/home/mattfel/sp_fixes/spatial/./gen/VCS/ArgInOut///model/PreviousAskMap.scala") // Store this run's askmap
        emit(s"[final] Total Cycles for App ArgInOut: ${root.totalCycles()}")
    }
    end()
  }
}
