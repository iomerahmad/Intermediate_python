import sqlite3
from pathlib import Path
def main():
    pass

    

def insert_table() -> None:
    DB_PATH = Path(__file__).resolve().parent / "trades.db"
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direction TEXT NOT NULL CHECK(direction IN ("Long", "short")),
            entry_time TEXT NOT NULL,
            r_result REAL NOT NULL

    )

    """)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()