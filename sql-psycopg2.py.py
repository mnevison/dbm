import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

results = cursor.fetchall()

# results = cursor.fetchone()

connecton.close()

for result in results:
    print(result)