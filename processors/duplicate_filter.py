def remove_duplicates(headlines):

    unique_headlines = list(set(headlines))

    return unique_headlines


if __name__ == "__main__":

    headlines = [

        "RBI cuts rates by 25 bps",

        "Markets rally after RBI rate cut",

        "RBI cuts rates by 25 bps",

        "Infosys posts strong earnings"

    ]

    filtered = remove_duplicates(headlines)

    print(filtered)