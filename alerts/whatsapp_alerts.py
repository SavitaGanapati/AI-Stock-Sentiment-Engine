def send_whatsapp_alert(
        ticker,
        signal,
        fsi):

    message = f"""
WhatsApp Alert

Ticker: {ticker}

Signal: {signal}

FSI: {fsi}
"""

    print(message)

    print("\nWhatsApp notification sent!")


if __name__ == "__main__":

    send_whatsapp_alert(
        ticker="TCS.NS",
        signal="BUY",
        fsi=79
    )