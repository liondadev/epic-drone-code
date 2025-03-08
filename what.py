import string
import time

from codrone_edu.drone import *

f = open(str(time.time_ns())+".txt", "w")

def log_action(type):
    global f
    f.write("action\t"+type+"\n")
    print("Action: " + type)

def log_flight(throttle, pitch, yaw, roll):
    global f
    f.write("flight\t"+str(throttle)+"\t"+str(pitch)+"\t"+str(yaw)+"\t"+str(roll)+"\n")
    print("Flight:" + str(throttle) + "\t" + str(pitch) + "\t" + str(yaw) + "\t" + str(roll))

def run_through_actions(sheet: str):
    lines = sheet.split('\n')

    for line in lines:
        bits = line.split('\t')
        type = bits[0]
        if type == "action":
            action = bits[1]
            if action == "takeoff":
                drone.takeoff()
            elif action == "land":
                drone.land()
        elif type == "flight":
            throttle = bits[1]
            pitch = bits[2]
            yaw = bits[3]
            roll = bits[4]

            drone.set_throttle(throttle)
            drone.set_pitch(pitch)
            drone.set_yaw(yaw)
            drone.set_roll(roll)
            drone.move(0.15)

tookoff = False

def check_buttons():
    global tookoff

    if drone.l1_pressed():
        if tookoff:
            log_action("land")
            drone.land()
            tookoff = False
        else:
            log_action("takeoff")
            drone.takeoff()
            tookoff = True
    elif drone.l2_pressed():
        log_action("land")
        drone.land()
    elif drone.r1_pressed():
        log_action("flip")
        drone.flip()


drone = Drone()
drone.pair()
drone.set_trim(10, 0)

delay = 0.15
last = 0
def do_recording():
    global delay
    global last
    while True:
        check_buttons()
        if last + delay < time.time():
            print(last, delay, time.time())
            continue
        last = time.time()
        pitch = drone.get_right_joystick_y()
        roll = drone.get_right_joystick_x()
        throttle = drone.get_left_joystick_y()
        yaw = drone.get_left_joystick_x() * -1

        if pitch > 60:
            pitch = 60
        if pitch < -60:
            pitch = -60
        if roll > 60:
            roll = 60
        if roll < -60:
            roll = -60
        if throttle > 60:
            throttle = 60
        if throttle < -60:
            throttle = -60
        if yaw > 60:
            yaw = 60
        if yaw < -60:
            yaw = -60

        drone.set_pitch(pitch)
        drone.set_roll(roll)
        drone.set_throttle(throttle)
        drone.set_yaw(yaw)
        drone.move(0.15)
        log_flight(throttle, pitch, yaw, roll)


print("1 - Record... Filename - Playback")
val = input("> ")

if val == "1":
    do_recording()
else:
    file = open(val, "r")
    run_through_actions(file.read())