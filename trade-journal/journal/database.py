import sqlite3
from pathlib import Path
from journal.trade import Trade 


def main():
    insert_table()

def insert_table() -> None:
    DB_PATH = Path(__file__).resolve().parent / "trades.db"
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direction TEXT NOT NULL CHECK(direction IN ("long", "short")),
            entry_time TEXT NOT NULL,
            r_result REAL NOT NULL

    )

    """)
    connection.commit()
    connection.close()

def get_all_trades() -> list[Trade]:
    DB_PATH = Path(__file__).resolve().parent / "trades.db"
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM trades
    """)
    rows = cursor.fetchall()
    connection.close()
    trades = []
    for row in rows:
        trade = {"direction": row[1], "entry_time": row[2], "r_result": row[3]}
        trades.append(Trade.from_dict(trade))
    return trades

def add_trade(trade: Trade) -> None:
    DB_PATH = Path(__file__).resolve().parent / "trades.db"
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO trades(
            direction,
            entry_time, 
            r_result)
        VALUES
            (?, ?, ?)
    """, (
        trade.direction,
        trade.entry_time,
        trade.r_result
    ))

    connection.commit()
    connection.close()
        

if __name__ == "__main__":
    main()