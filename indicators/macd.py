import yfinance as yf


def calculate_macd(ticker):

    stock = yf.download(
        ticker,
        period="1y"
    )

    stock["EMA12"] = (
        stock["Close"]
        .ewm(span=12, adjust=False)
        .mean()
    )

    stock["EMA26"] = (
        stock["Close"]
        .ewm(span=26, adjust=False)
        .mean()
    )

    stock["MACD"] = (
        stock["EMA12"]
        - stock["EMA26"]
    )

    stock["Signal"] = (
        stock["MACD"]
        .ewm(span=9, adjust=False)
        .mean()
    )

    return stock[
        [
            "Close",
            "MACD",
            "Signal"
        ]
    ]


if __name__ == "__main__":

    data = calculate_macd(
        "RELIANCE.NS"
    )

    print(data.tail())