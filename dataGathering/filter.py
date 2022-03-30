import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

dirname = os.path.dirname(__file__)
dirdata = os.path.abspath(os.path.join(dirname, "out", "1647867608"))
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
            out.append(m[7])
    return out


def getSpeed(lap, timestamps):
    speed = []
    time = []
    array = getNumpy(car_file)
    # timestamps = getTimeStamps(getNumpy(lap_file), lap)
    for m in array:
        if m[3] in timestamps:
            speed.append(m[0])
            time.append(m[3])
    return speed


def getLapPosition(lap, timestamps):
    pos = []
    time = []
    array = getNumpy(lap_file)
    # timestamps = getTimeStamps(getNumpy(lap_file), lap)
    for m in array:
        if m[7] in timestamps:
            pos.append(m[0])
            time.append(m[7])
    return pos, time


def getGasInput(lap, timestamps):
    gas = []
    time = []
    array = getNumpy(input_file)
    # timestamps = getTimeStamps(getNumpy(lap_file), lap)
    for m in array:
        if m[3] in timestamps:
            gas.append(m[0])
            time.append(m[3])
    return gas


def getBrakeInput(timestamps):
    brake = []
    time = []
    array = getNumpy(input_file)
    # timestamps = getTimeStamps(getNumpy(lap_file), lap)
    for m in array:
        if m[3] in timestamps:
            brake.append(m[1])
            time.append(m[3])
    return brake


def getrpm(lap, timestamps):
    rpm = []
    time = []
    array = getNumpy(car_file)
    # timestamps = getTimeStamps(getNumpy(lap_file), lap)
    for m in array:
        if m[3] in timestamps:
            rpm.append(m[1])
            time.append(m[3])
    return rpm


def getGear(lap, timestamps):
    gear = []
    time = []
    array = getNumpy(car_file)
    # timestamps = getTimeStamps(getNumpy(lap_file), lap)
    for m in array:
        if m[3] in timestamps:
            gear.append(m[2])
            time.append(m[3])
    return gear


def createLapReport(lap):
    timestamps = getTimeStamps(getNumpy(lap_file), lap)
    speed = getSpeed(lap, timestamps)
    pos, rel_time = getLapPosition(lap, timestamps)
    gas = getGasInput(lap, timestamps)
    brake = getBrakeInput(timestamps)
    rpm = getrpm(lap, timestamps)
    gear = getGear(lap, timestamps)

    fig, axs = plt.subplots(5, 1, sharex=True)
    fig.subplots_adjust(hspace=0.05)

    axs[0].plot(rel_time, speed)
    axs[0].set_yticks(np.arange(0, 300, 100))
    axs[0].set_ylabel("speed")
    axs[0].set_ylim(0, 300)
    axs[1].plot(rel_time, rpm)
    axs[1].set_ylabel("rpm")
    axs[2].plot(rel_time, gas)
    axs[2].set_ylabel("gas")
    axs[3].plot(rel_time, brake)
    axs[3].set_ylabel("brake")
    axs[4].plot(rel_time, gear)
    axs[4].set_ylabel("gear")
    plt.show()


def main():
    createLapReport(1)


if __name__ == "__main__":
    main()
