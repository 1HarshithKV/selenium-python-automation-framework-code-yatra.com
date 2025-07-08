# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
#
# class DemoExplicitWait:
#     def demo_exp_wait(self):
#         driver.get("https://www.yatra.com/")
#         sleep(5)
#         driver.maximize_window()
#         wait=WebDriverWait(driver,40)
#         sleep(2)
#
#         #entering going from
#         d=driver.find_element("xpath","//p[.='Departure From']")
#         d.click()
#         dd=driver.find_element("id","input-with-icon-adornment")
#         dd.send_keys("New York")
#         sleep(2)
#         driver.find_element("xpath","//li[@class='css-1546kn3']").send_keys(Keys.ENTER)
#
#         #entering going to data
#         g=driver.find_element("xpath","//p[.='Going To']")
#         g.click()
#         gg = (driver.find_element("id","input-with-icon-adornment"))
#         gg.send_keys("New Delhi")
#         sleep(3)
#         driver.find_element("xpath", "//li[@class='css-1546kn3']").send_keys(Keys.ENTER)
#
#         # search_results = wait.until(EC.presence_of_all_elements_located(driver.find_element("xpath","//li[@class='css-1546kn3']")))
#         # for result in search_results:
#         #     if "New Delhi" in result.text:
#         #         result.click()
#         #         break
#
#         #selecting date
#         sleep(2)
#         origin = driver.find_element("xpath","//div[@class='css-w7k25o']")
#         origin.click()
#         sleep(4)
#         all_date = driver.find_elements("xpath","//div[@class='react-datepicker__month-container']//div[@aria-selected='false']")
#         for date in all_date:
#             if date.get_attribute("aria-label") == "Choose Thursday, July 17th, 2025":
#                 date.click()
#                 sleep(2)
#                 break
#
#         # searching
#         driver.find_element("xpath","//button[normalize-space()='Search']").click()
#         sleep(40)
#
#         # #syncronisation
#         # wtime = driver.find_element("xpath","//a[@aria-label='My Account']")
#         # wait.until(EC.presence_of_element_located(wtime))
#
#         #scrolling:
#         driver.execute_script("window.scrollBy(0,900)")
#         sleep(2)
#         driver.execute_script("window.scrollTo(900,0)")
#         sleep(2)
#
#         #lenght of all stops
#         all_stops = driver.find_elements("xpath","//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
#         print(len(all_stops))
#
#         #clicking on 1 stop
#         driver.find_element("xpath","//p[@class='font-lightgrey bold'][normalize-space()='2']").click()
#         sleep(3)
#         stops = driver.find_elements("xpath","//span[@class='mob-duration']")
#         for i in stops:
#             print(i.text)
#         print(len(stops))
#         sleep(5)
#         for stop in stops:
#             print("The text is: "+stop.text)
#             assert stop.text == '1 Stop'
#             print("Assert Pass")
#
#         # closing browser
#         driver.close()
#
# d=DemoExplicitWait()
# d.demo_exp_wait()






























