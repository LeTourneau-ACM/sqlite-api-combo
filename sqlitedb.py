import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

def create_table(conn, sql_syntax):
    try:
        c = conn.cursor()
        c.execute(sql_syntax)
    except Error as e:
        print(e)

def main():
    database = "pythonsqlite.db"

    create_statement = """  CREATE TABLE IF NOT EXISTS Facts(
                            id integer PRIMARY KEY AUTOINCREMENT,
                            fact text NOT NULL,
                            rating integer default 0
                            );"""
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, create_statement)
    else:
        print("Error! Cannot connect to the database")

    # Create a cursor object so we can execute SQL queries

    c = conn.cursor()
    c.execute("INSERT INTO Facts(fact, rating) VALUES ('TEST FACT 2', 3);")
    c.execute("INSERT INTO Facts(fact, rating) VALUES ('TEST FACT 2', 3);")

    c.execute("SELECT * FROM Facts;")
    # Get the results from the select query
    rows = c.fetchall()
    # Loop through the results and print each of the results
    for row in rows:
        print(row)

    # Commit the changes to the database.
    conn.commit()

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
