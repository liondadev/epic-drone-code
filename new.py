from codrone_edu.drone import Drone
from time import sleep

# Color Detection
color_dataset = "color_data"

# Configuration Variables
throttle = 50
height_leeway = 0.15 # (meter) leeway in height measurements

trim_pitch = 0
trim_roll = -10

prefix = "Flight Control" #lolololol

dr = Drone()
dr.pair()

## Trimming ##
dr.set_trim(trim_roll, trim_pitch)

## Color Detection ##
dr.load_color_data(color_dataset)

def detect_color():
    sleep(0.15)
    color_data = dr.get_color_data()
    color = dr.predict_colors(color_data)
    print(color)
    sleep(0.15)

## Utility Functions ##
def reset():
    dr.set_pitch(0)
    dr.set_yaw(0)
    dr.set_roll(0)

def meter_to_cm(cm) -> float:
    return cm * 100

def cm_to_meter(meter) -> float:
    return meter / 100

def send_height_command_meters(meter):
    dr.get_position_data()
    x = 0
    y = 0
    z = meter
    dr.sendControlPosition(x, y, z, 0.5, 0, 0)

def dprint(stuff):
    print("[" + prefix + "]", stuff)

def move_forward(*args):
    dprint("Moving Forward")
    dr.move_forward(*args)

def move_right(*args):
    dprint("Moving Right")
    dr.move_right(*args)

def move_left(*args):
    dprint("Moving Left")
    dr.move_left(*args)

def move_backward(*args):
    dprint("Moving Backward")
    dr.move_backward(*args)

##############
## Movement ##
##############

dprint("Detecting Color...")
detect_color()

dprint("Taking off and hovering...")
dr.takeoff()
dr.hover(1)

prefix = "Figure Eight"
dprint("== Performing...")
dprint("Going to middle of the two checkpoints.")
reset()
move_forward(3.5, "ft", 0.5)
sleep(1.75)

dprint("Going above the checkpoints.")
reset()
dr.get_position_data(0.25)
send_height_command_meters(2.13)
sleep(2.5)

dprint("Going past the checkpoints (above).")
reset()
dr.get_position_data(0.25)
move_forward(3, "ft")
sleep(2.3)

dprint("Going down to allow going back in the middle of the two checkpoints.")
reset()
dr.get_position_data(0.25)
send_height_command_meters(-.75)
dr.move(2)

dprint("Going back to the middle of the two checkpoints.")
reset()
dr.get_position_data(0.25)
move_backward(2.5, "ft", 1.5)
sleep(2)

dprint("Going to the top of the two checkpoints.")
reset()
dr.get_position_data(0.25)
send_height_command_meters(2.13)
sleep(2)

dprint("Going in front of the first checkpoint.")
reset()
dr.get_position_data(0.25)
move_backward(3.5, "ft")
sleep(2)

dprint("Going down to be in front of the first checkpoint.")
reset()
dr.get_position_data(0.25)
send_height_command_meters(-1)
sleep(3)

dprint("Going back through the course to get to the second mat.")
reset()
dr.get_position_data(0.25)
dr.reset_move(2)
move_forward(11-2.13-1, "ft")
sleep(1.75)

dprint("Correcting a bit...")
reset()
dr.get_position_data(0.25)
dr.reset_move(2)
move_right(0.5, "ft")

dprint("Landing")
dr.land()
dr.reset_move_values(2)

dprint("== Done!")

dprint("Detecting Color...")
detect_color()

################
## SECOND MAT ##
################

# repair to fix relativity lol
dr.disconnect()
dr.close()

dr = Drone()
dr.pair()

prefix = "Second Loop"
dprint("== Performing...")

dr.takeoff()
dr.hover(1)

dprint("Going to meet first keyhole.")
reset()
dr.get_position_data(0.25)
send_height_command_meters(1)
sleep(2)

dprint("Going through first keyhole")
reset()
dr.get_position_data(0.25)
dr.move_right(6, "ft")
sleep(2)

dprint("Threading the drone sized needle!!!!")
reset()
dr.get_position_data(0.25)
send_height_command_meters(-0.25)
sleep(1)

dprint("Going through second keyhole")
reset()
dr.get_position_data(0.25)
move_backward(4.25, "ft")
sleep(2)

dprint("Correcting")
reset()
dr.get_position_data(0.25)
dr.move_left(0.5, "ft")
sleep(0.5)

dprint("LAND NOW!!")
dr.land()

dprint("== Done!")

prefix = "Flight Control"
dprint("Done :)")
