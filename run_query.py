import psycopg2
import os
import sys
import subprocess
import time

operation_type = sys.argv[1].lower()
test_query = ""
csv_rows = sys.argv[2]
table_name = "key_" + csv_rows

if operation_type == "sort":
    test_query = "SELECT * FROM " + table_name + " ORDER BY c1"
elif operation_type == "hash":
    test_query = "SELECT c1 FROM " + table_name + " GROUP BY c1"
elif operation_type == "selection":
    test_query = "SELECT * FROM " + table_name + " WHERE c1 = 'a'"
elif operation_type == "projection":
    test_query = "SELECT c1 FROM " + table_name
elif operation_type == "join":
    # Ensure that the column selected has a unique index. Otherwise the query will time-out
    test_query = "SELECT * FROM " + table_name + " JOIN " + table_name + "b ON " + table_name + ".c14 = " + table_name + "b.c14"


con = psycopg2.connect(
    host = "localhost",
    database = "key_tables",
    user = "lexingtonbrill",
    password = "")

cur = con.cursor()

cur.execute("SELECT pg_backend_pid()")
rows = cur.fetchall()
query_PID = rows[0][0]
# print(query_PID)

process = subprocess.Popen(["psrecord", str(query_PID), "--log", "CPU_Data.txt"])

time.sleep(.1)

cur.execute(test_query)

time.sleep(.05)

process.kill()

# print(operation_type + " of " + str(csv_rows) + " completed")

cur.close()
con.close()
