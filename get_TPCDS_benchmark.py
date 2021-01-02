import sys
import os

trials = int(sys.argv[1])

## Try getting rid of 4, 5, 6, 11, 12, 16, 18, 19, 20, 21, 22,
bad_queries = [4, 5, 11, 12, 16, 20, 21, 32, 37, 40, 72, 74, 77, 80, 82, 90, 92, 94, 95, 98]

index = 0
query_number = []

for num in range(1, 100):
    count = 0
    if num not in bad_queries:
        print("Query " + str(num), flush = True)
        while count < trials:
            if num == 10:
                os.system("python3 TPCDS_query_run.py query" + str(num) + "a.sql")
            elif num == 35:
                os.system("python3 TPCDS_query_run.py query" + str(num) + "a.sql")
            else:
                os.system("python3 TPCDS_query_run.py query" + str(num) + ".sql")
            count += 1

