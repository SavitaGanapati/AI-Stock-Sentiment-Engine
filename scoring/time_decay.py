import math


def calculate_time_weight(days_old, decay_rate=0.2):

    weight = math.exp(-decay_rate * days_old)

    return weight


if __name__ == "__main__":

    for days in [0, 1, 3, 7, 14]:

        weight = calculate_time_weight(days)

        print(
            f"{days} days old -> Weight = {weight:.4f}"
        )