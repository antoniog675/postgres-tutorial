import psycopg2


# connect to chinnok using psycopg2
connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# Query 1 - Select all records from the 'Artist' table
# cursor.execute('SELECT * FROM "Artist"')
# cursor.execute('SELECT "Name" from "Artist"')
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

results = cursor.fetchall()

# results = cursor.fetchone()

connection.close()

for result in results:
    print(result)