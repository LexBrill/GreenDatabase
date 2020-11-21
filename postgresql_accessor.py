import psycopg2
import time
import os
import sys
import subprocess

trial_amount = int(sys.argv[1])
i = 1

con = psycopg2.connect(
    host = "localhost",
    database = "test",
    user = "lexingtonbrill",
    password = "")

cur = con.cursor()

cur.execute("SELECT pg_backend_pid()")
rows = cur.fetchall()
query_PID = rows[0][0]
print(query_PID)

# os.system("psrecord " + str(query_PID) + " --log CPU_Data.txt")
process = subprocess.Popen(["psrecord", str(query_PID), "--log", "CPU_Data.txt"])

time.sleep(.1)



cur.execute("SELECT * FROM csv_1000")
rows = cur.fetchall()
a = 0
for r in rows:
    print(f"{r} {a}")
    a += 1


process.kill()

cur.close()
con.close()