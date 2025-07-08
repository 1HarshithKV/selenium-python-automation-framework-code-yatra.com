import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from testcases.conftets import setup
from utils.utils import Utils
from ddt import ddt, data, unpack, file_data

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()
    # @data(("Bangalore","New Delhi","Choose Thursday, July 17th, 2025", "1"), ("Mumbai","New Delhi","Choose Wednesday, July 30th, 2025", "1")) #directly we are ging multiple set of data
    # @unpack

    @file_data("../test_data/testdata.json") #this is for json format
    # @file_data("../test_data/testdata.yaml") #this is for yaml format

    # @data(*Utils.read_data_from_excel(r"C:\Users\AHMED\PycharmProjects\Python313\sampleproject\test_data\testdata.xlsx","Sheet1"))
    # @unpack #"""This format is for reading data from excel sheet"""

    # @data(*Utils.read_data_from_csv(r"C:\Users\AHMED\PycharmProjects\Python313\sampleproject\test_data\testdata.csv"))
    # @unpack # """This format is for reading data from csv file"""
    def test_search_flights_1_stops(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.search_flight(goingfrom, goingto, date) #"Bangalore","New Delhi","Choose Thursday, July 17th, 2025"
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stops(stops)
        stops = self.driver.find_elements("xpath","//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        lenght = len(stops)
        self.log.info(f"length of the selected element is {lenght}")
        self.ut.assertListItemText(stops,'1 Stop')

    # def test_search_flights_2_stops(self):
    #     search_flight_result = self.lp.search_flight("New York", "New Delhi", "Choose Sunday, July 20th, 2025")
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights_by_stops('2')
    #     stops = self.driver.find_elements("xpath","//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
    #     lenght = len(stops)
    #     print(f"length of the selected element is {lenght}")
    #     self.ut.assertListItemText(stops, "2 Stop")

        # for stop in stops:
        #     print("The text is: " + stop.text)
        #     assert stop.text.startswith("1 Stop")
        #     # stop.text == '1 Stop'
        #     print("Assert Pass")



