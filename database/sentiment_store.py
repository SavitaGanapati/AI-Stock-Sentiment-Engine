import sqlite3


def create_sentiment_table():

    conn = sqlite3.connect("stock_sentiment.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sentiments (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ticker TEXT,

            positive_score REAL,

            negative_score REAL,

            neutral_score REAL,

            compound_score REAL,

            confidence REAL

        )
        """
    )

    conn.commit()

    conn.close()


if __name__ == "__main__":

    create_sentiment_table()

    print("Sentiment table created successfully!")