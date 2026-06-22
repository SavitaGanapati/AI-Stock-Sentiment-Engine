def detect_sentiment_shift(previous_score, current_score):

    change = current_score - previous_score

    if change > 0.5:

        return "Strong Positive Shift"

    elif change < -0.5:

        return "Strong Negative Shift"

    else:

        return "Normal"


if __name__ == "__main__":

    previous_score = 0.15

    current_score = 0.82

    result = detect_sentiment_shift(
        previous_score,
        current_score
    )

    print(result)