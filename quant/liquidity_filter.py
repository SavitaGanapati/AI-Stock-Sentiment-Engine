def liquidity_check(
        market_cap,
        avg_volume):

    if (
        market_cap > 5000
        and avg_volume > 100000
    ):

        return "PASS"

    else:

        return "FAIL"


if __name__ == "__main__":

    result = liquidity_check(
        market_cap=250000,
        avg_volume=500000
    )

    print(result)