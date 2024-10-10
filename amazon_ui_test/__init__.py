import logging
import inspect
import selenium.webdriver.support.select
import config
from selenium.webdriver.support.select import Select
class BaseClass:
    def log(self):
        logging.basicConfig(filename="AmazonLoginReport.log",
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S %p'
                            )
        return logging.getLogger()

