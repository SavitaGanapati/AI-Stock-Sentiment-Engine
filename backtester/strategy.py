def generate_signal(
        fsi,
        momentum,
        fundamentals):

    if (
        fsi > 70
        and momentum == "Strong Momentum"
        and fundamentals == "Strong Fundamentals"
    ):

        return "BUY"

    elif fsi < -30:

        return "SELL"

    else:

        return "HOLD"


if __name__ == "__main__":

    signal = generate_signal(
        fsi=82,
        momentum="Strong Momentum",
        fundamentals="Strong Fundamentals"
    )

    print(signal)