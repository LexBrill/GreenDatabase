import sys
import json

fileName = sys.argv[1]
json_file = open(fileName)
data = json.load(json_file)
sql_select = "SELECT "
select_bool = False
sql_from = "FROM "
from_bool = False
from_list = []
sql_where = "WHERE "
where_bool = False
columns = data["table_columns"]
predicates = data["predicates"]
conditions = data["conditions"]

num = 0
for element in columns:
    select_bool = True
    if num > 0:
        sql_select += ", "
    sql_select += element["table"] + "." + element["column"]
    if element["table"] not in from_list:
        from_list.append(element["table"])
    num += 1

num = 0
for element in from_list:
    from_bool = True
    if num > 0:
        sql_from += ", "
    sql_from += element
    num += 1

num = 0
for element in predicates:
    where_bool = True
    conditional = element["left"] + " " + element["op"] + " " + element["right"]
    if num > 0:
        sql_where += " AND "
    sql_where += conditional
# for element in conditions:
#     conditional 

final_query = ""
if select_bool:
    final_query += sql_select
if from_bool:
    final_query += "\n" + sql_from
if where_bool:
    final_query += "\n" + sql_where
final_query += ";"
print(final_query)