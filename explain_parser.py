import psycopg2
import sys
import json

query = sys.argv[1]

if query[len(query)-1] == ";":
    query = query[0:len(query)-1]

explain_query = "EXPLAIN (FORMAT JSON) " + query

# print(explain_query)

con = psycopg2.connect(
    host = "localhost",
    database = "test",
    user = "lexingtonbrill",
    password = "")

cur = con.cursor()

cur.execute(explain_query)
rows = cur.fetchall()
# for r in rows:
#     # brokenSplit = r[0].split()
#     # print(brokenSplit[0])
#     # print(brokenSplit[2][5:])

#     # print(r[0])
#     print(f"{r}")

print(json.dumps(rows, indent = 2))
# print(rows)


# print(data)

cur.close()
con.close()