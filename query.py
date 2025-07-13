import pymysql
from pymysql.cursors import DictCursor

# Fetch
def view_all_data(custom_query=None):
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="your_username",
        password="your_password",
        database="your_database_name",
        cursorclass=DictCursor  # Use DictCursor for dictionary results
    )
    try:
        c = conn.cursor()
        if custom_query:
            c.execute(custom_query)
        else:
            c.execute('SELECT * FROM insurance ORDER BY id ASC')
        data = c.fetchall()
        return data
    finally:
        c.close()
        conn.close()
