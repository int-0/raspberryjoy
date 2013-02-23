Raspberry PI Joystick Drivers for python
========================================

Implementation of quick & dirty joystick drivers for Raspberry PI. These joysticks can be connected using GPIO port. Current joysticks are supported:

- Videopack joystick (first version, without external connector)


How to use
==========

For now, API is very easy:

```python
 joy = VideopackJoy()
 joy.open()
 state = joy.state
 joy.close()
```

How to connect
==============

Driver sourcecode includes little schema about wiring. No additional components (like resistors) are needed, just connect wires with pins... very easy!
