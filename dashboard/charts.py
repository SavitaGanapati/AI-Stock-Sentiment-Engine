import pandas as pd
import plotly.express as px


def plot_fsi():

    data = {
        "Ticker": [
            "RELIANCE.NS",
            "INFY.NS",
            "TCS.NS",
            "HDFCBANK.NS"
        ],

        "FSI": [
            82,
            76,
            71,
            65
        ]
    }

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="Ticker",
        y="FSI",
        title="Final Sentiment Index"
    )

    fig.show()


if __name__ == "__main__":
    plot_fsi()