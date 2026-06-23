"""
Twitter/X scraper module.

Version 1
---------
Mock Twitter posts for sentiment analysis.

Future Version 2
----------------
- Tweepy API
- snscrape
- Cashtag monitoring
- Influencer tracking
- Trending topic detection
"""


def get_twitter_posts(ticker):
    """
    Return Twitter/X posts related to a ticker.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol.

    Returns
    -------
    list
        List of tweet strings.
    """

    posts = [

        f"{ticker} looks strong after recent earnings.",

        f"Investors are bullish on {ticker}.",

        f"{ticker} may outperform its sector this quarter.",

        f"Positive sentiment building around {ticker}.",

        f"Analysts remain optimistic on {ticker}."

    ]

    return posts


if __name__ == "__main__":

    ticker = "RELIANCE.NS"

    posts = get_twitter_posts(
        ticker
    )

    print("\nTwitter/X Posts\n")

    for index, post in enumerate(posts, start=1):

        print(
            f"{index}. {post}"
        )