from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, hub,\
    scanning,artifactPickup, iForgot, firstPairArtifact, \
     calibration2, theRestofUs, calibrate, scanHSV
from pybricks.tools import run_task
import gc

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
    await yellowTowers()
    #print("yellow towers: ", watch.time()/1000)
    await scanning()
    #print("scanning: ", watch.time()/1000)
    await calibrate()
    #print("calibration: ", watch.time()/1000)
    await artifactPickup()
    #print("artifact pickup: ", watch.time()/1000)
    await iForgot()
    #print("iforgot: ", watch.time()/1000)
    await firstPairArtifact()
    #print("first artifact dropoff: ", watch.time()/1000)
    await calibration2()
    #print("calibration again: ", watch.time()/1000)
    await theRestofUs()
    #print("the rest of us: ", watch.time()/1000)
if __name__ == "__main__":
    print(db.distance_control.pid(24000, 0, 9000, 5, 10))
    run_task(main())