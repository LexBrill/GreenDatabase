import json
import os
import predict_usage

f = open("outp.json",)
data = json.load(f)

cpuTotal = 0.0
maxMax = 0.0
maxTemp = 0.0
memTotal = 0.0

first_query = (data[0][0][0]["Plan"]["Node Type"], data[0][0][0]["Plan"]["Plan Rows"])
second_query = None

if "Plans" in data[0][0][0]["Plan"]:
    second_query = (data[0][0][0]["Plan"]["Plans"][0]["Node Type"], data[0][0][0]["Plan"]["Plans"][0]["Plan Rows"])

if first_query[0] == "Aggregate":
    cpuTotal += predict_usage.getResult("hash", "cpu", int(first_query[1]))
    # print(cpuTotal)
    maxTemp = predict_usage.getResult("hash", "max", int(first_query[1]))
    if maxTemp > maxMax:
        maxMax = maxTemp
    # print(maxMax)
    memTotal += predict_usage.getResult("hash", "mem", int(first_query[1]))
    # print(memTotal)
elif first_query[0] == "Sort":
    cpuTotal += predict_usage.getResult("sort", "cpu", int(first_query[1]))
    # print(cpuTotal)
    maxTemp = predict_usage.getResult("sort", "max", int(first_query[1]))
    if maxTemp > maxMax:
        maxMax = maxTemp
    # print(maxMax)
    memTotal += predict_usage.getResult("sort", "mem", int(first_query[1]))
    # print(memTotal)
elif first_query[0] == "Seq Scan" and "Filter" in data[0][0][0]["Plan"]:
    cpuTotal += predict_usage.getResult("selection", "cpu", int(first_query[1]))
    # print(cpuTotal)
    maxTemp = predict_usage.getResult("selection", "max", int(first_query[1]))
    if maxTemp > maxMax:
        maxMax = maxTemp
    # print(maxMax)
    memTotal += predict_usage.getResult("selection", "mem", int(first_query[1]))
    # print(memTotal)
elif first_query[0] == "Seq Scan" and not "Filter" in data[0][0][0]["Plan"]:
    cpuTotal += predict_usage.getResult("projection", "cpu", int(first_query[1]))
    # print(cpuTotal)
    maxTemp = predict_usage.getResult("projection", "max", int(first_query[1]))
    if maxTemp > maxMax:
        maxMax = maxTemp
    # print(maxMax)
    memTotal += predict_usage.getResult("projection", "mem", int(first_query[1]))
    # print(memTotal)
else:
    print("Nothing executed. Fix your code Lexington.")

if second_query != None:
    if second_query[0] == "Seq Scan":
        cpuTotal += predict_usage.getResult("projection", "cpu", int(second_query[1]))
        # print(cpuTotal)
        maxTemp = predict_usage.getResult("projection", "max", int(second_query[1]))
        if maxTemp > maxMax:
            maxMax = maxTemp
        # print(maxMax)
        memTotal += predict_usage.getResult("projection", "mem", int(second_query[1]))
        # print(memTotal)
    else:
        print("There is more than just a Seq Scan for the second query.\n Once again, fix it Lexington")
else:
    print("No second query")

print("Predicted Total CPU Usage: " + str(cpuTotal) + "")
print("Predicted Max CPU Usage: " + str(maxMax) + "%")
print("Predicted Total Memory Usage: " + str(memTotal) + " MBs")

    # print(predict_usage.getResult("cpu", "hash", int(first_query[1])))


# print(data[0][0][0]["Plan"]["Node Type"])
# print(data[0][0][0]["Plan"]["Plan Rows"])
# print(data[0][0][0]["Plan"]["Plans"][0]["Node Type"])
# print(data[0][0][0]["Plan"]["Plans"][0]["Plan Rows"])