#import evdev
from evdev import InputDevice, categorize, ecodes

# creates object 'gamepad' to store the data
# you can call it whatever you like
gamepad = InputDevice(
    '/dev/input/by-id/usb-ShanWan_XBOX_360_For_Windows-event-joystick')

# button code variables (change to suit your device)
aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

l1Btn = 310
l2Btn = 2 # event.value <= 255
l3Btn = 317
r1Btn = 311 
r2Btn = 5
r3Btn = 318

startBtn = 315
selectBtn = 314

thumbstick1X = 0  # -32768 <= event.value <= 32767
thumbstick1Y = 1
thumbstick2X = 3
thumbstick2Y = 4

dPadX = 16  # -1 <= event.value <= 1
dPadY = 17

# prints out device info at start
print(gamepad)

# loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    # print(event)
    if event.type is ecodes.EV_KEY or event.type is 3:
        if event.value is not 0:
            if event.code == yBtn:
                print("Y")
            elif event.code == bBtn:
                print("B")
            elif event.code == aBtn:
                print("A")
            elif event.code == xBtn:
                print("X")

            elif event.code == l1Btn:
                print("L1")
            elif event.code == l2Btn:
                print("L2 %d" % event.value)
            elif event.code == l3Btn:
                print("L3")
            elif event.code == r1Btn:
                print("R1")
            elif event.code == r2Btn:
                print("R2 %d" % event.value)
            elif event.code == r3Btn:
                print("R3")

            elif event.code == startBtn:
                print("start")
            elif event.code == selectBtn:
                print("select")

            elif event.code == thumbstick1X:
                print("thumbstick1X %d" % event.value)
            elif event.code == thumbstick1Y:
                print("thumbstick1Y %d" % event.value)
            elif event.code == thumbstick2X:
                print("thumbstick2X %d" % event.value)
            elif event.code == thumbstick2Y:
                print("thumbstick2Y %d" % event.value)

            elif event.code == dPadX:
                print("dPadX %d" % event.value)
            elif event.code == dPadY:
                print("dPadY %d" % event.value)
