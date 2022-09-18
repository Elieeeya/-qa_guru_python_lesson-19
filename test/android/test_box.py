from test.conftest import *
from test.conftest import create_driver
from util.attachment import add_video


@allure.tag('Browserstack mobile')
@allure.title('Wikipedia search BrowserStack')
def test_search_wikipedia():
    browser.config.driver = create_driver(test_search_wikipedia)

    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))
    add_video(browser)
    browser.quit()


@allure.tag('Browserstack mobile homework')
@allure.title('Open Wikipedia from Google in Android app')
def test_open_wikipedia():
    browser.config.driver = create_driver(test_search_wikipedia)
    browser.element((AppiumBy.CLASS_NAME, "android.widget.LinearLayout")).click()
    browser.element((AppiumBy.CLASS_NAME, "android.widget.EditText")).type("Wikipedia")
    browser.all((AppiumBy.CLASS_NAME, "android.view.View")).should(have.size_greater_than(0))
    add_video(browser)
    browser.quit()
