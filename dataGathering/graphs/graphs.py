import matplotlib.pyplot as plt
import json


def lapTimestamps():
    timestamps = []
    last_b = 0
    last_e = 0
    last = "e"
    prevline = ""

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/lap.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            strline = line.replace("\'", "\"")
            jline = json.loads(strline)
            if jline["lap_position"] < 0.0002 and jline["timestamp"] - last_b > 10000:
                if last == "b":
                    timestamps.append(prevline["timestamp"])
                    last_e = jline["timestamp"]
                else:
                    timestamps.append(jline["timestamp"])
                    last_b = jline["timestamp"]
                    last = "b"
            if jline["lap_position"] > 0.9999 and jline["timestamp"] - last_e > 10000:
                if not last == "e":
                    timestamps.append(jline["timestamp"])
                    last_e = jline["timestamp"]
                    last = "e"
            prevline = jline
    f.close()
    print(str(timestamps))
    return timestamps


# def isolateLaps():
#     os.makedirs('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/input/lap')
#
#     tss = lapTimestamps()
#
#     with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/input.txt', 'r+') as file:
#         lines = file.readlines()
#         for l in lines:
#             strline = l.replace("\'", "\"")
#             jline = json.loads(strline)

def plotSteerInput():
    steerInput = []
    time = []
    tss = lapTimestamps()

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/input.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            strline = l.replace("\'", "\"")
            jline = json.loads(strline)
            if tss[5] >= jline["timestamp"] >= tss[4]:
                steerInput.append(jline["steering"])
    file.close()

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/lap.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            strline = l.replace("\'", "\"")
            jline = json.loads(strline)
            if tss[5] >= jline["timestamp"] >= tss[4]:
                time.append(jline["current"] / 1000)
    file.close()
    plt.plot(time, steerInput)
    plt.show()

def plotGasInput():
    gasInput = []
    time = []
    tss = lapTimestamps()
    print(str(tss))

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/input.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            strline = l.replace("\'", "\"")
            jline = json.loads(strline)
            if tss[5] >= jline["timestamp"] >= tss[4]:
                gasInput.append(jline["gas"])
                # time.append(jline["timestamp"])
    file.close()

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/lap.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            strline = l.replace("\'", "\"")
            jline = json.loads(strline)
            if tss[5] >= jline["timestamp"] >= tss[4]:
                time.append(jline["lap_position"])
    file.close()
    print(str(gasInput))
    print(str(time))
    plt.plot(time, gasInput)
    plt.show()

def plotSpeed():
    speed = []
    time = []
    tss = lapTimestamps()

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/car.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            strline = l.replace("\'", "\"")
            jline = json.loads(strline)
            if tss[5] >= jline["timestamp"] >= tss[4]:
                speed.append(jline["car_speed"])
        file.close()
    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/TestData/lap.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            strline = l.replace("\'", "\"")
            jline = json.loads(strline)
            if tss[5] >= jline["timestamp"] >= tss[4]:
                time.append(jline["lap_position"])
        file.close()
        print(str(speed))
        print(str(time))
    plt.plot(time, speed)
    plt.xlabel("Lap progress")
    plt.ylabel("Speed in km/h")
    plt.show()


def main():
    plotSteerInput()


if __name__ == "__main__":
    main()
