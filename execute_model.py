import os
import sys


trial_amount = int(sys.argv[1])

i = 1

# os.system("mkdir gathered_data")

while i <= trial_amount:
    os.system("python3 run_query.py sort 100 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > sort_cpu_100_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 1000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > sort_cpu_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 10000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > sort_cpu_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 30000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > sort_cpu_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 60000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > sort_cpu_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 100000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > sort_cpu_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py sort 100 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > sort_mem_100_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 1000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > sort_mem_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 10000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > sort_mem_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 30000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > sort_mem_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 60000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > sort_mem_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py sort 100000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > sort_mem_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py hash 100 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > hash_cpu_100_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 1000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > hash_cpu_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 10000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > hash_cpu_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 30000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > hash_cpu_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 60000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > hash_cpu_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 100000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > hash_cpu_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py hash 100 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > hash_mem_100_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 1000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > hash_mem_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 10000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > hash_mem_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 30000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > hash_mem_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 60000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > hash_mem_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py hash 100000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > hash_mem_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py selection 100 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > selection_cpu_100_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 1000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > selection_cpu_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 10000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > selection_cpu_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 30000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > selection_cpu_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 60000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > selection_cpu_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 100000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > selection_cpu_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py selection 100 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > selection_mem_100_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 1000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > selection_mem_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 10000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > selection_mem_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 30000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > selection_mem_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 60000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > selection_mem_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py selection 100000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > selection_mem_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py projection 100 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > projection_cpu_100_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 1000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > projection_cpu_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 10000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > projection_cpu_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 30000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > projection_cpu_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 60000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > projection_cpu_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 100000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > projection_cpu_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py projection 100 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > projection_mem_100_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 1000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > projection_mem_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 10000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > projection_mem_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 30000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > projection_mem_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 60000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > projection_mem_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py projection 100000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > projection_mem_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py join 100 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > join_cpu_100_" + str(i) + ".txt")
    os.system("python3 run_query.py join 1000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > join_cpu_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 10000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > join_cpu_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 30000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > join_cpu_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 60000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > join_cpu_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 100000 && python3 extractor.py CPU_Data.txt cpu > processed_data.txt && python3 data_processor.py processed_data.txt cpu > join_cpu_100000_" + str(i) + ".txt")
    
    os.system("python3 run_query.py join 100 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > join_mem_100_" + str(i) + ".txt")
    os.system("python3 run_query.py join 1000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > join_mem_1000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 10000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > join_mem_10000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 30000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > join_mem_30000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 60000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > join_mem_60000_" + str(i) + ".txt")
    os.system("python3 run_query.py join 100000 && python3 extractor.py CPU_Data.txt mem > processed_data.txt && python3 data_processor.py processed_data.txt mem > join_mem_100000_" + str(i) + ".txt")

    i += 1

os.system("python3 model.py " + str(trial_amount))

os.system("python3 cleaner.py " + str(trial_amount))