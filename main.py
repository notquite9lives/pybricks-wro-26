from pybricks.parameters import Color

from wrotools import db, yellowTowers, watch, resetDB, async_wrapper, colorScanning, moveAttachmentArms, hub, moveLeftArm, moveRightArm
from pybricks.tools import run_task, multitask
import gc

color_list = [Color.RED, Color.GREEN, Color.BLACK, Color.BLUE, Color.YELLOW]


async def main():
    """the main function :)"""
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
    await db.straight(-95)
    await db.turn(-90)
    await db.straight(-80)
    await db.turn(-3)
    db.settings(250, 700, 150, 300)
    await db.straight(20)
    colors = await multitask(async_wrapper(db.straight, 670), colorScanning())
    print(colors)
    colors = colors[1]
   
    # picking up artifacts
    await moveAttachmentArms(40,-270)
    await db.turn(90)
    await db.straight(-250)
    await db.straight(320)
    await db.turn(90)
    await db.straight(250)
    await db.turn(90)
    await db.straight(193)
    await moveAttachmentArms(30, 250)
    await db.turn(180)
    await db.straight(600)

    print()
    #color thingy
    if colors[3] == Color.YELLOW:
        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(400)
        await db.turn(-90)
        await db.straight(170)
        await moveLeftArm(40,-270)
        await db.straight(-90)
    
    if colors[3] == Color.BLUE:
        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(260)
        await db.turn(-90)
        await db.straight(170)
        await moveLeftArm(40,-270)
        await db.straight(-90)

    if colors[3] == Color.BLACK:
        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(850)
        await db.turn(-90)
        await db.straight(170)
        await moveLeftArm(40,-270)
        await db.straight(-90)

    if colors[3] == Color.GREEN:
        await db.straight(170)
        await moveLeftArm(40,-270)
        await db.straight(-90)
    
    if colors[3] == Color.RED:
        await db.turn(-87)
        await db.straight(150)
        await db.turn(90)
        await db.straight(170)
        await moveLeftArm(40,-270)
        await db.straight(-90)

    x = color_list.index(colors[3]) - color_list.index(colors[2])
    await db.straight(-80)
    if x > 0:
        await db.turn(-90)
    else :
        await db.turn(90)
    await db.straight(x * 125)
    await db.turn(90)
    await db.straight(170)
    await moveRightArm(40,-270)
    await db.straight(-90)

if __name__ == "__main__":
    print(db.distance_control.pid(27000, 0, 7000, 4, 9))
    run_task(main())
 
