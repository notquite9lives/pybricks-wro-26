# WRO TOOLS FILE
# version: 1.2
# date: 15/6/2026

import gc, random

import umath
from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Color
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask

# MATH STUFF

pi: float = umath.pi

# ROBOT HARDWARE DETAILS

wheel_diameter: float = 68.8
wheel_circumference: float = wheel_diameter * pi
distance_between_wheels: int = 198
colors = []
# INITIALIZATION            

hub: PrimeHub = PrimeHub()
left_motor: Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor: Motor = Motor(Port.D)
color_sensor1: ColorSensor = ColorSensor(Port.C)
color_sensor2: ColorSensor = ColorSensor(Port.F)
attachment_left: Motor = Motor(Port.E)
attachment_right: Motor = Motor(Port.A)
db: DriveBase = DriveBase(left_motor, right_motor, wheel_diameter, distance_between_wheels)
db.use_gyro(True)
watch: StopWatch = StopWatch()
watch.reset()
hub.imu.reset_heading(0)
colors = []
validColors = [Color.BLACK, Color.GREEN, Color.BLUE, Color.YELLOW, Color.RED]


# HELPER FUNCTIONS

async def resetDB() -> None:

    """
    Resets the driving base
    """

    db.reset()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    print("reset complete")
    await wait(50)

def convertSpeed(speed: float) -> float:
    """
    Converts percentage speed to degrees per second
    
    :param speed: The percentage speed being converted
    :type speed: int, %
    :return: The converted degrees per second measure of the percentage speed
    :rtype: Number, deg/st
    """
    return (speed/100) * 1050

async def moveAttachmentArms(speed: float, angle: int) -> None:
    """
    Moves both the attachment arms at the same time

    :param speed: The percentage speed that the arms will move at
    :type speed: int, %
    :param angle: The angle the arms will move by
    :type angle: int, deg
    """

    speed = convertSpeed(speed)

    async def move_right():
        await attachment_right.run_angle(speed, -angle)
        
    async def move_left():
        await attachment_left.run_angle(speed, angle)
        
    
    await multitask(move_right(), move_left())

async def moveRightArm(speed: float, angle: int) -> None:
    """
    Moves both the attachment arms at the same time

    :param speed: The percentage speed that the arms will move at
    :type speed: int, %
    :param angle: The angle the arms will move by
    :type angle: int, deg
    """

    speed = convertSpeed(speed)
    await attachment_right.run_angle(speed, -angle)

async def moveLeftArm(speed: float, angle: int) -> None:
    """
    Moves both the attachment arms at the same time

    :param speed: The percentage speed that the arms will move at
    :type speed: int, %
    :param angle: The angle the arms will move by
    :type angle: int, deg
    """

    speed = convertSpeed(speed)
    await attachment_left.run_angle(speed, angle)

async def moveUntilReflection(reflection: int, speed: int, distance: int = 0, use_distance: bool = False) -> None:
    """
    Makes the robot move until either:
    - A. It reaches a color with a reflection below a certain threshold
    - B. A certain distance is reached

    :param reflection: The reflection threshold where the robot will stop moving
    :type reflection: int, %
    :param speed: The percentage speed that the bot will move at
    :type speed: int, %
    :param distance: The secondary distance threshold where the robot will stop
    :type distance: int, mm
    :param use_distance: Controls whether to use the distance check
    :type use_distance: bool
    """

    async def waitForColor():
        while await color_sensor1.reflection() > reflection:
            await wait(10)

    async def driveForever():
        db.drive(0.6004*convertSpeed(speed), 0)

        while True:
            await wait(10)
    
    async def detectDistance():
        while True:
            distance_moved = 0.6004*right_motor.angle()
            if distance_moved >= distance:
                break
            await wait(10)
        
    
    await resetDB()

    if use_distance:
        await multitask(driveForever(), waitForColor(), detectDistance(), race=True)
    else:
        await multitask(driveForever(), waitForColor(), race=True)

    db.brake()

async def moveUntilColor(color: Color, speed: int, distance: int = 0, use_distance: bool = False) -> None:
    """
    Makes the robot move until either:
    - A. It reaches a color with a reflection below a certain threshold
    - B. A certain distance is reached

    :param color: The color where the robot will stop moving
    :type color: Color
    :param speed: The percentage speed that the bot will move at
    :type speed: int, %
    :param distance: The secondary distance threshold where the robot will stop
    :type distance: int, mm
    :param use_distance: Controls whether to use the distance check
    :type use_distance: bool
    """

    async def waitForColor():
        while await color_sensor1.color() != color:
            await wait(10)

    async def driveForever():
        db.drive(0.6004 * convertSpeed(speed), 0)

        while True:
            await wait(10)

    async def detectDistance():
        while True:
            distance_moved = 0.6004 * right_motor.angle()
            if distance_moved >= distance:
                break
            await wait(10)

    await resetDB()

    if use_distance:
        await multitask(driveForever(), waitForColor(), detectDistance(), race=True)
    else:
        await multitask(driveForever(), waitForColor(), race=True)

    db.brake()

async def async_wrapper(func, *args, **kwargs):
    """
    Forces a pybricks MaybeAwaitable function to always behave like a coroutine so that it functions with the multitask() function

    :param func: The method to execute.
    :type func: Callable[..., Awaitable[Any]]
    :param args: Positional arguments for the method
    :type args: Any
    :param kwargs: Keyword arguments for the method
    :type kwargs: Any
    :return: The resolved value from the awaited method
    :rtype: Any
    """

    return await func(*args, **kwargs)

async def yellowTowers() -> None:
    """
    Running the first task, which includes:
    - Start calibration
    - Picking up both yellow towers
    - Moving and placing the tower tops on the bases
    """

    #db.distance_control.pid(10000, 0, 9000, 5, 10)

    db.settings(340, 900, 150, 300)

    # calibration
    await multitask(async_wrapper(db.straight, -500), moveAttachmentArms(60, 450))
    db.reset()


    # picking up the tower
    db.settings(1000,900,120,300)
    await db.straight(247)
    await db.turn(-90)
    db.stop()
    db.distance_control.pid(30000, 0, 9000, 5, 10)
    db.settings(660,750,150,300)
    #i luv peepee
    await db.straight(192)
    db.settings(150,300,120,300)
    await db.straight(120)
    db.settings(1000, 900, 150, 300)
    await moveAttachmentArms(40, -390) 

    # placing first tower
    db.settings(1000,850,150,300)
    await db.straight(-40)
    await db.turn(90)
    await db.straight(513)
    await moveUntilReflection(20, 45, 100) #fill distance properly
    db.settings(800, 850, 120, 250) 
    await db.turn(1)
    await db.straight(435)
    await moveAttachmentArms(40,270)
    await db.straight(-223)
    db.settings(500, 800, 160, 300)

    # calibration
    await db.turn(90)
    await db.straight(-307)


    # placing second tower
    db.settings(450,600,150,300)
    await moveUntilReflection(20, 40, 100) # fill distance properly
    await multitask(async_wrapper(db.straight, 328), moveAttachmentArms(40, -270))
    db.settings(240, 700, 120, 250)
    await db.turn(-90)
    await db.straight(221)
    await moveAttachmentArms(38,270)
    await db.straight(-85)
    db.settings(280, 800, 160, 300)
    await moveRightArm(38, 1)

async def colorScanning():
    """
    Scans colors (of artifacts) until a list of 4, unique, valid (as defined by list validColors) is formed

    :return: The list of scanned colors
    :rtype: list[Color]

    """
    cleanedList = []
    watch.reset()
    while True:
        h, s, v = await scanHSV()
        if 226 <= h <= 280 and Color.GREEN not in cleanedList:
                cleanedList.append(Color.GREEN)
                print(Color.BLACK, h,s,v)        
        elif 17 <= h <= 57 and Color.YELLOW not in cleanedList:
                cleanedList.append(Color.YELLOW)
                print(Color.YELLOW, h, s, v)
        elif 300 <= h <= 400  and Color.RED not in cleanedList:
                cleanedList.append(Color.RED)
                print(Color.RED, h, s, v)
        elif 130 <= h <= 180 and Color.BLUE not in cleanedList:
                cleanedList.append(Color.BLUE)
                print(Color.GREEN, h, s, v)
        elif 190 <= h <= 225 and Color.BLACK not in cleanedList:
                cleanedList.append(Color.BLACK)
                print(Color.BLUE, h, s, v)

        if len(cleanedList) == 4:
            print(cleanedList)
            break

        if watch.time() > 4000:
            filtered_list = [item for item in validColors if item not in cleanedList]
            while len(cleanedList) < 4:
                cleanedList.append(random.choice(filtered_list))

        await wait(50)

    gc.collect()
    return cleanedList

async def scanHSV():
    raw = await color_sensor2.hsv()
    return raw.h, raw.s, raw.v

async def moveUntilHSV(hue: int, saturation: int, value: int = 0, speed: int = 30):
    async def waitUntilHSV():
        while await scanHSV() != (hue, saturation, value):
            await wait(0.05)

    async def waitUntilHSV_noValue():
        h, s, _ = await scanHSV()
        while (h, s) != (hue, saturation):
            await wait(0.05)
            h, s, _ = await scanHSV()

    async def driveForever():
        db.drive(0.6004 * convertSpeed(speed), 0)

        while True:
            await wait(0.05)

    if value == 0:
        await multitask(waitUntilHSV_noValue(), driveForever(), race=True)
    else:
        await multitask(waitUntilHSV(), driveForever(), race=True)

async def scanning():
    global colors
    await db.turn(-90)
    await db.straight(-70)
    await db.turn(-90)
    await db.straight(-100)
    await db.turn(-4)
    await db.straight(30)
    db.settings(250, 700, 150, 300)
    colors = await multitask(async_wrapper(db.straight, 690), colorScanning())
    print(colors)
    colors = colors[1]

async def calibrate():
    await moveAttachmentArms(40,-270)
    await db.turn(90)
    await db.straight(-250)
    db.settings(300, 600, 160, 300)

async def artifactPickup():
    await db.straight(320)
    await db.turn(90)
    await db.straight(248)
    await db.turn(90)
    await db.straight(200)
    await moveAttachmentArms(30, 250)
    await db.turn(180)
    await db.straight(10)

async def iForgot():
    db.settings(480, 600, 160, 300)
    if colors[3] == Color.GREEN:
        await db.straight(300)
        await db.turn(-90)
        await db.straight(25)
        await db.turn(90)
        await db.straight(326)
    else:
        await db.straight(600)

async def firstPairArtifact():
    if colors[3] == Color.YELLOW:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(377)
        await db.turn(-90)
        await db.straight(172)
        await moveLeftArm(40,-270)

        if colors[2] == Color.BLUE:
            await moveRightArm(40,-270)
            await db.turn(-1)

        elif colors[2] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(145)
            await db.turn(90)
            await db.straight(130)
            await moveRightArm(40, -270)

        elif colors[2] == Color.RED:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(401)
            await db.turn(90)
            await db.straight(122)
            await moveRightArm(40, -270)

        elif colors[2] == Color.GREEN:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(270)
            await db.turn(90)
            await db.straight(122)
            await moveRightArm(40,-270)

    elif colors[3] == Color.BLUE:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(262)
        await db.turn(-2)
        await db.turn(-90)
        await db.straight(178)
        await moveLeftArm(40,-270)

        if colors[2] == Color.BLACK:
            await moveRightArm(40, -270)

        elif colors[2] == Color.RED:
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(274)
            await db.turn(90)
            await db.straight(132)
            await moveRightArm(40,-270)

        elif colors[2] == Color.GREEN:
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(138)
            await db.turn(90)
            await db.straight(134)
            await moveRightArm(40,-270)

        elif colors[2] == Color.YELLOW:
            await db.straight(-250)
            await db.turn(90)
            await db.straight(247)
            await db.turn(-90)
            await db.straight(250)
            await moveRightArm(40,-270)
            
    elif colors[3] == Color.BLACK:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(127)
        await db.turn(-90)
        await db.straight(168)
        await moveLeftArm(40,-270)
        await db.turn(-1)

        if colors[2] == Color.GREEN:
            await moveRightArm(40, -270)

        elif colors[2] == Color.RED:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(139)
            await db.turn(90)
            await db.straight(139)
            await moveRightArm(40,-270)

        elif colors[2] == Color.BLUE:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(266)
            await db.turn(-90)
            await db.straight(133)
            await moveRightArm(40, -270)

        elif colors[2] == Color.YELLOW:
            await db.turn(-2)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(378)
            await db.turn(-90)
            await db.straight(350)
            await db.turn(1)
            await moveRightArm(40, -270)

    elif colors[3] == Color.GREEN:

        await db.turn(6)
        await db.straight(142)
        await moveLeftArm(40,-270)

        if colors[2] == Color.RED:
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(243)
            await db.turn(-90)
            await db.straight(144)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLUE:
            await db.straight(-140)
            await db.turn(90)
            await db.straight(370)
            await db.turn(-90)
            await db.straight(142)
            await moveRightArm(40, -270)

        elif colors[2] == Color.YELLOW:
            await db.turn(-2)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(496)
            await db.turn(-90)
            await db.straight(336)
            await db.turn(1)
            await moveRightArm(40, -270)
    
    elif colors[3] == Color.RED:

        await db.turn(-86)
        await db.straight(143)
        await db.turn(90)
        await db.straight(165)
        await moveLeftArm(40,-270)

        if colors[2] == Color.GREEN:
            await db.turn(-1)
            await db.straight(-130)
            await db.turn(90)
            await db.straight(270)
            await db.turn(-90)
            await db.straight(132)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(394)
            await db.turn(-90)
            await db.straight(130)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLUE:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(512)
            await db.turn(-90)
            await db.straight(130)
            await db.turn(1)
            await moveRightArm(40, -270)

        elif colors[2] == Color.YELLOW:
            await db.turn(-1)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(632)
            await db.turn(-90)
            await db.straight(338)
            await db.turn(1)
            await moveRightArm(40, -270)

async def calibration2():
    db.settings(450, 650, 120, 250)
    if colors[2] == Color.YELLOW:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(810)
        await db.turn(-90)
        await db.straight(-400)
        
    if colors[2] == Color.BLUE:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(690)
        await db.turn(-90)
        await db.straight(-400)
        
    if colors[2] == Color.BLACK:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(560)
        await db.turn(-90)
        await db.straight(-400)
        
    if colors[2] == Color.GREEN:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(430)
        await db.turn(-90)
        await db.straight(-400)

    if colors[2] == Color.RED:
        await db.straight(-100)
        await db.turn(-90)
        await db.straight(300)
        await db.turn(-90)
        await db.straight(-400)
    db.reset()

async def theRestofUs():
    db.settings(750, 550, 200, 300)
    await multitask(
        async_wrapper(db.straight, 224),
        moveAttachmentArms(10, 140)
    )
    await db.turn(1)
    await db.turn(90)

    await multitask(
        async_wrapper(db.straight, 300),
        moveAttachmentArms(10, 158)
    )
    db.settings(200, 100, 300, 450)
    await db.straight(5)
    await db.turn(-1)
    await db.straight(220)

    await moveAttachmentArms(40, -450)
    await moveLeftArm(40, -10)

    #suprise rule
    #go to people
    db.settings(1000, 1000, 200, 300)
    await db.straight(-150)
    await db.turn(180)
    await db.straight(-450)
    db.reset()
    await db.straight(450)
    await db.turn(90)
    await db.straight(505)
    await db.turn(90)
    await db.straight(300)
    await moveLeftArm(40, 250)
    await db.straight(-600)
    await db.turn(180)
    await moveLeftArm(40, -450)
    await db.straight(-227)
    await db.turn(90)
    await db.straight(200)

    #jhj
    await db.straight(539)
    await db.turn(90)
    await db.straight(630)
    db.settings(120, 300, 120, 150)
    await db.straight(15)
    await moveAttachmentArms(40, 165)
    #put bandar in place
    db.settings(100, 100, 300, 300)
    await db.turn(-15)
    await db.turn(30)
    await db.turn(-15)
    #go to debris waala jaga
    db.settings(600, 600, 200, 150)
    await db.straight(-240)
    await db.turn(90)
    await db.straight(-1560)
    #drop black
    await db.turn(-90)
    await db.straight(-375)
    await db.straight(165)
    await db.turn(220)
    await moveRightArm(40, -300)
    #drop blue
    await db.straight(-155)
    await db.turn(-80)
    await db.straight(-420)
    await db.turn(40)
    await db.straight(280)
    await db.turn(130)
    await moveAttachmentArms(40, -270)
    #drop tower #2
    await db.straight(-80)
    await db.turn(-40)
    await db.straight(-600)
    await moveLeftArm(40, 360)
    await db.straight(-105)
    await db.turn(-90)
    await db.straight(195)
    await db.turn(90)
    await db.straight(100)
    await moveRightArm(40, 360)

async def dist(n):
    return umath.sqrt(n[0]**2 + n[1]**2 + n[2]**2)

async def colorScanning2():
    """
    Scans colors (of artifacts) until a list of 4, unique, valid (as defined by list validColors) is formed

    :return: The list of scanned colors
    :rtype: list[Color]

    """
    cleanedList = []
    Rf = (349, 87, 25)
    Rc = (352, 92, 94)
    Bf = (180, 0, 5)
    Bc = (180, 5, 14)
    Gf = (156, 64, 13)
    Gc = (154, 89, 46)
    Df = (210, 20, 10)
    Dc = (180, 17, 22)
    Yf = (37, 69, 45)
    Yc = (60, 37, 100)

    while True:
        h, s, v = await scanHSV()
        d = await dist((h, s, v))
        Rd = min(umath.fabs(d - await dist(Rc)), umath.fabs(d - await dist(Rf))) if Color.RED not in cleanedList else 10000
        Bd = min(umath.fabs(d - await dist(Bc)), umath.fabs(d - await dist(Bf))) if Color.BLUE not in cleanedList else 10000
        Gd = min(umath.fabs(d - await dist(Gc)), umath.fabs(d - await dist(Gf))) if Color.GREEN not in cleanedList else 10000
        Dd = min(umath.fabs(d - await dist(Dc)), umath.fabs(d - await dist(Df))) if Color.BLACK not in cleanedList else 10000
        Yd = min(umath.fabs(d - await dist(Yc)), umath.fabs(d - await dist(Yf))) if Color.YELLOW not in cleanedList else 10000
        if min(Rd, Bd, Gd, Dd, Yd) < 15:
            if Rd == min(Rd, Bd, Gd, Dd, Yd):
                cleanedList.append(Color.RED)
            elif Bd == min(Rd, Bd, Gd, Dd, Yd):
                cleanedList.append(Color.BLUE)
            elif Gd == min(Rd, Bd, Gd, Dd, Yd):
                cleanedList.append(Color.GREEN)
            elif Yd == min(Rd, Bd, Gd, Dd, Yd):
                cleanedList.append(Color.YELLOW)
            elif Dd == min(Rd, Bd, Gd, Dd, Yd):
                cleanedList.append(Color.BLACK)

        if len(cleanedList) == 4:
            print(cleanedList)
            break

        await wait(50)

    gc.collect()
    return cleanedList