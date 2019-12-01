import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Qd9r7w6i', db='players')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
#cursor.execute("SELECT * FROM players.users;")


# Inserting data into table
# cursor.execute("INSERT INTO players.users (id, name) VALUES (5, 'john');")
# cursor.execute("INSERT INTO players.users (id, name) VALUES (6, 'Jack');")


# Getting all data from table “users”
cursor.execute("SELECT * FROM players.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)


# cursor.close()
# conn.close()
# cursor.execute("DELETE FROM players.users WHERE name = 'john'")

# Updating data inside the table
cursor.execute("UPDATE players.users SET id = '10' WHERE name = 'Jack'")

# cursor.close()

# Getting all data from table “users”
cursor.execute("SELECT * FROM players.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()