from utils.exception_handler import handle_exception


def test_exception_handler():

    try:

        x = 10 / 0

    except Exception as e:

        handle_exception(e)

        print(
            "Exception handler test passed."
        )


if __name__ == "__main__":

    test_exception_handler()