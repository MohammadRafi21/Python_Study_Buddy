import logging

logging.basicConfig(
    filename= "logs/running_log.log",
    level=logging.INFO,
    format= "%(asctime)s | %(levelname)s | %(message)s"
)