import psycopg2
import os
import subprocess

bad_queries = [4, 5, 11, 12, 16, 20, 21, 32, 37, 40, 72, 74, 77, 80, 82, 90, 92, 94, 95, 96, 97, 98, 99]

con = psycopg2.connect(
    host = "localhost",
    database = "tpcds",
    user = "lexingtonbrill",
    password = "")

cur = con.cursor()

for num in range(1, 100):
    if num not in bad_queries:
        if num == 10 or num == 35:
            query_name = "query" + str(num) + "a.sql"
        else:
            query_name = "query" + str(num) + ".sql"
        fp = open("queries/" + query_name, "r")
        sql_query = fp.read()
        fp.close()
        outputFile = open("text_explain_query" + str(num) + ".txt", "w")
        cur.execute("EXPLAIN (FORMAT TEXT) " + sql_query)
        rows = cur.fetchall()
        rows_string = ""
        for tup in rows:
            rows_string += str(tup[0]) + "\n"
        n = outputFile.write(rows_string)
        print("Done query " + str(num))
        # print(rows)
        
cur.close()
con.close()

for num in range(1, 100):
    if num not in bad_queries:
        # print(str(num))
        os.system("python3 get_usage_text.py text_explain_query" + str(num) + ".txt")
    else:
        print()