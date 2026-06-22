import sqlite3


def create_connection():

    connection = sqlite3.connect("stock_sentiment.db")

    return connection


if __name__ == "__main__":

    conn = create_connection()

    print("Database connection established successfully!")

    conn.close()