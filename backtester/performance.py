def calculate_performance(
        initial_value,
        final_value):

    total_return = (
        (
            final_value
            - initial_value
        )
        / initial_value
    ) * 100

    return round(
        total_return,
        2
    )


if __name__ == "__main__":

    initial_value = 1000000

    final_value = 1185000

    total_return = calculate_performance(
        initial_value,
        final_value
    )

    print(
        f"Total Return: {total_return}%"
    )