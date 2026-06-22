from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def load_vader():

    analyzer = SentimentIntensityAnalyzer()

    return analyzer


if __name__ == "__main__":

    model = load_vader()

    print("VADER loaded successfully!")