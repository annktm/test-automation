import logging


class BaseClass:
    def log(self):
        logging.basicConfig(filename="AmazonLoginReport.log",
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S %p'
                            )
        return logging.getLogger()

