def calculate_momentum(
        return_1m,
        return_3m):

    if (
        return_1m > 5
        and return_3m > 15
    ):

        return "Strong Momentum"

    elif (
        return_1m > 0
        and return_3m > 0
    ):

        return "Moderate Momentum"

    else:

        return "Weak Momentum"


if __name__ == "__main__":

    result = calculate_momentum(
        return_1m=8,
        return_3m=20
    )

    print(result)