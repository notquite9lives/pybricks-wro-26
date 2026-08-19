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
    await db.straight(-250)""""""""
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
"""
"""
    db.stop()
    db.reset()
    wait(100)

    await db.straight(300)
    await db.turn(90)
    await db.straight(357)
    await db.turn(93)
    db.settings(140, 650, 120, 250)
    await db.straight(240)
    await moveAttachmentArms(40, 270)
    await db.straight(-100)
    await db.turn(180)
    await db.straight(500)
    db.settings(240, 650, 120, 250)

    if colors[1] == Color.YELLOW:
        await db.turn(90)
        await db.straight(51)
        await db.turn(-90)
        await moveLeftArm(40,-270)

        if colors[0] == Color.BLUE:
           print(colors[0])
           await moveRightArm(40, -270)

        await db.straight(-100)
        await db.turn(180)
        await db.straight(-320)
        await db.straight(150)
        await db.turn(90)
        await resetDB()

        if colors[0] == Color.GREEN:
            await db.straight(250)
            await db.turn(90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-255)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.BLACK:
            await db.straight(145)
            await db.turn(90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.turn(3)
            await db.straight(-255)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.RED:
            await db.straight(405)
            await db.turn(90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.turn(3)
            await db.straight(-255)
            await db.straight(150)
            await db.turn(180)

    if colors[1] == Color.RED:


        # 26, 36, 48.5 62.5
        await db.turn(-90)
        await db.straight(488)
        await db.turn(90)
        await moveLeftArm(40,-270)
        await db.straight(-100)
        await db.turn(180)
        await db.straight(-310)
        if colors[0] == Color.YELLOW:
            await db.straight(350)
        else:
            await db.straight(150)
        await db.turn(-90)
        await resetDB()

        if colors[0] == Color.GREEN:
            await db.straight(250)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-248)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.BLACK:
            await db.straight(386)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-248)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.BLUE:
            await db.straight(520)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-248)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.YELLOW:
            await db.straight(651)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-456)
            await db.straight(150)
            await db.turn(180)

    if colors[1] == Color.GREEN:
        await db.turn(-90)
        await db.straight(340)
        await db.turn(90)
        await moveLeftArm(40,-270)

        if colors[0] == Color.RED:
            print(colors[0])
            await moveRightArm(40, -270)

        await db.turn(-1)
        await db.straight(-100)
        await db.turn(180)
        await db.straight(-308)
        if colors[0] == Color.YELLOW:
            await db.straight(350)
        else:
            await db.straight(150)

        if colors[0] == Color.BLACK:
            await db.turn(-90)
            await db.straight(250)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-248)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.BLUE:
            await db.turn(-90)
            await db.straight(386)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-248)
            await db.straight(150)
            await db.turn(180)

        if colors[0] == Color.YELLOW:
            await db.turn(-90)
            await db.straight(520)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-448)
            await db.straight(150)
            await db.turn(180)

    if colors[1] == Color.BLACK:
        await db.turn(-90)
        await db.straight(218)
        await db.turn(90)
        await moveLeftArm(40,-270)

        if colors[0] == Color.GREEN:
            print(colors[0])
            await moveRightArm(40, -270)

        await db.turn(-1)
        await db.straight(-100)
        await db.turn(180)
        await db.straight(-315)
        await db.turn(1)
        await db.straight(350 if colors[0] == Color.YELLOW else 150)

        if colors[0] == Color.RED:
            await db.turn(90)
            await db.straight(135)
            await db.turn(90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.turn(3)
            await db.straight(-249)
            await db.straight(156)
            await db.turn(180)

        elif colors[0] == Color.BLUE:
            await db.turn(-90)
            await db.straight(255)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-248)
            await db.straight(150)
            await db.turn(180)

        elif colors[0] == Color.YELLOW:
            await db.turn(-90)
            await db.straight(386)
            await db.turn(-90)
            await moveRightArm(40,-270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-453)
            await db.straight(150)
            await db.turn(180)

    if colors[1] == Color.BLUE:
        await db.turn(-90)
        await db.straight(72)
        await db.turn(90)
        await moveLeftArm(40, -270)

        if colors[0] == Color.BLACK:
            print(colors[0])
            await moveRightArm(40, -270)

        await db.turn(-1)
        await db.straight(-100)
        await db.turn(180)
        await db.straight(-318)
        await db.turn(1)
        await db.straight(350 if colors[0] == Color.YELLOW else 150)

        if colors[0] == Color.RED:
            await db.turn(90)
            await db.straight(265)
            await db.turn(90)
            await moveRightArm(40, -270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-255)
            await db.straight(150)
            await db.turn(180)

        elif colors[0] == Color.GREEN:
            await db.turn(90)
            await db.straight(150)
            await db.turn(90)
            await moveRightArm(40, -270)
            await db.straight(-100)
            await db.turn(180)
            await db.turn(3)
            await db.straight(-255)
            await db.straight(150)
            await db.turn(180)

        elif colors[0] == Color.YELLOW:
            await db.turn(-90)
            await db.straight(250)
            await db.turn(-90)
            await moveRightArm(40, -270)
            await db.straight(-100)
            await db.turn(180)
            await db.straight(-448)
            await db.straight(150)
            await db.turn(180)



    color_list = [Color.RED, Color.GREEN, Color.BLACK, Color.BLUE, Color.YELLOW]

    if colors[0] == Color.YELLOW:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(810)
        await db.turn(-90)
        await db.straight(-400)
        
    if colors[0] == Color.BLUE:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(690)
        await db.turn(-90)
        await db.straight(-400)
        
    if colors[0] == Color.BLACK:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(560)
        await db.turn(-90)
        await db.straight(-400)
        
    if colors[0] == Color.GREEN:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(430)
        await db.turn(-90)
        await db.straight(-400)

    if colors[0] == Color.BLUE:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(300)
        await db.turn(-90)
        await db.straight(-400)
"""
    resetDB()

    await multitask(
        async_wrapper(db.straight, 268),
        moveAttachmentArms(10, 165)
    )
  
    await db.turn(90)

    await multitask(
        async_wrapper(db.straight, 250),
        moveAttachmentArms(10, 165)
    )
    await wait(100)
    db.settings(60, 200, 80, 150)
    await db.straight(260)    

    await moveAttachmentArms(40, -260)
    db.settings(300, 200, 80, 150)
    await db.straight(-350)
    await db.turn(-90)
    await db.straight(450)  

    db.settings(60, 200, 80, 150)
    await db.straight(160) 
    await moveAttachmentArms(40, 150)

if __name__ == "__main__":
    print(db.distance_control.pid(30000, 0, 9000, 5, 10))
    run_task(main())
 
