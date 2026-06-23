def analyze_fundamentals(
        pe_ratio,
        roe,
        debt_to_equity):

    if (
        pe_ratio < 30
        and roe > 15
        and debt_to_equity < 1
    ):

        return "Strong Fundamentals"

    elif (
        pe_ratio < 50
        and roe > 10
    ):

        return "Moderate Fundamentals"

    else:

        return "Weak Fundamentals"


if __name__ == "__main__":

    result = analyze_fundamentals(
        pe_ratio=25,
        roe=18,
        debt_to_equity=0.5
    )

    print(result)