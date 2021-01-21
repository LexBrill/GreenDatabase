import sys

fileName = sys.argv[1]

fp = open(fileName, 'r')

max_energy = 0

line = fp.readline()
while line:
    line = line.strip()
    try:
        max_energy = max(max_energy, float(line))
    except ValueError:
        pass
    line = fp.readline()
print(str(max_energy))
