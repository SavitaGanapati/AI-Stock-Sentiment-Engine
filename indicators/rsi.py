import yfinance as yf
import pandas as pd


def calculate_rsi(ticker, period=14):

    stock = yf.download(
        ticker,
        period="6mo"
    )

    delta = stock["Close"].diff()

    gain = delta.where(delta > 0, 0)

    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()

    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss

    stock["RSI"] = 100 - (100 / (1 + rs))

    return stock[["Close", "RSI"]]


if __name__ == "__main__":

    data = calculate_rsi(
        "RELIANCE.NS"
    )

    print(data.tail())