def get_portfolio():

    portfolio = {

        "Cash": 250000,

        "Holdings": {

            "RELIANCE.NS": 300000,

            "INFY.NS": 250000,

            "TCS.NS": 200000

        }

    }

    return portfolio


if __name__ == "__main__":

    portfolio = get_portfolio()

    print(portfolio)