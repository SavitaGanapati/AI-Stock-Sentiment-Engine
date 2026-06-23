import yfinance as yf


def analyze_volume(
        ticker,
        period=20):

    stock = yf.download(
        ticker,
        period="6mo"
    )

    stock["Average_Volume"] = (
        stock["Volume"]
        .rolling(window=period)
        .mean()
    )

    return stock[
        [
            "Volume",
            "Average_Volume"
        ]
    ]


if __name__ == "__main__":

    data = analyze_volume(
        "RELIANCE.NS"
    )

    print(data.tail())