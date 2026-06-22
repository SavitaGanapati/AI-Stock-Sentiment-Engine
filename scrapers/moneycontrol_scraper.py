import requests
from bs4 import BeautifulSoup


def get_moneycontrol_headlines():

    url = "https://www.moneycontrol.com/news/business/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print("Status code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    for a in soup.find_all("a"):
        text = a.get_text(strip=True)

        if len(text) > 40:
            headlines.append(text)

    return headlines


if __name__ == "__main__":

    headlines = get_moneycontrol_headlines()

    print("\nTop Headlines:\n")

    for headline in headlines[:10]:
        print(headline)