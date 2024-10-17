import pytest
import allure

from common.logger import logger
from common.yaml_config import GentConf
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
from config.college.PublicMethods import PublicMethods


@pytest.fixture(scope="class", autouse=True)
def some_data():
    PublicMethods().sponsor_login(GentConf().get_env("student_account"), GentConf().get_env("code"))
    yield
    sponsor_page.close()


sponsor_page = DrissionpageDriverConfig().driver_config()


@allure.feature("主办方")
class TestSponsor:
    @pytest.mark.sponsor
    @allure.story("主办方")
    def test_overall_overview(self):
        try:
            number = sponsor_page.ele('@class=number').text
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")
        assert number == '3', f"Unexpected page title: {number}"

    @pytest.mark.sponsor
    @allure.story("院校管理")
    def test_school_management(self):
        try:
            sponsor_page.ele('@data-id=2301').click()
            name_institution = sponsor_page.ele('@data-toggle=popover').text
            print(name_institution)
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")
        assert name_institution == "华北水利水电大学江淮校区", f"Unexpected page title: {name_institution}"
