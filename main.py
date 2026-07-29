from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, async_wrapper, colorScanning, moveAttachmentArms, hub, \
    moveLeftArm, moveRightArm, moveUntilColor
from pybricks.tools import run_task, multitask
import gc
color_list = [Color.RED, Color.GREEN, Color.BLACK, Color.BLUE, Color.YELLOW]


async def main():
    """
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
    print(watch.time()/1000)

    # color scanning the artifacts
    await db.turn(-90)
    await db.straight(-70)
    await db.turn(-90)
    await db.straight(-100)
    await db.turn(-4)
    await db.straight(20)
    db.settings(250, 700, 150, 300)
    colors = await multitask(async_wrapper(db.straight, 690), colorScanning())
    print(colors)
    colors = colors[1]

    # picking up artifacts
    await moveAttachmentArms(40,-270)
    await db.turn(90)
    await db.straight(-250)"""
    db.settings(260, 600, 160, 300)
    colors = [Color.GREEN, Color.RED, Color.GREEN, Color.BLUE]
    await db.straight(320)
    await db.turn(90)
    await db.straight(255)
    await db.turn(90)
    await db.straight(190)
    await moveAttachmentArms(30, 250)
    await db.turn(180)
    await db.straight(200)
    await moveUntilColor(Color.RED, 40)
    await db.straight(-55)
    #await db.straight(600)

    #color thingy
    if colors[3] == Color.YELLOW:
        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(410)
        await db.turn(-90)
        await db.straight(170)
        await moveLeftArm(40,-270)
        if colors[2] == Color.BLUE:
            await moveRightArm(40,-270)
        elif colors[2] == Color.BLACK:
            pass
        elif colors[2] == Color.RED:
            pass
        elif colors[2] == Color.GREEN:
            pass

    
    elif colors[3] == Color.BLUE:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(235)
        await db.turn(-90)
        await db.straight(172)
        await moveLeftArm(40,-270)

        if colors[2] == Color.BLACK:
            await moveRightArm(40, -270)

        elif colors[2] == Color.RED:
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(267)
            await db.turn(90)
            await db.straight(140)
            await moveRightArm(40,-270)

        elif colors[2] == Color.GREEN:
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(135)
            await db.turn(90)
            await db.straight(140)
            await moveRightArm(40,-270)

        elif colors[2] == Color.YELLOW:
            await db.straight(-140)
            await db.turn(90)
            await db.straight(92)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(90)
            await db.straight(100)
            await db.turn(-90)
            await db.straight(250)
            await db.turn(90)
            db.settings(200, 500, 120, 200)
            await db.straight(-265)


    elif colors[3] == Color.BLACK:
        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(140)
        await db.turn(-90)
        await db.straight(170)
        await moveLeftArm(40,-270)
        if colors[2] == Color.GREEN:
            await moveRightArm(40, -270)
        elif colors[2] == Color.RED:
            pass
        elif colors[2] == Color.BLUE:
            pass
        elif colors[2] == Color.BLACK:
            pass


    elif colors[3] == Color.GREEN:
        await db.turn(-1)
        await db.straight(150)
        await moveLeftArm(40,-270)
        if colors[2] == Color.RED:
            await moveRightArm(40, -270)
        elif colors[2] == Color.BLACK:
            pass
        elif colors[2] == Color.BLUE:
            pass
        elif colors[2] == Color.YELLOW:
            pass

    
    elif colors[3] == Color.RED:
        await db.turn(-87)
        await db.straight(130)
        await db.turn(90)
        await db.straight(170)
        await moveLeftArm(40,-270)
        if colors[2] == Color.GREEN:
            pass
        elif colors[2] == Color.BLACK:
            pass
        elif colors[2] == Color.BLUE:
            pass
        elif colors[2] == Color.YELLOW:
            pass

    """else:
        await db.straight(90)
        x = color_list.index(colors[3]) - color_list.index(colors[2])
        await db.straight(-80)
        if x > 0:
            await db.turn(90)
        else:
            await db.turn(-90)
        await db.straight(abs(x * 125 - 154))
        await db.turn(90)

        await db.straight(170)
        await moveRightArm(40,-270)
        await db.straight(-90)"""


if __name__ == "__main__":
    print(db.distance_control.pid(28000, 0, 7500, 4, 9))
    run_task(main())
 
