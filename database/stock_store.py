import sqlite3


def create_stock_table():

    conn = sqlite3.connect("stock_sentiment.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS stocks (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ticker TEXT,

            sector TEXT,

            market_cap REAL,

            volume REAL,

            fsi REAL

        )
        """
    )

    conn.commit()

    conn.close()


if __name__ == "__main__":

    create_stock_table()

    print("Stock table created successfully!")