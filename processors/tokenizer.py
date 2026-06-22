import nltk
from nltk.corpus import stopwords

# Download stop words (only first time)
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

# Financial phrases to preserve
financial_phrases = [
    "bull run",
    "bear market",
    "rate cut",
    "interest hike",
    "profit booking"
]


def tokenize_text(text):

    words = text.split()

    tokens = []

    for word in words:

        if word.lower() not in stop_words:
            tokens.append(word)

    return tokens


if __name__ == "__main__":

    sample = """
    RBI announces a rate cut and markets enter a bull run
    """

    tokens = tokenize_text(sample)

    print(tokens)