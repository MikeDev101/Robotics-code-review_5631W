# VEX EDR Python-Project with Competition Template
import sys
import vex


def autonomous():
    # Place autonomous code here
    pass

def driver():
    # You will usually have a while forever loop
    while True:
        # Driver control code here, setting motors based on joystick movements
        pass

# Do not adjust these next two lines
vex.run_autonomous(autonomous)
vex.run_driver(driver)

# Place additional code at the end which will run in both autonomous and driver modes
# (e.g. object avoidance logic)
