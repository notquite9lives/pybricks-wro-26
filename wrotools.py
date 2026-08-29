# WRO TOOLS FILE
# version: 1.2
# date: 15/6/2026


import gc

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
validColors = [Color.RED, Color.BLUE, Color.GREEN, Color.BLACK, Color.YELLOW]


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

    # picking up the tower
    db.settings(350,700,120,300)
    await db.straight(275)
    await db.turn(-1)
    await db.turn(-90)
    db.stop()
    db.distance_control.pid(30000, 0, 9000, 5, 10)
    db.settings(260,400,150,300)
    await db.straight(202)
    db.settings(150,300,120,300)
    await db.straight(120)
    db.settings(400, 650, 150, 300)
    await moveAttachmentArms(40, -390) 

    # placing first tower
    db.settings(500,650,150,300)
    await db.straight(-65)
    await db.turn(90)
    await db.straight(503)
    await moveUntilReflection(20, 45, 100) #fill distance properly
    db.settings(240, 700, 120, 250)
    await db.straight(440)
    await moveAttachmentArms(40,270)
    await db.straight(-220)
    db.settings(280, 800, 160, 300)

    # calibration
    await db.turn(90)
    await db.straight(-300)


    # placing second tower
    db.settings(450,600,150,300)
    await moveUntilReflection(20, 40, 100) # fill distance properly
    await multitask(async_wrapper(db.straight, 320), moveAttachmentArms(40, -270))
    db.settings(240, 700, 120, 250)
    await db.turn(-90)
    await db.straight(218)
    await moveAttachmentArms(38,270)
    await db.straight(-100)
    db.settings(280, 800, 160, 300)
    await moveRightArm(38, 1)

async def colorScanning():
    """
    Scans colors (of artifacts) until a list of 4, unique, valid (as defined by list validColors) is formed

    :return: The list of scanned colors
    :rtype: list[Color]

    """
    cleanedList = []
    black_debounce_count = 0

    while True:
        currentReflection = await color_sensor2.reflection()
        currentScan = await color_sensor2.color()
        h, s, v = await scanHSV()

        finalDebounce = 3
        if 235 <= h <= 245:
            black_debounce_count += 1
            if black_debounce_count >= finalDebounce:
                if Color.BLACK not in cleanedList:
                    cleanedList.append(Color.BLACK)
                    print(Color.BLACK)
        elif h < 20 or v == 0 or s == 0:
            black_debounce_count = 0
        else:
            if 35 <= h <= 45:
                cleanedList.append(Color.YELLOW)
                print(Color.YELLOW)
            elif 345 <= h <= 355:
                cleanedList.append(Color.RED)
                print(Color.RED)
            elif 155 <= h <= 165:
                cleanedList.append(Color.GREEN)
                print(Color.GREEN)
            elif 210 <= h <= 220:
                cleanedList.append(Color.BLUE)
                print(Color.BLUE)

        if len(cleanedList) == 4:
            print(cleanedList)
            break

        await wait(50)

    return cleanedList


    gc.collect()

async def correction(target_heading):
    db.settings(200, 700, 100, 200)

    # 1. Calculate raw difference
    error = hub.imu.heading() - target_heading

    # 2. Wrap error into range [-180, 180] for the shortest path
    shortest_error = (error + 180) % 360 - 180

    # 3. Turn to eliminate the error
    if not (-0.5 < shortest_error < 0.5):
        await db.turn(-shortest_error)

    db.settings(260, 600, 160, 300)

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
    await db.straight(265)
    await db.turn(90)
    await db.straight(190)
    await moveAttachmentArms(30, 250)
    await db.turn(180)

async def iForgot():
    global colors
    if colors[3] == Color.GREEN:
        await db.straight(300)
        await db.turn(-90)
        await db.straight(58)
        await db.turn(90)
        await db.straight(336)
    else:
        await db.straight(600)

async def firstPairArtifact():
    if colors[3] == Color.YELLOW:

        await db.turn(3)
        await db.turn(90)
        await db.turn(3)
        await db.straight(400)
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
        await db.straight(220)
        await db.turn(-2)
        await db.turn(-90)
        await db.straight(182)
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
        await db.straight(92)
        await db.turn(-90)
        await db.straight(172)
        await moveLeftArm(40,-270)

        if colors[2] == Color.GREEN:
            await moveRightArm(40, -270)

        elif colors[2] == Color.RED:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(-90)
            await db.straight(143)
            await db.turn(90)
            await db.straight(143)
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
            await db.straight(376)
            await db.turn(-90)
            await db.straight(350)
            await db.turn(1)
            await moveRightArm(40, -270)

    elif colors[3] == Color.GREEN:

        await db.turn(6)
        await db.straight(140)
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
            await db.straight(-140)
            await db.turn(90)
            await db.straight(380)
            await db.turn(-90)
            await db.straight(158)
            await moveRightArm(40, -270)

        elif colors[2] == Color.YELLOW:
            await db.turn(-2)
            await db.straight(-350)
            await db.turn(90)
            await db.straight(503)
            await db.turn(-90)
            await db.straight(356)
            await db.turn(1)
            await moveRightArm(40, -270)
    
    elif colors[3] == Color.RED:

        await db.turn(-87)
        await db.straight(180)
        await db.turn(90)
        await db.straight(165)
        await moveLeftArm(40,-270)

        if colors[2] == Color.GREEN:
            await db.turn(-1)
            await db.straight(-130)
            await db.turn(90)
            await db.straight(245)
            await db.turn(-90)
            await db.straight(137)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLACK:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(377)
            await db.turn(-90)
            await db.straight(140)
            await moveRightArm(40, -270)

        elif colors[2] == Color.BLUE:
            await db.turn(-1)
            await db.straight(-140)
            await db.turn(90)
            await db.straight(502)
            await db.turn(-90)
            await db.straight(140)
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

async def calibration1():

    if colors[2] == Color.YELLOW:
        await db.straight(-300)
        await db.turn(-90)
        await db.straight(535)
        await db.turn(90)
        await db.straight(-1000)

    elif colors[2] == Color.BLUE:
        await db.straight(-300)
        await db.turn(-90)
        await db.straight(390)
        await db.turn(90)
        await db.straight(-1000)

    elif colors[2] == Color.BLACK:
        await db.straight(-300)
        await db.turn(-90)
        await db.straight(240)
        await db.turn(90)
        await db.straight(-1000)

    elif colors[2] == Color.GREEN:
        await db.straight(-300)
        await db.turn(-90)
        await db.straight(162)
        await db.turn(90)
        await db.straight(-1000)

    else:
        await db.straight(-1000)

    db.stop()
    db.reset()
    wait(100)

async def artifactPickup2():

    await db.straight(300)
    await db.turn(90)
    if colors != Color.RED:
        await db.straight(427)
    else:
        await db.straight(244)
    await db.turn(93)
    db.settings(140, 650, 120, 250)
    await db.straight(270)
    await moveAttachmentArms(40, 270)
    await db.straight(-100)
    await db.turn(180)
    await db.straight(500)
    db.settings(240, 650, 120, 250)

async def secondPairArtifact():

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

async def calibration2():

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

async def theRestofUs():
    await multitask(
        async_wrapper(db.straight, 231),
        moveAttachmentArms(10, 175)
    )
    await db.turn(90)

    await multitask(
        async_wrapper(db.straight, 250),
        moveAttachmentArms(10, 165)
    )

    await wait(100)
    db.settings(200, 200, 80, 150)
    await db.straight(260)    

    await moveAttachmentArms(40, -450)
    await moveLeftArm(40, 10)

    await db.straight(-319)
    await db.turn(-90)
    await db.straight(645)
    db.settings(200, 200, 60, 150)
    await moveAttachmentArms(40, 165)
    await db.turn(-15)
    await db.turn(30)
    await db.turn(-15)
    db.settings(600, 200, 200, 150)
    await db.straight(-240)
    await db.turn(90)
    await db.straight(-1560)
    await db.turn(-90)
    await db.straight(-375)
    await db.straight(160)
    await db.turn(220)
    await moveRightArm(40, -300)
    await db.straight(-150)
    await db.turn(-40)
    await db.straight(-420)
    await db.straight(280)
    await db.turn(130)
    await moveAttachmentArms(40, -270)
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
    
