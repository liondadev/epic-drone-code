from time import sleep

from codrone_edu.drone import Drone

dr = Drone()

while True:
    print(dr.get_movement_state(), dr.get_state_data())
    sleep(0.15)