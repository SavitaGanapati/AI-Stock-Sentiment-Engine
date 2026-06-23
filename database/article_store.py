import sqlite3


def create_article_table():

    conn = sqlite3.connect("stock_sentiment.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS articles (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            source TEXT,

            headline TEXT,

            article_text TEXT,

            ticker TEXT

        )
        """
    )

    conn.commit()

    conn.close()


if __name__ == "__main__":

    create_article_table()

    print("Articles table created successfully!")


    