import sys
import yaml

###############################################
# Computer model numbers were gathered from:  #
# Model:     MacBook Pro (16-inch, 2019)      #
# Processor: 2.6 Ghz 6-Core Intel Core i7     #
# Memory:    16 GB 2667 MHz DDR4              #
###############################################

yaml_file = open("model_data.yaml")
parsed_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)

cpu_sort_m = parsed_yaml["sort_cpu_m"]
cpu_sort_b = parsed_yaml["sort_cpu_b"]

cpu_hash_m = parsed_yaml["hash_cpu_m"]
cpu_hash_b = parsed_yaml["hash_cpu_b"]

cpu_selection_m = parsed_yaml["selection_cpu_m"]
cpu_selection_b = parsed_yaml["selection_cpu_b"]

cpu_projection_m = parsed_yaml["projection_cpu_m"]
cpu_projection_b = parsed_yaml["projection_cpu_b"]

cpu_join_m = parsed_yaml["join_cpu_m"]
cpu_join_b = parsed_yaml["join_cpu_b"]


mem_sort_m = parsed_yaml["sort_mem_m"]
mem_sort_b = parsed_yaml["sort_mem_b"]

mem_hash_m = parsed_yaml["hash_mem_m"]
mem_hash_b = parsed_yaml["hash_mem_b"]

mem_selection_m = parsed_yaml["selection_mem_m"]
mem_selection_b = parsed_yaml["selection_mem_b"]

mem_projection_m = parsed_yaml["projection_mem_m"]
mem_projection_b = parsed_yaml["projection_mem_b"]

mem_join_m = parsed_yaml["join_mem_m"]
mem_join_b = parsed_yaml["join_mem_b"]


max_sort_m = parsed_yaml["sort_max_m"]
max_sort_b = parsed_yaml["sort_max_b"]

max_hash_m = parsed_yaml["hash_max_m"]
max_hash_b = parsed_yaml["hash_max_b"]

max_selection_m = parsed_yaml["selection_max_m"]
max_selection_b = parsed_yaml["selection_max_b"]

max_projection_m = parsed_yaml["projection_max_m"]
max_projection_b = parsed_yaml["projection_max_b"]

max_join_m = parsed_yaml["join_max_m"]
max_join_b = parsed_yaml["join_max_b"]

def getResult(Operation, InfoType, Rows):
    if InfoType.lower() == "cpu":
        if Operation.lower() == "sort":
            result = (float(Rows) * cpu_sort_m) + cpu_sort_b
            return result
        elif Operation.lower() == "hash":
            result = (float(Rows) * cpu_hash_m) + cpu_hash_b
            return result
        elif Operation.lower() == "selection":
            result = (float(Rows) * cpu_selection_m) + cpu_selection_b
            return result
        elif Operation.lower() == "projection":
            result = (float(Rows) * cpu_projection_m) + cpu_projection_b
            return result
        elif Operation.lower() == "join":
            result = (float(Rows) * cpu_join_m) + cpu_join_b
            return result
        else:
            result = -1
            # print("Error. After \"cpu\", add operation then number of rows")
            print("Error 0")

    elif InfoType.lower() == "mem":
        if Operation.lower() == "sort":
            result = (float(Rows) * mem_sort_m) + mem_sort_b
            return result
        elif Operation.lower() == "hash":
            result = (float(Rows) * mem_hash_m) + mem_hash_b
            return result
        elif Operation.lower() == "selection":
            result = (float(Rows) * mem_selection_m) + mem_selection_b
            return result
        elif Operation.lower() == "projection":
            result = (float(Rows) * mem_projection_m) + mem_projection_b
            return result
        elif Operation.lower() == "join":
            result = (float(Rows) * mem_join_m) + mem_join_b
            return result
        else:
            result = -1
            # print("Error. After \"mem\", add operation then number of rows")
            print("Error 1")

    elif InfoType.lower() == "max":
        if Operation.lower() == "sort":
            result = (float(Rows) * max_sort_m) + max_sort_b
            return result
        elif Operation.lower() == "hash":
            result = (float(Rows) * max_hash_m) + max_hash_b
            return result
        elif Operation.lower() == "selection":
            result = (float(Rows) * max_selection_m) + max_selection_b
            return result
        elif Operation.lower() == "projection":
            result = (float(Rows) * max_projection_m) + max_projection_b
            return result
        elif Operation.lower() == "join":
            result = (float(Rows) * max_join_m) + max_join_b
            return result
        else:
            result = -1
            print("Error 2")
            # print("Error. After \"max\", add operation then number of rows")

    else:
        result = -1
        print("Error. Format: operation cpu/mem/max number of rows")

# print(getResult(sys.argv[1], sys.argv[2], sys.argv[3]))

