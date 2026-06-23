import yfinance as yf


def calculate_moving_average(
        ticker,
        period=50):

    stock = yf.download(
        ticker,
        period="6mo"
    )

    stock["Moving_Average"] = (
        stock["Close"]
        .rolling(window=period)
        .mean()
    )

    return stock[["Close", "Moving_Average"]]


if __name__ == "__main__":

    data = calculate_moving_average(
        "RELIANCE.NS"
    )

    print(data.tail())