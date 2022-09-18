import os
from datetime import date
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser
import allure


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def create_driver(func) -> webdriver:
    USER = os.getenv('LOGIN')
    KEY = os.getenv('KEY')
    APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')

    desired_capabilities = {
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "deviceName": "Google Pixel 3",
        "os_version": "9.0",
        "platformName": "android",
        "project": "Browserstack project",
        "build": "browserstack-build-" + str(date.today()),
        "name": "android_test " + str(date.today())
    }

    return webdriver.Remote(
        command_executor=f"http://{USER}:{KEY}@{APPIUM_BROWSERSTACK}/wd/hub",
        desired_capabilities=desired_capabilities
    )
