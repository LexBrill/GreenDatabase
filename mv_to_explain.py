import psycopg2
import os
import sys
import subprocess
import time

sql_query = sys.argv[1]
mvName = sys.argv[2]

con = psycopg2.connect(
    host = "localhost",
    database = "tpcds",
    user = "lexingtonbrill",
    password = ""
)
cur = con.cursor()

outputFile = open("mvs/mv" + mvName + ".txt", "w")
cur.execute("EXPLAIN (FORMAT TEXT) " + sql_query)
rows = cur.fetchall()
rows_string = ""
for tup in rows:
    rows_string += str(tup[0]) + "\n"
n = outputFile.write(rows_string)
print(mvName)

cur.close()
con.close()