import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="abc123",
    host="localhost",
    port="5432"
)
conn.autocommit = True  # Enable autocommit mode

# Create a cursor object
cur = conn.cursor()

# Execute SQL to create a database
cur.execute("CREATE DATABASE database1;")
cur.execute("CREATE DATABASE database2;")
cur.execute("CREATE DATABASE database3;")

# Execute SQL to view all databases
cur.execute("SELECT datname FROM pg_database;")
databases = cur.fetchall()
print(databases)

# Execute SQL to create a table
cur.execute('''
    CREATE TABLE table1 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INT
    );           
''')

# Execute SQL to insert data into the table
cur.execute("INSERT INTO table1 (name, age) VALUES (%s, %s)", ("Alice", 30))


# Close the cursor and connection
cur.close()
conn.close()