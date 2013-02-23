#!/usr/bin/env python
#

import RPi.GPIO as GPIO

import joystick

# Wire config: (joy cable --> GPIO PIN)
_W_WHITE = 3
_W_GREEN = 5
_W_YELLOW = 7
_W_ORANGE = 8
_W_RED = 10

class VideopackJoy(joystick.Joystick)
    def __init__(self):
        joystick.Joystick.__init__(self)
        self.__opened = False

    # Configure proper GPIO ports
    #
    def open(self):
        if self.__opened:
            return
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(_W_WHITE,  GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(_W_GREEN,  GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(_W_YELLOW,  GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(_W_ORANGE,  GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(_W_RED,  GPIO.IN, pull_up_down = GPIO.PUD_UP)
        self.__opened = True

    # Clean-up GPIO
    #
    def close(self):
        if not self.__opened:
            return
        GPIO.cleanup()
        self.__opened = False

    # Return 2-axis and button state
    #
    @property
    def state(self):
        if not self.__opened:
            raise joystick.JoystickError('Joystick not opened!')
        x, y = 0, 0
        if not GPIO.input(_W_WHITE):
            y  = -1
        if not GPIO.input(_W_GREEN):
            x  = +1
        if not GPIO.input(_W_YELLOW):
            y = +1
        if not GPIO.input(_W_ORANGE):
            x = -1
        state = (x, y, not GPIO.input(_W_RED))
        return state


if __name__ == '__main__':
    joy = VideopackJoy()
    joy.open()
    while True:
        state = joy.state
        print state
        if state[2]:
            break
    joy.close()
