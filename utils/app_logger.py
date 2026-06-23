import logging

logging.basicConfig(
    filename="stock_engine.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message):

    logging.info(message)


def log_error(message):

    logging.error(message)


if __name__ == "__main__":

    log_info(
        "AI Stock Sentiment Engine started."
    )

    print(
        "Log entry written successfully."
    )