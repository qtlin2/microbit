'''

Quick tips for Python:

1. Indentation is very important in Python. Make sure to use the correct number of spaces to indent blocks of code.

2. Remember to use colons (:) to mark the start of code blocks, such as in if/else statements and for loops.

3. Python is case sensitive, so make sure to use the correct capitalization for variable names and function names.

4. Always use quotes (either single or double) to enclose strings.

'''

'''

Preparation:

In this case, it needs extensions to run the source code.

Click 'Extensions' on left menu. Search 'kbit' and add it.

'''


# ======================== Use 'KBit' module to control Smart Car ===========================================

def car_move_forward(speed):
    kBit.run(KBitDir.RUN_FORWARD, speed)
    kBit.led(KBitColor.WHITE)


def car_move_back():
    kBit.run(KBitDir.RUN_BACK, 40)


def car_turn_right():
    kBit.run(KBitDir.TURN_RIGHT, 40)
    kBit.set_led(255, 255, 0)


def car_turn_left():
    kBit.run(KBitDir.TURN_LEFT, 30)
    kBit.set_led(255, 255, 0)  # yellow


def car_stop_move():
    kBit.car_stop()
    kBit.ledBrightness(100)
    kBit.set_led(0, 180, 255)


# ================ Use neopixel to control RGB Ring colors ================================================

def RGB_ring_bling():
    leds_number = 18
    ring = neopixel.create(DigitalPin.P8, leds_number, NeoPixelMode.RGB)
    ring.show_rainbow(1, 360)
    # ring.show()


# ========================== Main function ===============================================================

# Set safety distance ahead. More information about Smart Car parameters at the bottom of the file.
SAFE_DISTANCE = 12

def on_forever():

    # TODO test RGB ring
    # RGB_ring_bling()

    # Loop to make Smart Car to keep doing the same tasks: dectection and movement.
    while True:

        # Get the latest detect data
        front_distance = kBit.ultra()

        # Left/right avoidance sensor return number 0 or 1. Zero means obstacle is detected. One means no obstacle.
        leftside_detect = kBit.obstacle(KBitMotorObs.LEFT_SIDE)
        rightside_detect = kBit.obstacle(KBitMotorObs.RIGHT_SIDE)

        if front_distance > SAFE_DISTANCE and leftside_detect == 1 and rightside_detect == 1:
            if front_distance < SAFE_DISTANCE*2:
                # Slow down
                car_move_forward(speed=30)
            else:
                car_move_forward(speed=50)
            basic.pause(100)

        elif front_distance <= SAFE_DISTANCE:
            car_stop_move()
            car_turn_right()
            basic.pause(400)
            car_stop_move()

        elif leftside_detect == 0 and rightside_detect == 1:
            car_turn_right()
            basic.pause(400)
            car_stop_move()

        elif rightside_detect == 0:
            car_turn_left()
            basic.pause(300)
            car_stop_move()

# Execute 'on_forever' function
basic.forever(on_forever)





'''

Smart Car Parameters

    Wheels
        Diameter: 45mm
        Width: 19mm
        
    Motor    
        Wheel RPM: 180rpm

    Vehicle Speed: 4.05cm/100ms

    Ultrasonic sensor
        Distance = Sound speed x Time
        Sound speed = 340m/s = 340mm/ms


'''