import sys
import json
import time
import os

fileName = sys.argv[1]
json_file = open(fileName)
large_json = json.load(json_file)
# mv_index = 0
for data in large_json:
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
        if num > 0:
            sql_where += " AND "
        conditional = element["left"] + " " + element["op"] + " " + element["right"]
        sql_where += conditional
        num += 1
    keys = list(conditions.keys())
    conditions_index = 0
    for element in conditions:
        where_bool = True
        if num > 0:
            sql_where += " AND "
        conditional = keys[conditions_index] + " = " + conditions[element][0]["table"] + "." + conditions[element][0]["column"]
        sql_where += conditional
        num += 1
        conditions_index += 1

    final_query = ""
    if select_bool:
        final_query += sql_select
    if from_bool:
        final_query += " " + sql_from
    if where_bool:
        final_query += " " + sql_where
    final_query += ";"
    # print(data["mvName"])
    # print(final_query)
    try:
        os.system("python3 mv_to_explain.py \"" + final_query + "\" " + data["mvName"])
        os.system("python3 get_usage_text.py mvs/mv" + data["mvName"] + ".txt")
    except:
        pass
    # mv_index += 1
    # time.sleep(3)