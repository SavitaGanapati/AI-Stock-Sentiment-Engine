import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, project_root)

from scrapers.twitter_scraper import get_twitter_posts


def test_twitter_scraper():

    posts = get_twitter_posts(
        "RELIANCE.NS"
    )

    print(posts)


if __name__ == "__main__":

    test_twitter_scraper()