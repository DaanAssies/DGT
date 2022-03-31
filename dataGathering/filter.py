import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
from time import time

dirname = os.path.dirname(__file__)
dirdata = os.path.abspath(os.path.join(dirname, "out", "1648717625c"))
lap_file = os.path.join(dirdata, "lap.csv")
car_file = os.path.join(dirdata, "car.csv")
input_file = os.path.join(dirdata, "input.csv")
pickledir = os.path.abspath(os.path.join(dirname, "1648490239p"))
picklefile = os.path.join(pickledir, "input.pkl")


def getNumpy(file):
    with open(os.path.join(dirdata, file), 'r'):
        out = np.genfromtxt(os.path.join(dirdata, file), delimiter=',', skip_header=1)
    return out


def unpickle(file):
    print(file)
    f = open(file, 'rb')
    unpickler = pickle.Unpickler(f)
    res = []
    while True:
        try:
            x = unpickler.load()
            res.append(x)
        except EOFError:
            return res


# Function to get the timestamps where laps get started and where they end. Includes the lap count
def getTimeStamps(array, lap):
    out = []
    for m in array:
        if (m[1]) == lap:
            out.append(m[10])
    print(out)
    return out


def getSpeed(timestamps):
    speed = []
    array = getNumpy(car_file)
    for m in array:
        if m[4] in timestamps:
            speed.append(m[0])
    return speed


def getLapPosition(timestamps):
    pos = []
    array = getNumpy(lap_file)
    for m in array:
        if m[7] in timestamps:
            pos.append(m[0])
    return pos


def getGasInput(timestamps):
    gas = []
    array = getNumpy(input_file)
    for m in array:
        if m[3] in timestamps:
            gas.append(m[0])
    return gas


def getBrakeInput(timestamps):
    brake = []
    array = getNumpy(input_file)
    for m in array:
        if m[3] in timestamps:
            brake.append(m[1])
    return brake


def getrpm(timestamps):
    rpm = []
    array = getNumpy(car_file)
    for m in array:
        if m[4] in timestamps:
            rpm.append(m[1])
    return rpm


def getGear(timestamps):
    gear = []
    array = getNumpy(car_file)
    for m in array:
        if m[4] in timestamps:
            gear.append(m[2])
    return gear


def createLapReport(lap):
    timestamps = getTimeStamps(getNumpy(lap_file), lap)
    speed = getSpeed(timestamps)
    gas = getGasInput(timestamps)
    brake = getBrakeInput(timestamps)
    rpm = getrpm(timestamps)
    gear = getGear(timestamps)

    fig, axs = plt.subplots(5, 1, sharex=True)
    fig.subplots_adjust(hspace=0.05)

    axs[0].plot(timestamps, speed)
    axs[0].set_yticks(np.arange(0, 300, 100))
    axs[0].set_ylabel("speed")
    axs[0].set_ylim(0, 300)
    axs[1].plot(timestamps, rpm)
    axs[1].set_ylabel("rpm")
    axs[2].plot(timestamps, gas)
    axs[2].set_ylabel("gas")
    axs[3].plot(timestamps, brake)
    axs[3].set_ylabel("brake")
    axs[4].plot(timestamps, gear)
    axs[4].set_ylabel("gear")
    plt.show()


def main():
    start_time = time()
    createLapReport(1)
    print("The graph took ", time() - start_time, " seconds to generate")


if __name__ == "__main__":
    main()
