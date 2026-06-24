"""
News Pipeline
Coordinates the end-to-end sentiment workflow.
"""
from database.article_store import (
    insert_article
)
from datetime import datetime
from scrapers.moneycontrol_scraper import (
    get_moneycontrol_headlines
)

from scrapers.twitter_scraper import (
    get_twitter_posts
)

from reports.daily_report import (
    generate_daily_report
)

from scrapers.economic_times_scraper import (
    get_et_headlines

)
def run_pipeline():

    print("\nStarting news pipeline...")

    print("\nCollecting Moneycontrol news...")

    news = get_moneycontrol_headlines()

    print(
        f"Number of news items: {len(news)}"
    )
    for headline in news:

        insert_article(
            timestamp=datetime.now().isoformat(),
            source="Moneycontrol",
            headline=headline,
            article_text=headline,
            ticker=""
    )

    print(
    f"Stored {len(news)} Moneycontrol headlines."
)
    print("\nCollecting Twitter posts...")
    tickers = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS"
]   
    for ticker in tickers:
        posts = get_twitter_posts(ticker)
        
    print(
        f"Number of posts: {len(posts)}"
    )

    print("\nGenerating report...")

    generate_daily_report()

    print("\n Collecting ET headlines")
    get_et_headlines()

    print(
        "\nPipeline completed successfully."
    )


if __name__ == "__main__":

    run_pipeline()