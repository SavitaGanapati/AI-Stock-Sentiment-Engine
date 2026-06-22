def get_source_weight(source):

    source_weights = {

        "Company Filing": 1.00,

        "Reuters": 0.95,

        "Moneycontrol": 0.85,

        "Economic Times": 0.85,

        "Livemint": 0.80,

        "Reddit": 0.55,

        "Twitter/X": 0.45

    }

    return source_weights.get(source, 0.50)


if __name__ == "__main__":

    sources = [

        "Moneycontrol",

        "Economic Times",

        "Reddit",

        "Twitter/X"

    ]

    for source in sources:

        weight = get_source_weight(source)

        print(f"{source} → Weight = {weight}")