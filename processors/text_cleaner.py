import re


def clean_text(text):

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove special characters and emojis
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces
    text = " ".join(text.split())

    return text


if __name__ == "__main__":

    sample = """
    RBI cuts rates by 25 bps! Markets rally 🚀
    Read more: https://example.com
    """

    cleaned = clean_text(sample)

    print("Original Text:\n")
    print(sample)

    print("\nCleaned Text:\n")
    print(cleaned)