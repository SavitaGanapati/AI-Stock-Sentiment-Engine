def calculate_fsi(
        sentiment_score,
        time_weight,
        source_weight):

    weighted_score = (
        sentiment_score
        * time_weight
        * source_weight
    )

    fsi = weighted_score * 100

    return round(fsi, 2)


if __name__ == "__main__":

    sentiment_score = 0.85

    time_weight = 0.75

    source_weight = 0.85

    fsi = calculate_fsi(
        sentiment_score,
        time_weight,
        source_weight
    )

    print(f"Final Sentiment Index = {fsi}")