import os
import sys


trial_amount = int(sys.argv[1])

i = 1

# os.system("mkdir gathered_data")

os.system("rm CPU_Data.txt")
os.system("rm processed_data.txt")
os.system("rm outp.json")

while i <= trial_amount:
    os.system("rm sort_cpu_100_" + str(i) + ".txt")
    os.system("rm sort_cpu_1000_" + str(i) + ".txt")
    os.system("rm sort_cpu_10000_" + str(i) + ".txt")
    os.system("rm sort_cpu_30000_" + str(i) + ".txt")
    os.system("rm sort_cpu_60000_" + str(i) + ".txt")
    os.system("rm sort_cpu_100000_" + str(i) + ".txt")
    
    os.system("rm sort_mem_100_" + str(i) + ".txt")
    os.system("rm sort_mem_1000_" + str(i) + ".txt")
    os.system("rm sort_mem_10000_" + str(i) + ".txt")
    os.system("rm sort_mem_30000_" + str(i) + ".txt")
    os.system("rm sort_mem_60000_" + str(i) + ".txt")
    os.system("rm sort_mem_100000_" + str(i) + ".txt")
    
    os.system("rm hash_cpu_100_" + str(i) + ".txt")
    os.system("rm hash_cpu_1000_" + str(i) + ".txt")
    os.system("rm hash_cpu_10000_" + str(i) + ".txt")
    os.system("rm hash_cpu_30000_" + str(i) + ".txt")
    os.system("rm hash_cpu_60000_" + str(i) + ".txt")
    os.system("rm hash_cpu_100000_" + str(i) + ".txt")
    
    os.system("rm hash_mem_100_" + str(i) + ".txt")
    os.system("rm hash_mem_1000_" + str(i) + ".txt")
    os.system("rm hash_mem_10000_" + str(i) + ".txt")
    os.system("rm hash_mem_30000_" + str(i) + ".txt")
    os.system("rm hash_mem_60000_" + str(i) + ".txt")
    os.system("rm hash_mem_100000_" + str(i) + ".txt")
    
    os.system("rm selection_cpu_100_" + str(i) + ".txt")
    os.system("rm selection_cpu_1000_" + str(i) + ".txt")
    os.system("rm selection_cpu_10000_" + str(i) + ".txt")
    os.system("rm selection_cpu_30000_" + str(i) + ".txt")
    os.system("rm selection_cpu_60000_" + str(i) + ".txt")
    os.system("rm selection_cpu_100000_" + str(i) + ".txt")
    
    os.system("rm selection_mem_100_" + str(i) + ".txt")
    os.system("rm selection_mem_1000_" + str(i) + ".txt")
    os.system("rm selection_mem_10000_" + str(i) + ".txt")
    os.system("rm selection_mem_30000_" + str(i) + ".txt")
    os.system("rm selection_mem_60000_" + str(i) + ".txt")
    os.system("rm selection_mem_100000_" + str(i) + ".txt")
    
    os.system("rm projection_cpu_100_" + str(i) + ".txt")
    os.system("rm projection_cpu_1000_" + str(i) + ".txt")
    os.system("rm projection_cpu_10000_" + str(i) + ".txt")
    os.system("rm projection_cpu_30000_" + str(i) + ".txt")
    os.system("rm projection_cpu_60000_" + str(i) + ".txt")
    os.system("rm projection_cpu_100000_" + str(i) + ".txt")
    
    os.system("rm projection_mem_100_" + str(i) + ".txt")
    os.system("rm projection_mem_1000_" + str(i) + ".txt")
    os.system("rm projection_mem_10000_" + str(i) + ".txt")
    os.system("rm projection_mem_30000_" + str(i) + ".txt")
    os.system("rm projection_mem_60000_" + str(i) + ".txt")
    os.system("rm projection_mem_100000_" + str(i) + ".txt")

    os.system("rm join_cpu_100_" + str(i) + ".txt")
    os.system("rm join_cpu_1000_" + str(i) + ".txt")
    os.system("rm join_cpu_10000_" + str(i) + ".txt")
    os.system("rm join_cpu_30000_" + str(i) + ".txt")
    os.system("rm join_cpu_60000_" + str(i) + ".txt")
    os.system("rm join_cpu_100000_" + str(i) + ".txt")
    
    os.system("rm join_mem_100_" + str(i) + ".txt")
    os.system("rm join_mem_1000_" + str(i) + ".txt")
    os.system("rm join_mem_10000_" + str(i) + ".txt")
    os.system("rm join_mem_30000_" + str(i) + ".txt")
    os.system("rm join_mem_60000_" + str(i) + ".txt")
    os.system("rm join_mem_100000_" + str(i) + ".txt")
    
    i += 1
