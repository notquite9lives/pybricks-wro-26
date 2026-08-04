from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, async_wrapper, colorScanning, moveAttachmentArms, hub, \
    moveLeftArm, moveRightArm, moveUntilColor, correction, color_sensor1, moveUntilHSV
from pybricks.tools import run_task, multitask
import gc
color_list = [Color.RED, Color.GREEN, Color.BLACK, Color.GREEN]


async def main():

    print(round((hub.battery.voltage()-6500)/19))
    # initialization and running garbage collector
    gc.collect()
    db.settings(240, 650, 120, 250)
    #db.settings(500, 1000, 500, 600)
    watch.reset()
    watch.resume()
    await resetDB()
    """# yellow towers + time
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
    #raise Exception("terminate code")
    colors = [None, None, Color.RED, Color.YELLOW]
    db.settings(260, 600, 160, 300)
    await db.straight(320)
    await db.turn(90)
    await db.straight(253)
    await db.turn(90)
    await db.straight(190)
    await moveAttachmentArms(30, 250)
    await db.turn(180)
    """await db.straight(200)
    await moveUntilColor(Color.RED, 40)
    await db.straight(-55)"""



    if colors[3] == Color.GREEN:
        await db.straight(300)
        await db.turn(-90)
        await db.straight(37)
        await db.turn(90)
        await db.straight(320)
    else:
        await db.straight(600)

    #color thingy
    if colors[3] == Color.YELLOW:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(362)
        await db.turn(-90)
        await db.straight(176)
        await moveLeftArm(40,-270)

        if colors[2] == Color.BLUE:
            await moveRightArm(40,-270)

        elif colors[2] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(130)
            await db.turn(90)
            await db.straight(140)
            await moveRightArm(40, -270)

        elif colors[2] == Color.RED:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(495)
            await db.turn(90)
            await db.straight(140)
            await moveRightArm(40, -270)

        elif colors[2] == Color.GREEN:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(260)
            await db.turn(90)
            await db.straight(140)
            await moveRightArm(40,-270)
            
            

    
    elif colors[3] == Color.BLUE:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(231)
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
            await db.turn(-2)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(252)
            await db.turn(-90)
            await db.straight(355)
            await db.turn(1)
            await moveRightArm(40, -270)


    elif colors[3] == Color.BLACK:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(100)
        await db.turn(-90)
        await db.straight(172)
        await moveLeftArm(40,-270)

        if colors[2] == Color.GREEN:
            await moveRightArm(40, -270)

        elif colors[2] == Color.RED:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(135)
            await db.turn(90)
            await db.straight(140)
            await moveRightArm(40,-270)
#hi
        elif colors[2] == Color.BLUE:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(250)
            await db.turn(-90)
            await db.straight(147)
            await moveRightArm(40, -270)

        elif colors[2] == Color.YELLOW:
            await db.turn(-2)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(382)
            await db.turn(-90)
            await db.straight(350)
            await db.turn(1)
            await moveRightArm(40, -270)


    elif colors[3] == Color.GREEN:

        await db.turn(6)
        await db.straight(150)
        await moveLeftArm(40,-270)

        if colors[2] == Color.RED:
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(245)
            await db.turn(-90)
            await db.straight(140)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLUE:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(372)
            await db.turn(-90)
            await db.straight(145)
            await moveRightArm(40, -270)

        elif colors[2] == Color.YELLOW:
            await db.turn(-2)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(507)
            await db.turn(-90)
            await db.straight(350)
            await db.turn(1)
            await moveRightArm(40, -270)

    
    elif colors[3] == Color.RED:

        await db.turn(-87)
        await db.straight(150)
        await db.turn(90)
        await db.straight(170)
        await moveLeftArm(40,-270)

        if colors[2] == Color.GREEN:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(245)
            await db.turn(-90)
            await db.straight(140)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(372)
            await db.turn(-90)
            await db.straight(130)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLUE:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(502)
            await db.turn(-90)
            await db.straight(125)
            await db.turn(1)
            await moveRightArm(40, -270)

        elif colors[2] == Color.YELLOW:
            await db.turn(-1)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(632)
            await db.turn(-90)
            await db.straight(330)
            await db.turn(1)
            await moveRightArm(40, -270)

    await db.straight(-140)


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
 
