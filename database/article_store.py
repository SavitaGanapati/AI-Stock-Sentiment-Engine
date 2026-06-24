import sqlite3


def create_article_table():

    conn = sqlite3.connect(
        "stock_sentiment.db"
    )

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


def insert_article(
    timestamp,
    source,
    headline,
    article_text,
    ticker
):

    conn = sqlite3.connect(
        "stock_sentiment.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO articles
        (
            timestamp,
            source,
            headline,
            article_text,
            ticker
        )
        VALUES
        (?, ?, ?, ?, ?)
        """,
        (
            timestamp,
            source,
            headline,
            article_text,
            ticker
        )
    )

    conn.commit()

    conn.close()


if __name__ == "__main__":

    create_article_table()

    insert_article(
        timestamp="2026-06-24",
        source="Moneycontrol",
        headline="Reliance expands retail business",
        article_text="Reliance expands retail business across India.",
        ticker="RELIANCE.NS"
    )

    print(
        "Article inserted successfully!"
    )