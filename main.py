from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, async_wrapper, colorScanning, moveAttachmentArms, hub, \
    moveLeftArm, moveRightArm, moveUntilColor, correction, scanning,artifactPickup, iForgot, firstPairArtifact, calibration1, artifactPickup2, secondPairArtifact, calibration2, theRestofUs
from pybricks.tools import run_task, multitask, wait
import gc
colors = [Color.GREEN, Color.BLUE, Color.BLUE, Color.RED]

async def main():

    print(round((hub.battery.voltage()-6500)/19))
    # initialization and running garbage collector
    gc.collect()
    db.settings(240, 650, 120, 250)
    #db.settings(500, 1000, 500, 600)
    watch.reset()
    watch.resume()
    await resetDB()
    # yellow towers + time

    await yellowTowers()
    await scanning()
    await artifactPickup()
    await iForgot()
    await firstPairArtifact()
    await calibration1()
    await artifactPickup2()
    await secondPairArtifact()
    await calibration2()
    await theRestofUs()

if __name__ == "__main__":
    print(db.distance_control.pid(30000, 0, 9000, 5, 10))
    run_task(main())
 
