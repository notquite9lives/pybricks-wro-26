from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, async_wrapper, colorScanning, moveAttachmentArms, hub, \
    moveLeftArm, moveRightArm, moveUntilColor, correction
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

    await resetDB()

    await multitask(
        async_wrapper(db.straight, 231),
        moveAttachmentArms(10, 165)
    )

    await moveRightArm(40,-12)
    await db.turn(90)

    await multitask(
        async_wrapper(db.straight, 250),
        moveAttachmentArms(10, 165)
    )
    await wait(100)
    db.settings(200, 200, 80, 150)
    await db.straight(260)    

    await moveAttachmentArms(40, -340)
    await moveLeftArm(40, -10)
    db.settings(300, 200, 80, 150)
    await db.straight(-332)
    await db.turn(-90)
    await db.straight(450)
    await db.straight(208)
    await moveAttachmentArms(40, 150)
    await moveRightArm(40, -15)
    await db.straight(-300)
    await moveAttachmentArms(40, 50)
    await db.turn(-90)
    await db.straight(780)

if __name__ == "__main__":
    print(db.distance_control.pid(30000, 0, 9000, 5, 10))
    run_task(main())
 
