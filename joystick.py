#!/usr/bin/env python
#
# RaspberryJoy
#
# Released under GPLv3
#
#

class Joystick(object):
    def __init__(self):
        pass

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    @property
    def state(self):
        raise NotImplementedError()


class JoystickError(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return 'Joystick Error: %s' % self.__msg
