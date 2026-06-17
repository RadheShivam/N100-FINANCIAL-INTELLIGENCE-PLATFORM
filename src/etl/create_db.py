# # import sqlite3

# # conn = sqlite3.connect("nifty100.db")

# # with open("db/schema.sql", "r") as f:
# #     conn.executescript(f.read())

# # conn.commit()
# # conn.close()

# # print("Database created successfully!")







# import sqlite3
# import os

# print("Current Directory:", os.getcwd())

# conn = sqlite3.connect("nifty100.db")

# with open("db/schema.sql", "r", encoding="utf-8") as f:
#     sql_script = f.read()

# print("\nSQL Loaded Successfully")
# print(sql_script[:200])

# try:
#     conn.executescript(sql_script)
#     conn.commit()

#     print("\nTables Created Successfully")

# except Exception as e:
#     print("\nERROR:")
#     print(e)

# finally:
#     conn.close()

















import sqlite3
import os

print("Current Working Directory:")
print(os.getcwd())

conn = sqlite3.connect("nifty100.db")

with open("db/schema.sql", "r", encoding="utf-8") as f:
    schema = f.read()

print("\nSchema loaded successfully.")

conn.executescript(schema)

conn.commit()

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

print("\nTables created:")
print(tables)

conn.close()