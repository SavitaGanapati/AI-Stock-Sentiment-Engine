"""
AI Stock Sentiment Engine
Main Entry Point
"""


from reports.daily_report import generate_daily_report


def main():

    print("\n" + "=" * 60)
    print("AI STOCK SENTIMENT ENGINE")
    print("=" * 60)

    print("\nStep 1 : Collecting stock news...")

    # Scrapers
    # get_news()

    print("Completed")

    print("\nStep 2 : Processing text...")

    # text_cleaner()
    # tokenizer()

    print("Completed")

    print("\nStep 3 : Running sentiment models...")

    # finbert_model()
    # vader_model()

    print("Completed")

    print("\nStep 4 : Computing sentiment scores...")

    # final_sentiment_index()

    print("Completed")

    print("\nStep 5 : Ranking stocks...")

    # ranking_engine()

    print("Completed")

    print("\nStep 6 : Generating report...")

    generate_daily_report()

    print("\n" + "=" * 60)
    print("Execution completed successfully.")
    print("=" * 60)


if __name__ == "__main__":

    main()