import vex
import sys

#region config
BallLoader = vex.Motor(1)
BLM        = vex.Motor(2)
BRM        = vex.Motor(3, True)
FLM        = vex.Motor(4)
FRM        = vex.Motor(5, True)
Lift       = vex.Motor(6)
Ball       = vex.Motor(7)
FlipLeft   = vex.Motor(8)
FlipRight  = vex.Motor(9, True)
JS         = vex.Joystick()
#endregion config

# == moveInDirection parameter tips and tricks ==
# 1.0 = Forward
# 2.0 = Backwards

# 0.1 = Left
# 0.2 = Right

# 1.1 = Forwards left
# 1.2 = Forwards right

# 2.1 = Backwards left
# 2.2 = Backwards right

# Leave Direction 0 to stop all movement.

# For turning, have 3rd input set to the desired JS axis for turning. (except direct rotate left and direct rotate right)
# =====================

def moveInDirection(Direction, Power, Turn):
    if Direction == 1 or Direction == 1.1 or Direction == 1.2:
        if Direction == 1:
            FRM.run(-(Power))
            BLM.run(-(Power))
            FLM.run(-(Power))
            BRM.run(-(Power))
        elif Direction == 1.1:
            FRM.run(Power - Turn)
            BLM.run(Power + Turn)
            FLM.run(Power + Turn)
            BRM.run(Power - Turn)
        elif Direction == 1.2:
            FRM.run(Power + Turn)
            BLM.run(Power - Turn)
            FLM.run(Power - Turn)
            BRM.run(Power + Turn)
    elif Direction == 2 or Direction == 2.1 or Direction == 2.2:
        if Direction == 2:
            FRM.run(Power)
            BLM.run(Power)
            FLM.run(Power)
            BRM.run(Power)
        elif Direction == 2.1:
            FRM.run(-(Power) + Turn)
            BLM.run(-(Power) - Turn)
            FLM.run(-(Power) - Turn)
            BRM.run(-(Power) + Turn)
        elif Direction == 2.2:
            FRM.run(-(Power) - Turn)
            BLM.run(-(Power) + Turn)
            FLM.run(-(Power) + Turn)
            BRM.run(-(Power) - Turn)
    elif Direction == 0.1:
        FRM.run(-(Power))
        BLM.run(Power)
        FLM.run(-(Power))
        BRM.run(Power)
    elif Direction == 0.2:
        BLM.run(Power)
        FRM.run(-(Power))
        FLM.run(Power)
        BRM.run(-(Power))

def stopMotors():
    FRM.run(0)
    FLM.run(0)
    BLM.run(0)
    BRM.run(0)

def wait(time):
    sys.sleep(time)

# The moveInDirection function is best suited for autonomous.

# == WIRING DIAGRAM ==

# MAIN DRIVE MOTORS
# BLM - Back Left Motor, goes to pin 2
# BRM - Back Right Motor, goes to pin 3
# FLM - Front Left Motor, goes to pin 4
# FRM - Front Right Motor, goes to pin 5

# OTHER MOTORS
# Lift motors (Use 3-wire splitter) - goes to pin 6
# Launcher motors (Use 3-wire splitter) - goes to pin 7
# Loader motor - goes to pin 1

# FLIPPER MOTORS
# Flipper Left - pin 8
# Flipper Right - pin 9

# MOTOR, LIFT, AND BALL OUTPUTS GO RED WIRE TO RED WIRE, BLACK WIRE TO BLACK WIRE!!!

def driver():
    JS.set_deadband(15)
    pow_control = 0 #virtural toggle switch, do NOT put into main loop!
    while True:
        # Resetting these variables...
        BLM_power = 0
        BRM_power = 0
        FLM_power = 0
        FRM_power = 0
        Lift_power = 0
        Ball_power = 0
        Flip_power = 0
        
        # Control/Input variables...
        d_move = JS.axis3()
        d_steer = JS.axis1()
        d_lift_up = JS.b5up()
        d_lift_down = JS.b5down()
        d_flip_up = JS.b6up()
        d_flip_down = JS.b7down()
        Ball_Launcher_Power = JS.b7down()
        
        # axis1: Arcade drive (Main movement)
        if d_move != 0 or d_steer != 0:
            BLM_power = d_move + d_steer
            FLM_power = d_move + d_steer
        if d_move != 0 or d_steer != 0:
            BRM_power = d_move - d_steer
            FRM_power = d_move - d_steer
        
        # button5: Pushbutton control (Lift)
        if d_lift_up == True:
            Lift_power = 100
        elif d_lift_down == True:
            Lift_power = -100
        
        #button6: Pushbutton control (Flipper)
        if d_flip_up == True:
            Flip_power = 100
        elif d_flip_down == True:
            Flip_power = -100
        
        # button7down: Toggle pushbutton control (Ball launcher)
        if Ball_Launcher_Power == True:
            if pow_control == 0:
                pow_control = 2
            if pow_control == 1:
                pow_control = -1
        else:
            if pow_control == 2:
                pow_control = 1
            if pow_control == -1:
                pow_control = 0
        if pow_control == 2 or pow_control == 1:
            Ball_power = 100
        
        # Motors being ran with variables, 0 to 100.
        Lift.run(Lift_power)
        Ball.run(Ball_power)
        FlipLeft.run(Flip_power)
        FlipRight.run(Flip_power)
        BallLoader.run(Ball_power)
        BLM.run(BLM_power)
        BRM.run(BRM_power)
        FLM.run(FLM_power)
        FRM.run(FRM_power)

def autonomous(): #to be finished.
    wait(0.5)
    moveInDirection(1.0, 100, 0)
    wait(1)
    stopMotors()
    wait(1)
    moveInDirection(2.0, 100, 0)
    wait(1)
    stopMotors()

# main thread!
#autonomous() #currently disabled due to being unfinished.
driver()
