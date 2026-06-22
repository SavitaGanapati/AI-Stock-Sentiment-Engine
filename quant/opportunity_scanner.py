import pandas as pd


def scan_opportunities():

    stocks = [

        {
            "Ticker": "RELIANCE.NS",
            "FSI": 82,
            "Macro_Theme": "Positive",
            "Sentiment_Shift": "Strong Positive Shift"
        },

        {
            "Ticker": "INFY.NS",
            "FSI": 76,
            "Macro_Theme": "Positive",
            "Sentiment_Shift": "Strong Positive Shift"
        },

        {
            "Ticker": "TCS.NS",
            "FSI": 69,
            "Macro_Theme": "Positive",
            "Sentiment_Shift": "Normal"
        }

    ]

    df = pd.DataFrame(stocks)

    return df


if __name__ == "__main__":

    opportunities = scan_opportunities()

    print(opportunities)