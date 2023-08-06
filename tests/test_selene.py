import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "lysenko")
@allure.feature("Задачи в репозитории")
@allure.story("test_selene")
def test_selene_github(browser_size):
    browser.open("https://github.com")

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)
