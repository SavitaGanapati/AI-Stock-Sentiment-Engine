def explain_signal(
        signal,
        fsi,
        momentum):

    explanation = f"""

Signal: {signal}

FSI Score: {fsi}

Momentum: {momentum}

"""

    return explanation


if __name__ == "__main__":

    print(
        explain_signal(
            signal="BUY",
            fsi=82,
            momentum="Strong"
        )
    )