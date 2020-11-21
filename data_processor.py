import sys

fileName = sys.argv[1]

if sys.argv[2].lower() == "cpu":
    getCPU = True
elif sys.argv[2].lower() == "mem":
    getCPU = False


fp = open(fileName, 'r')

line = fp.readline()
lastValue = line.split()

line = fp.readline()

area = 0

max_CPU = float(lastValue[0])

data_transfer = 0


while line:
    data = line.split()

    if getCPU:
        area = area + ((float(lastValue[0]) + float(data[0])) / 2)
        lastValue[0] = float(data[0])

        if max_CPU < float(data[0]):
            max_CPU = float(data[0])

    elif not getCPU:
        data_transfer = data_transfer + abs(float(lastValue[0]) - float(data[0]))
        lastValue[0] = float(data[0])

    line = fp.readline()

if getCPU:
    print(area)
    print(max_CPU)
else:
    print(data_transfer)