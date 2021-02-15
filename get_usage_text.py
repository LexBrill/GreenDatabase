import sys
import predict_usage

fileName = sys.argv[1]

fp = open(fileName, 'r')

cpuTotal = 0.0
maxMax = 0.0
maxTemp = 0.0
memTotal = 0.0
rows = 0

def get_info(query_type):
    global cpuTotal
    global maxTemp
    global maxMax
    global memTotal
    if query_type == "hash":
        cpuTotal += predict_usage.getResult("hash", "cpu", rows)
        maxTemp = predict_usage.getResult("hash", "max", rows)
        maxMax = max(maxMax, maxTemp)
        memTotal += predict_usage.getResult("hash", "mem", rows)
    elif query_type == "sort":
        cpuTotal += predict_usage.getResult("sort", "cpu", rows)
        maxTemp = predict_usage.getResult("sort", "max", rows)
        maxMax = max(maxMax, maxTemp)
        memTotal += predict_usage.getResult("sort", "mem", rows)
    elif query_type == "selection":
        cpuTotal += predict_usage.getResult("selection", "cpu", rows)
        maxTemp = predict_usage.getResult("selection", "max", rows)
        maxMax = max(maxMax, maxTemp)
        memTotal += predict_usage.getResult("selection", "mem", rows)
    elif query_type == "projection":
        cpuTotal += predict_usage.getResult("projection", "cpu", rows)
        maxTemp = predict_usage.getResult("projection", "max", rows)
        maxMax = max(maxMax, maxTemp)
        memTotal += predict_usage.getResult("projection", "mem", rows)
    elif query_type == "join":
        cpuTotal += predict_usage.getResult("join", "cpu", rows)
        maxTemp = predict_usage.getResult("join", "max", rows)
        maxMax = max(maxMax, maxTemp)
        memTotal += predict_usage.getResult("join", "mem", rows)



line = fp.readline()
line = fp.readline()
line = fp.readline()
line = "->  " + line
while line:
    line = line.strip()
    if line[0:2] == "->":
        line = line.lower()
        line_list = line.split('(')
        query_type = line_list[0].strip()[4:].split()
        rows = float(line_list[1].split()[1][5:])
        if query_type[0] == "groupaggregate":
            pass

        elif query_type[0] == "gather":
            if query_type[1] == "merge":
                get_info("selection")

        elif query_type[0] == "parallel":
            if query_type[1] == "hash":
                get_info("hash")
            elif query_type[1] == "seq":
                get_info("selection")
        
        elif query_type[0] == "hash":
            get_info("hash")
            # if query_type[1] == None:
            #     get_info("hash")
            # elif query_type[1] == "join":
            #     get_info("hash")
        
        elif query_type[0] == "finalize":
            get_info("selection")

        elif query_type[0] == "partial":
            pass

        elif query_type[0] == "append":
            get_info("selection")

        elif query_type[0] == "sort":
            get_info("sort")

    line = fp.readline()

print(str(cpuTotal))
print(str(maxMax))
print(str(memTotal))
        



