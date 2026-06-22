from transformers import pipeline


def load_finbert():

    classifier = pipeline(
        "text-classification",
        model="ProsusAI/finbert"
    )

    return classifier


if __name__ == "__main__":

    model = load_finbert()

    print("FinBERT loaded successfully!")