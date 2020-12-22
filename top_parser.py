import sys

fileName = sys.argv[1]

fp = open(fileName, 'r')

total_energy = 0

line = fp.readline()
index = 1
while line:
    if index % 13 == 0:
        line = line.strip()
        total_energy += float(line)
        print(line)
    index += 1
    line = fp.readline()

print("Total energy: " + str(total_energy))