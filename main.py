from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, async_wrapper, colorScanning, moveAttachmentArms, hub, \
    moveLeftArm, moveRightArm, moveUntilColor, correction
from pybricks.tools import run_task, multitask, wait
import gc
colors = [Color.BLUE, Color.YELLOW, Color.BLACK, Color.RED]

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


    """
    //
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
    await db.straight(320)
    await db.turn(90)
    await db.straight(253)
    await db.turn(90)
    await db.straight(190)
    await moveAttachmentArms(30, 250)
    await db.turn(180)

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
        await db.straight(361)
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
            await db.straight(392)
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
            db.settings(260, 700, 150, 300)


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

    await db.turn(-1)
    await db.straight(-140)
    print(colors)
    
    if colors[2] == Color.YELLOW:
        await db.turn(-90)
        await db.straight(535)
        await db.turn(90)
        await db.straight(-900)

    elif colors[2] == Color.BLUE:
        await db.turn(-90)
        await db.straight(390)
        await db.turn(90)
        await db.straight(-900)

    elif colors[2] == Color.BLACK:
        await db.turn(-90)
        await db.straight(328)
        await db.turn(90)
        await db.straight(-900)

    elif colors[2] == Color.GREEN:
        await db.turn(-90)
        await db.straight(130)
        await db.turn(90)
        await db.straight(-900)

    else:
        await db.straight(-900)

    db.stop()
    db.reset()
    wait(100)

    await db.straight(300)
    await db.turn(90)
    await db.straight(368)
    await db.turn(93)
    await db.straight(240)
    await moveAttachmentArms(40, 280)
    await db.turn(180)
    await db.straight(600)

    if colors[1] == Color.YELLOW:
        await db.turn(90)
        await db.straight(61)
        await db.turn(-90)
        await moveLeftArm(40,-270)
        
        if colors[0] == Color.BLUE:
           print(colors[0])
           moveRightArm(40, -270)

        await db.straight(-150)
        await db.turn(180)
        await db.straight(-350)
        await db.straight(150)
        await db.turn(180)

        if colors[0] == Color.GREEN:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(260)
            await moveRightArm(40,-270)
            await db.straight(-150)
            await db.turn(180)
            await db.straight(-340)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(390)
            await moveRightArm(40,-270)
            await db.straight(-150)
            await db.turn(180)
            await db.straight(-340)
            await db.straight(150)
            await db.turn(180)


        

        





    color_list = [Color.RED, Color.GREEN, Color.BLACK, Color.BLUE, Color.YELLOW]
"""
    for i in colors:
        if color_list.index(i) == colors[2]:
            z = i*130
            db.turn(-90)
            db.straight(z)
            db.turn(90)
            db.straight(-900)

    else:
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
 
