import psycopg2

try:
    # Establish connection using TCP/IP
    connection = psycopg2.connect(
        database="chinook",
        host="localhost",  
        port="5432"        
    )

    # Build a cursor object of the database
    cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
    # cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
    # cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
    # cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
    cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

    # Query 6 - select all tracks where the composer is "Queen" from the "Track" table
    # cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

    # Fetch the results (multiple)
    results = cursor.fetchall()

    # results = cursor.fetchone()

    # Print results
    for result in results:
        print(result)

except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")

finally:
    if connection:
        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
