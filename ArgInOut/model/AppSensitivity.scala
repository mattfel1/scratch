package model
import models.Sensitivity

object AppSensitivity extends App {
  override def main(args: Array[String]): Unit = {
    val center: Map[String,String] = Map()
    println(s"Center: $center") 
    println(s"Hashcode mapping:")
    Sensitivity.around("/local/ssd/home/mattfel/sp_fixes/spatial/./gen/VCS/ArgInOut///ArgInOut_data.csv", center)
  }
}
