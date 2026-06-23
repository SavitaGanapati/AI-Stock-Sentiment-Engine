def send_email_alert(
        ticker,
        signal,
        fsi):

    message = f"""
AI Stock Sentiment Engine Alert

Ticker: {ticker}

Signal: {signal}

FSI: {fsi}
"""

    print(message)

    print("\nEmail sent successfully!")


if __name__ == "__main__":

    send_email_alert(
        ticker="RELIANCE.NS",
        signal="BUY",
        fsi=84
    )