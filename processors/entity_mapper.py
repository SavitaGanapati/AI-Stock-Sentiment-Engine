company_to_ticker = {

    "Reliance Industries": "RELIANCE.NS",

    "Infosys": "INFY.NS",

    "TCS": "TCS.NS",

    "HDFC Bank": "HDFCBANK.NS",

    "ICICI Bank": "ICICIBANK.NS"

}


def map_company_to_ticker(text):

    tickers = []

    for company, ticker in company_to_ticker.items():

        if company.lower() in text.lower():

            tickers.append(ticker)

    return tickers


if __name__ == "__main__":

    sample = """
    Reliance Industries and Infosys report strong quarterly earnings.
    """

    mapped = map_company_to_ticker(sample)

    print(mapped)