from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentEngine:

    def __init__(self):

        self.finbert = pipeline(
            "text-classification",
            model="ProsusAI/finbert"
        )

        self.vader = SentimentIntensityAnalyzer()


    def finbert_sentiment(self, text):

        result = self.finbert(text)

        return result


    def vader_sentiment(self, text):

        result = self.vader.polarity_scores(text)

        return result


if __name__ == "__main__":

    engine = SentimentEngine()

    sample_text = """
    Reliance Industries reported strong earnings and
    analysts remain bullish.
    """

    print("\nFinBERT Output:")
    print(engine.finbert_sentiment(sample_text))

    print("\nVADER Output:")
    print(engine.vader_sentiment(sample_text))