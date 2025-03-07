from codrone_edu.drone import *
import time

from scipy.constants import centi


def clearmove(dr: Drone):
    dr.set_pitch(0)
    dr.set_yaw(0)
    dr.set_throttle(0)

# init drone
dr = Drone()
dr.connect() # open serial conn
dr.set_trim(10, 0) # stop drone from flying to the right for no flipping reason :(


def partone(dr: Drone):
    # todo: color detection

    # Takeoff and hover above the green line thing
    dr.takeoff()
    dr.hover(0.5)

    # Go through the first thing and get ready for a figure eight
    clearmove(dr)
    dr.set_pitch(50)
    dr.set_throttle(30)
    dr.move(1.5)

    # move above the two gates
    clearmove(dr)
    dr.set_throttle(50)
    dr.move(1)

    # past the second gate
    dr.set_pitch(50)
    dr.set_throttle(20)
    dr.move(1.25)

    # move below the second gate
    clearmove(dr)
    dr.set_throttle(-80)
    dr.move(2.25)

    # back to middle
    clearmove(dr)
    dr.set_pitch(-60)
    dr.set_throttle(40)
    dr.move(1)

    # up above the first gate
    clearmove(dr)
    dr.set_throttle(50)
    dr.move(1)

    # back in front of the first gate
    clearmove(dr)
    dr.set_pitch(-95)
    dr.set_throttle(40)
    dr.move(0.75)

    # move the drone down to middle front of first gate
    clearmove(dr)
    dr.set_throttle(-80)
    dr.move(3)

    # skip keyhold - move to top of landing pad
    clearmove(dr)
    dr.set_pitch(100)
    dr.set_throttle(50)
    dr.move(1.9)

    # move forward and right a bit to land on second pad
    clearmove(dr)
    dr.set_roll(50)
    dr.set_throttle(60)
    dr.move(0.3)

    # land on mat to do color detection
    dr.land()
    # todo: color detection

    # take off and go through keyhole rings

def recovery(dr: Drone):
    # Finish detecting the color of the second color mat
    # and fly through the two hoop thingies
    dr.takeoff() # sleeps
    clearmove(dr)

    # fly up to meet the first hoop thing
    dr.set_throttle(40)
    dr.move(0.75)

    # correct for moving to the side for no fucking reason

    # go through the first hoop thing
    clearmove(dr)
    dr.set_roll(50)
    dr.set_throttle(30)
    dr.move(1.5)
    clearmove(dr)

    # move down a bit to correct for the second hoop
    clearmove(dr)
    dr.set_throttle(-60)
    dr.set_roll(30)
    dr.move(1.75)

    # go up a tiny bit
    clearmove(dr)
    dr.set_throttle(50)
    dr.move(0.25)

    # move through the second hoop
    clearmove(dr)
    dr.set_pitch(-75)
    dr.set_throttle(20)
    dr.move(1.75)

    # correct a bit for movement
    clearmove(dr)
    dr.set_throttle(30)
    dr.set_roll(-50)
    dr.move(0.5)

partone(dr)

dr.land() # land da drone
dr.close() # close serial conn