import sqlite3

def test_database_exists():

    conn = sqlite3.connect("nifty100.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """)

    tables = cursor.fetchall()

    assert len(tables) == 9

    conn.close()