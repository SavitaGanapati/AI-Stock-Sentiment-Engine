"""
Twitter/X scraper module.

Version 1:
Simulated tweets for sentiment analysis.

Version 2:
- Tweepy API
- snscrape
- Cashtag monitoring
- Influencer tracking
- Trending topic detection
"""


def fetch_tweets(ticker):

    tweets = [

        f"{ticker} looks strong after recent earnings.",

        f"Investors are bullish on {ticker}.",

        f"{ticker} may outperform the sector this quarter.",

        f"Positive sentiment building around {ticker}."

    ]

    return tweets


if __name__ == "__main__":

    ticker = "RELIANCE.NS"

    tweets = fetch_tweets(ticker)

    print("\nTwitter/X Posts:\n")

    for tweet in tweets:

        print(tweet)