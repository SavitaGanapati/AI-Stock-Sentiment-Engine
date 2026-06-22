import pandas as pd


def rank_stocks(stock_data):

    df = pd.DataFrame(stock_data)

    df = df.sort_values(
        by="FSI",
        ascending=False
    )

    df["Rank"] = range(
        1,
        len(df) + 1
    )

    return df


if __name__ == "__main__":

    stock_data = [

        {
            "Ticker": "RELIANCE.NS",
            "FSI": 82.4
        },

        {
            "Ticker": "INFY.NS",
            "FSI": 75.3
        },

        {
            "Ticker": "TCS.NS",
            "FSI": 69.7
        },

        {
            "Ticker": "HDFCBANK.NS",
            "FSI": 61.2
        }

    ]

    ranked_df = rank_stocks(stock_data)

    print(ranked_df)