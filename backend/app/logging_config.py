import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Create a logger for our app
    logger = logging.getLogger("bank")
    logger.setLevel(logging.INFO)
    return logger


logger = setup_logging()