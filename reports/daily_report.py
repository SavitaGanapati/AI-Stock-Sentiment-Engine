"""
Daily report generator.
"""

import pandas as pd


def generate_daily_report():

    data = {

        "Ticker": [
            "RELIANCE.NS",
            "TCS.NS",
            "INFY.NS"
        ],

        "Sentiment": [
            "Positive",
            "Neutral",
            "Positive"
        ]
    }

    df = pd.DataFrame(data)

    print("\nDaily Report\n")

    print(df)

    df.to_csv(
        "reports/daily_report.csv",
        index=False
    )

    print(
        "\nReport saved successfully."
    )


if __name__ == "__main__":

    generate_daily_report()