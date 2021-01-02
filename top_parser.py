import sys

fileName = sys.argv[1]

fp = open(fileName, 'r')

total_energy = 0

line = fp.readline()
while line:
    line = line.strip()
    try:
        total_energy += float(line)
    except ValueError:
        pass
    line = fp.readline()
print(str(total_energy))






# line = fp.readline()
# index = 1
# while line:
#     if index % 13 == 0:
#         line = line.strip()
#         total_energy += float(line)
#         # print(line)
#     index += 1
#     line = fp.readline()

# # print("Total energy: " + str(total_energy))
# print(str(total_energy))