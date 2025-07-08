import os.path
import time

import pytest
from pytest_selenium import driver
from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver import Firefox,FirefoxOptions
# from selenium.webdriver import Edge,EdgeOptions
# from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(autouse=True)
def setup(request):
    o = ChromeOptions()
    o.add_experimental_option("detach",True)
    driver = Chrome(options=o)
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report,"extra", [])
    if report.when == "call":
        extras.append(pytest_html.extras.url("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::","_")+".png"
            # file_name = str(int(round(time.time() * 1000)))+".png"
            destinationFile = os.path.join(report_directory,file_name)
            driver.save_screenshot(destinationFile)
            print("screenshot done")
            if file_name:
                html = '<div><img src"%s" alt="screenshot" style="width:300px;height=200px"'\
                       'onclick="window.open(this.src)"allign="right"/></div>'%file_name
            extras.append(pytest_html.extras.html(html)) #extra.append(pytest_html.extras.html(html))

def pytest_html_report_title(report):
    report.title = "Yatra.com_Automation_Report"

# from time import sleep
# import pytest
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver import Firefox,FirefoxOptions
# from selenium.webdriver import Edge,EdgeOptions
# from selenium.webdriver.support.wait import WebDriverWait
#
# def pytest_addoption(parser):
#     parser.addoption("--browser",action="store", default="chrome", help="Browser to use")
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="session")
# def setup(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="class")
# def setup(request,browser):
#     if browser == "chrome":
#         o = ChromeOptions()
#         driver = Chrome(options=o)
#     elif browser == "firefox":
#         f = FirefoxOptions()
#         driver = Firefox(options=f)
#     elif browser == "edge":
#         e = EdgeOptions()
#         driver = Edge(options=e)
#     else:
#         raise ValueError(f"Unsupported browser:{browser}")
#     driver.get("https://www.yatra.com/")
#     sleep(5)
#     driver.maximize_window()
#     wait=WebDriverWait(driver,40)
#     sleep(2)
#     request.cls.driver=driver
#     request.cls.wait=wait
#     yield
#     driver.quit()