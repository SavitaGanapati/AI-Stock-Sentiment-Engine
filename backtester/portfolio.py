class Portfolio:

    def __init__(self, initial_capital):

        self.cash = initial_capital

        self.positions = {}


    def buy(self, ticker, amount):

        if amount <= self.cash:

            self.positions[ticker] = amount

            self.cash -= amount

            print(f"Bought {ticker} for ₹{amount}")

        else:

            print("Insufficient funds")


    def portfolio_summary(self):

        print("\nPortfolio Holdings:")

        for ticker, amount in self.positions.items():

            print(f"{ticker}: ₹{amount}")

        print(f"\nRemaining Cash: ₹{self.cash}")


if __name__ == "__main__":

    portfolio = Portfolio(
        initial_capital=1000000
    )

    portfolio.buy(
        "RELIANCE.NS",
        300000
    )

    portfolio.buy(
        "INFY.NS",
        250000
    )

    portfolio.buy(
        "TCS.NS",
        200000
    )

    portfolio.portfolio_summary()