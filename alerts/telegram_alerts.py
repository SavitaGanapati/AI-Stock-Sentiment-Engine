def send_telegram_alert(
        ticker,
        signal,
        fsi):

    message = f"""
Telegram Alert

Ticker: {ticker}

Signal: {signal}

FSI: {fsi}
"""

    print(message)

    print("\nTelegram notification sent!")


if __name__ == "__main__":

    send_telegram_alert(
        ticker="INFY.NS",
        signal="BUY",
        fsi=81
    )