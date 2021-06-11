import json
from itertools import islice

last_ts = 0
last_flag = 0

def main():
    return

def convert():
    global last_ts

    inputInfo = []
    carInfo = []
    lapInfo = []

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/output.txt', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            strline = line.replace("\'", "\"")
            jline = json.loads(strline)
            if jline["timestamp"] >= last_ts:
                flag = jline["flag"]
                if flag == 0:
                    inputInfo.append(line)
                if flag == 1:
                    carInfo.append(line)
                if flag == 2:
                    lapInfo.append(line)
            last_ts = jline["timestamp"]
    f.close()

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/input.txt', 'w') as output:
        output.write(''.join(inputInfo))
        # output.write('\n')

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/car.txt', 'w') as output:
        output.write(''.join(carInfo))

    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/lap.txt', 'w') as output:
        output.write(''.join(lapInfo))


def move():
    global last_ts, last_flag
    print(str(last_ts))
    with open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/py_log.txt') as logs:
        for line in islice(logs, 2, None):
            strline = line.replace("\'", "\"")
            jline = json.loads(strline)
            if last_flag == 2:
                if jline["timestamp"] > last_ts:
                    last_flag = jline["flag"]
                    output = open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/output.txt', 'a')
                    output.write(''.join(line))
                    last_ts = jline["timestamp"]
            elif jline["timestamp"] >= last_ts:
                last_flag = jline["flag"]
                output = open('C:/Users/daana/OneDrive/Documenten/Assetto Corsa/logs/output.txt', 'a')
                output.write(''.join(line))
                last_ts = jline["timestamp"]





if __name__ == "__main__":
    main()
