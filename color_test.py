from codrone_edu.drone import Drone
import time
import math

dr = Drone()
dr.pair()

colors = ["blue", "red", "green"]
data_folder_name = "color_" + str(math.ceil(time.time()))
def calibrate_color_sensor(dr: Drone):
    # Handle calibrating each color in sequence
    for color in colors:
        data = []
        samples = 500

        for i in range(2):
            print("Sample: ", i+1)
            next = input("Press enter to calibrate " + color)

            # Take the samples, with a progress bar
            print("0% ", end="")
            for j in range(samples):
                color_data = dr.get_color_data()[0:9]
                data.append(color_data)
                time.sleep(0.005)
                if j % 10 == 0:
                    print("-", end="")
            print(" 100%")

        dr.new_color_data(color, data, data_folder_name)
    print("Finished Callibration!")


def detect_color(dr: Drone):
    dr.load_color_data("color_data")

    time.sleep(0.15)
    color_data = dr.get_color_data()
    color = dr.predict_colors(color_data)
    print(color)
    time.sleep(0.15)


detect_color(dr)
# calibrate_color_sensor(dr)

