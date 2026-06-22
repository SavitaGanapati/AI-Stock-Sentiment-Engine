import pandas as pd


def get_nse_symbols():

    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

    df = pd.read_csv(url)

    df["ticker"] = df["SYMBOL"] + ".NS"

    return df


if __name__ == "__main__":

    stocks = get_nse_symbols()

    print(stocks.head())