import allure
import pytest
from hamcrest import equal_to, assert_that


@pytest.mark.smoke
@pytest.mark.positive
@allure.feature("UI home page")
@allure.title("homa page")
def test_ui_open_home_page(app):
    # open page
    home_page = app.home_page().open_page()

    # check title
    assert_that(home_page.get_title(), equal_to("Selenium"))
