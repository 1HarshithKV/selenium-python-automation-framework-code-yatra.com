"""
This is Yatra's flight search page
1.Selecting 1 Stop and validating
"""
import logging
from time import sleep
from base.base_driver import BaseDriver
from utils.utils import Utils

class SearchFlightResult(BaseDriver):
    log = Utils.custom_logger(loglevel=logging.WARNING)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #LOCATORS
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"

    def get_filter_by_1_stop(self):
        self.driver.find_element("xpath",self.FILTER_BY_1_STOP_ICON).click()

    def get_filter_by_2_stop(self):
        self.driver.find_element("xpath",self.FILTER_BY_2_STOP_ICON).click()

    def get_filter_by_non_stop(self):
        self.driver.find_element("xpath",self.FILTER_BY_NON_STOP_ICON).click()

    def filter_flights_by_stops(self,stops):
        if stops == '1':
            self.get_filter_by_1_stop()
            self.log.warning("Selected flights with 1 Stop")
            sleep(3)
        elif stops == '2':
            self.get_filter_by_2_stop()
            self.log.warning("Selected flights with 2 Stop")
            sleep(3)
        elif stops == '0':
            self.get_filter_by_non_stop()
            self.log.warning("Selected non-stop flights")
            sleep(3)
        else:
            self.log.warning("Please provide the valid filters")