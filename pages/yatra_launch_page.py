"""
This is Yatra launch page, Here we are doing
1.Entering departure from data
2.Entering going to data
3.Entering departure data
4.Clicking search button
"""
import logging
from time import sleep
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from pages.search_flights_result_page import SearchFlightResult
from utils.utils import Utils

class LaunchPage(BaseDriver):
    log = Utils.custom_logger(loglevel=logging.WARNING)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        # self.wait = wait

    #LOCATORS:- #Depart from locator
    DEPART_FROM_FIELD = "//p[.='Departure From']"
    DEPART_FROM_FIELD1 = "input-with-icon-adornment"
    DEPART_FROM_FIELD2 = "//li[@class='css-1546kn3']"
#############################################################################################################
    GOING_TO_FIELD = "//p[.='Going To']"
    GOING_TO_FIELD1 = "input-with-icon-adornment"
    GOING_TO_FIELD2 = "//li[@class='css-1546kn3']"
##############################################################################################################
    SELECT_DATA_FIELD = "//div[@class='css-w7k25o']"
    ALL_DATES = "//div[@class='react-datepicker__month-container']//div[@aria-selected='false']"
    SEARCH_BUTTON = "//button[normalize-space()='Search']"

    def get_depart_from_field1(self): #clickable locator
        return self.wait_until_element_is_clickable("xpath",self.DEPART_FROM_FIELD)
    def get_depart_from_field2(self): #entering data in depart from field locator
        return self.driver.find_element("id", self.DEPART_FROM_FIELD1)
    def get_depart_from_field3(self): #selecting data from the list locator
        return self.driver.find_element("xpath",self.DEPART_FROM_FIELD2)

    def get_going_to_field1(self):
        return self.wait_until_element_is_clickable("xpath",self.GOING_TO_FIELD)
    def get_going_to_field2(self):
        return self.wait_until_element_is_clickable("id",self.GOING_TO_FIELD1)
    def get_going_to_field3(self):
        return self.wait_until_element_is_clickable("xpath",self.GOING_TO_FIELD2)

    def get_departure_data(self):
        return self.wait_until_element_is_clickable("xpath",self.SELECT_DATA_FIELD)

    def get_search_button(self):
        return self.driver.find_element("xpath",self.SEARCH_BUTTON)

    def enter_Depart_From_Location(self,depart_location):
        self.get_depart_from_field1().click()
        self.get_depart_from_field2().send_keys(depart_location)
        sleep(2)
        self.get_depart_from_field3().send_keys(Keys.ENTER)

    def enter_Going_To_Location(self,going_to_location):
        self.get_going_to_field1().click()
        self.get_going_to_field2().send_keys(going_to_location)
        sleep(2)
        self.get_going_to_field3().send_keys(Keys.ENTER)

    sleep(2)
    def selecting_data(self,select_date):
        self.get_departure_data().click()
        sleep(5)
        all_date =  self.driver.find_elements("xpath",self.ALL_DATES)
        for date in all_date:
            if date.get_attribute("aria-label") == select_date:  #Choose Thursday, July 17th, 2025
                date.click()
                sleep(4)
                break

    def search_button(self):
        self.get_search_button().click()
        sleep(40)

    def search_flight(self,departlocation,goingtolocation,departuredata):
        self.enter_Depart_From_Location(departlocation)
        self.enter_Going_To_Location(goingtolocation)
        self.selecting_data(departuredata)
        self.search_button()

        search_flights_result = SearchFlightResult(self.driver)
        return search_flights_result



