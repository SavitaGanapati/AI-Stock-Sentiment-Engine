"""
Database Tools

Utility functions for inspecting and maintaining
the Market Sentiment Analysis SQLite database.
"""

import sqlite3


DATABASE_NAME = "stock_sentiment.db"


def create_connection():
    """
    Create a connection to the SQLite database.
    """

    return sqlite3.connect(DATABASE_NAME)


def show_tables():
    """
    Display all tables in the database.
    """

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """
    )

    tables = cursor.fetchall()

    print("\nDatabase Tables\n")

    for table in tables:
        print(table[0])

    conn.close()


def show_articles_by_source():
    """
    Display number of articles by source.
    """

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            source,
            COUNT(*)
        FROM articles
        GROUP BY source
        """
    )

    rows = cursor.fetchall()

    print("\nArticles by Source\n")

    for source, count in rows:

        print(f"{source:<20} {count}")

    conn.close()


def show_latest_articles(limit=10):
    """
    Display the latest stored articles.
    """

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            timestamp,
            source,
            headline
        FROM articles
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    print("\nLatest Articles\n")

    for row in rows:

        print(row)

    conn.close()


if __name__ == "__main__":

    show_tables()

    show_articles_by_source()

    show_latest_articles()