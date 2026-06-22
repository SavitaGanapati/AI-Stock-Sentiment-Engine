import requests
from bs4 import BeautifulSoup


def get_et_headlines():

    url = "https://economictimes.indiatimes.com/markets"

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

    return list(set(headlines))


if __name__ == "__main__":

    headlines = get_et_headlines()

    print("\nTop Headlines:\n")

    for headline in headlines[:10]:
        print(headline)