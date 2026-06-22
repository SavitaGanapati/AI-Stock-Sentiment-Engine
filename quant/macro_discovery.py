def get_macro_themes():

    themes = {

        "Fed Rate Cuts":
        {
            "impact": "Positive",
            "affected_sectors":
            [
                "IT",
                "Banking"
            ]
        },

        "Crude Oil Spike":
        {
            "impact": "Negative",
            "affected_sectors":
            [
                "Paints",
                "Aviation"
            ]
        },

        "Semiconductor Boom":
        {
            "impact": "Positive",
            "affected_sectors":
            [
                "Electronics",
                "Manufacturing"
            ]
        },

        "Defense Spending":
        {
            "impact": "Positive",
            "affected_sectors":
            [
                "Defense"
            ]
        }

    }

    return themes


if __name__ == "__main__":

    themes = get_macro_themes()

    for theme, details in themes.items():

        print(f"\nTheme: {theme}")

        print(
            f"Impact: {details['impact']}"
        )

        print(
            f"Sectors: {details['affected_sectors']}"
        )