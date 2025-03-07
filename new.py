from codrone_edu.drone import Drone
from time import sleep

# Configuration Variables
throttle = 50
checkpoint_height_cm = 50 # (cm) height of the checkpoints (~7ft)
height_leeway = 0.15 # (meter) leeway in height measurements

trim_pitch = 0
trim_roll = 10

prefix = "Flight Control" #lolololol

dr = Drone()
dr.pair()

## Trimming ##
dr.set_trim(trim_roll, trim_pitch)

## Utility Functions ##
def reset():
    dr.reset_move_values(2)

def meter_to_cm(cm) -> float:
    return cm * 100

def cm_to_meter(meter) -> float:
    return meter / 100

def send_height_command_meters(meter):
    pos_data = dr.get_position_data()
    x = pos_data[1]
    y = pos_data[2]
    z = meter
    dr.sendControlPosition(x, y, z, 0.5, 0, 0)

def dprint(stuff):
    dr.controller_buzzer(400, 100)
    print("[" + prefix + "]", stuff)

##############
## Movement ##
##############

# take off, move to center of the checkpoints
dprint("Taking off and hovering...")
dr.takeoff()
dr.hover(1)

prefix = "Figure Eight"
dprint("Performing.")
dprint("Going to middle of the two checkpoints.")
reset()
dr.move_forward(3, "ft", 0.5)
sleep(2.5)

dprint("Going above the checkpoints.")
reset()
send_height_command_meters(2.13)
sleep(2.5)

dprint("Going past the checkpoints (above).")
reset()
dr.move_forward(4, "ft")
sleep(2.3)

dprint("Going down to allow going back in the middle of the two checkpoints.")
reset()
send_height_command_meters(-0.5)
sleep(2)

dprint("Going back to the middle of the two checkpoints.")
reset()
dr.move_backward(2.5, "ft")
sleep(2)

dprint("Going to the top of the two checkpoints.")
reset()
send_height_command_meters(2.13)
sleep(2)

dprint("Going in front of the first checkpoint.")
reset()
dr.move_backward(3.5, "ft")
sleep(2)

dprint("Done")

prefix = "2nd Mat"
dprint("Performing")

# Go above the checkpoints

dr.land()