from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, hub,\
    scanning,artifactPickup, iForgot, firstPairArtifact, calibration1, \
    artifactPickup2, secondPairArtifact, calibration2, theRestofUs, calibrate, scanHSV
from pybricks.tools import run_task
import gc
colors = [Color.GREEN, Color.YELLOW, Color.BLACK, Color.RED]
    
async def main():
    print(round((hub.battery.voltage()-6500)/19))
    # initialization and running garbage collector
    gc.collect()
    
    db.settings(240, 650, 120, 250)
    #db.settings(500, 1000, 500X, 600)
    watch.reset()
    watch.resume()
    await resetDB()
    # yellow towers + time
    print(await scanHSV())
    await yellowTowers()
    await scanning()
    await calibrate()
    await artifactPickup()
    await iForgot()
    await firstPairArtifact()
    await calibration1()
    await artifactPickup2()
    await secondPairArtifact()
    await calibration2()
    print(watch.time())
    await theRestofUs()
    print(watch.time())
if __name__ == "__main__":
    print(db.distance_control.pid(24000, 0, 9000, 5, 10))
    run_task(main())
 
