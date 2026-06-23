def explain_stock(
        ticker,
        fsi,
        momentum,
        fundamentals,
        macro_theme):

    explanation = f"""

Ticker: {ticker}

FSI: {fsi}

Momentum: {momentum}

Fundamentals: {fundamentals}

Macro Theme: {macro_theme}

"""

    return explanation


if __name__ == "__main__":

    print(
        explain_stock(
            ticker="RELIANCE.NS",
            fsi=84,
            momentum="Strong",
            fundamentals="Strong",
            macro_theme="Positive"
        )
    )