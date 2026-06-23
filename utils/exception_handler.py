"""
Centralized exception handling utilities.
"""

from utils.app_logger import log_error


def handle_exception(error):

    error_message = (
        f"{type(error).__name__}: {str(error)}"
    )

    log_error(error_message)

    print(
        f"Error occurred: {error_message}"
    )


if __name__ == "__main__":

    try:

        result = 10 / 0

    except Exception as e:

        handle_exception(e)