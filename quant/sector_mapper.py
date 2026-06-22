def get_sector_mapping():

    sector_map = {

        "Fed Rate Cuts": {
            "sector": "IT",
            "stocks": [
                "INFY.NS",
                "TCS.NS",
                "WIPRO.NS",
                "HCLTECH.NS"
            ]
        },

        "Crude Oil Spike": {
            "sector": "Oil & Gas",
            "stocks": [
                "ONGC.NS",
                "OIL.NS"
            ]
        },

        "Defense Spending": {
            "sector": "Defense",
            "stocks": [
                "HAL.NS",
                "BEL.NS",
                "BDL.NS"
            ]
        }

    }

    return sector_map


if __name__ == "__main__":

    mappings = get_sector_mapping()

    for theme, details in mappings.items():

        print(f"\nTheme: {theme}")

        print(f"Sector: {details['sector']}")

        print(f"Stocks: {details['stocks']}")