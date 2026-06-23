"""
Centralized exception handling utilities.
"""

from utils.logger import log_error


def handle_exception(error):
    """
    Handle exceptions and log them.

    Parameters
    ----------
    error : Exception
        Exception object to handle.
    """

    error_message = (
        f"{type(error).__name__}: {str(error)}"
    )

    log_error(error_message)

    print(
        f"Error occurred: {error_message}"
    )


if __name__ == "__main__":

    try:

        # Intentional error
        result = 10 / 0

    except Exception as e:

        handle_exception(e)