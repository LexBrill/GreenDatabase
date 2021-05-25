import sys
import predict_usage

fileName = sys.argv[1]

fp = open(fileName, 'r')

cpuTotal = 0.0
maxMax = 0.0
maxTemp = 0.0
memTotal = 0.0
rows = 0

l_weight = 1
seq_scan_average = []

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
    elif query_type == "projection": # probably not going to matter
        cpuTotal += predict_usage.getResult("projection", "cpu", rows)
        maxTemp = predict_usage.getResult("projection", "max", rows)
        maxMax = max(maxMax, maxTemp)
        memTotal += predict_usage.getResult("projection", "mem", rows)
    elif query_type == "join":
        cpuTotal += predict_usage.getResult("join", "cpu", (rows + (sum(seq_scan_average) * l_weight)))
        maxTemp = predict_usage.getResult("join", "max", (rows + (sum(seq_scan_average) * l_weight)))
        maxMax = max(maxMax, maxTemp)
        memTotal += predict_usage.getResult("join", "mem", (rows + (sum(seq_scan_average) * l_weight)))


delayed_calculation = []

line = fp.readline()
while line:
    line_temp = line
    line = line.strip()
    if line[0:2] == "->":
        number_of_spaces = 0
        while line_temp[number_of_spaces] == " ":
            number_of_spaces += 1
        line = line.lower()
        line_list = line.split('(')
        query_type = line_list[0].strip()[4:].split()
        rows = float(line_list[1].split()[1][5:])

        if len(delayed_calculation) > 0 and len(delayed_calculation[0]) == 2 and number_of_spaces <= delayed_calculation[0][1]:
            get_info("join")
            delayed_calculation.clear()
            seq_scan_average.clear()

        elif query_type[0] == "groupaggregate":
            pass

        elif query_type[0] == "gather":
            if len(query_type) > 1 and query_type[1] == "merge":
                get_info("selection")

        elif query_type[0] == "parallel":
            if query_type[1] == "hash" and len(query_type) >= 3 and query_type[2] == "join":
                delayed_calculation.append(tuple(("join", number_of_spaces)))
            elif query_type[1] == "hash":
                get_info("hash")
            elif query_type[1] == "seq":
                get_info("selection")
        
        elif query_type[0] == "hash" and len(query_type) > 1 and query_type[1] == "join":
            delayed_calculation.append(tuple(("join", number_of_spaces)))

        elif query_type[0] == "hash":
            get_info("hash")
            # if query_type[1] == None:
            #     get_info("hash")
            # elif query_type[1] == "join":
            #     get_info("hash")
        
        elif query_type[0] == "seq":
            if len(delayed_calculation) > 0 and len(delayed_calculation[0]) == 2 and number_of_spaces > delayed_calculation[0][1]:
                seq_scan_average.append(rows)
        
        elif query_type[0] == "finalize":
            get_info("selection")

        elif query_type[0] == "partial":
            pass

        elif query_type[0] == "append":
            get_info("selection")

        elif query_type[0] == "sort":
            get_info("sort")

        elif query_type[0] == "subquery":
            get_info("selection")

        elif query_type[0] == "unique":
            get_info("hash")

    line = fp.readline()

print("CPU TOTAL: " + str(cpuTotal))
print("MAX CPU: " + str(maxMax))
print("MEM TOTAL: " + str(memTotal))
        

# print(str(cpuTotal))


