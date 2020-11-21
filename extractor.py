import sys

fileName = sys.argv[1]

if sys.argv[2].lower() == "cpu":
    getCPU = True
elif sys.argv[2].lower() == "mem":
    getCPU = False


fp = open(fileName, 'r')

line = fp.readline()
line = fp.readline()

reachedData = False

while line:
    data = line.split()

    if getCPU:
        if reachedData:
            print(data[1])
        else:
            if data[1] != "0.000":
                reachedData = True
                print(data[1])
    elif not getCPU:
        if reachedData:
            print(data[2])
        else:
            if data[1] != "0.000":
                reachedData = True
                print(data[2])
    line = fp.readline()