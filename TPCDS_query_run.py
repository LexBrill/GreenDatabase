import psycopg2
import time
import os
import sys
import subprocess

query = sys.argv[1]

fp = open("queries/" + sys.argv[1], "r")
sql_query = fp.read()
fp.close()

con = psycopg2.connect(
    host = "localhost",
    database = "tpcds",
    user = "lexingtonbrill",
    password = ""
)

cur = con.cursor()

cur.execute("SELECT pg_backend_pid()")
rows = cur.fetchall()
query_PID = rows[0][0]
print(query_PID)

#top -pid 430 -stats power -o power -l 0 > top.txt
outputFile = open("top.txt", "w")

process = subprocess.Popen(["top", "-pid", str(query_PID), "-stats", "power", "-o", "power", "-l", "0"], stdout = outputFile)

time.sleep(1)

cur.execute(sql_query)
rows = cur.fetchall()
a = 0
for r in rows:
    print(f"{r} {a}")
    a += 1

time.sleep(1)
process.kill()

cur.close()
con.close()

os.system("python3 top_parser.py top.txt")