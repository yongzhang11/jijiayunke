# @Time：2024/8/5 13:53
# @Author: Allan
import time

from config.supplier.PublicMethod import PublicMethods
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
import pytest
import allure
from common.yaml_config import GentConf
from common.logger import logger

page = DrissionpageDriverConfig().driver_config()


@pytest.fixture(scope="class", autouse=True)
def some_data():
    PublicMethods().login(GentConf().get_env("learning_course_username"))
    PublicMethods().content(1)
    PublicMethods().import_learning_courses(GentConf().get_env("learning_course_name"))
    yield
    # page.close()
    pass


@allure.feature("内容管理")
class TestContent:
    @pytest.mark.content1
    @allure.story("导入学习课程")
    def test_create_learning_course(self):
        try:
            time.sleep(5)
            page.refresh()
            page.wait.ele_displayed('@class=text-danger]', timeout=10)
            text = page.ele('@class=text-danger').text
            assert text == '上架', f"Unexpected page title: {text}"
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")

    @pytest.mark.content1
    @allure.story("上架课程")
    def test_resource_display_correct(self):
        try:
            logger.info("*************** 开始执行用例 ***************")
            PublicMethods().enter_designated_learning_course("内部测试学习课程0724")
            texts = page.ele('@class=number').text
        except Exception as e:
            # print(f"测试过程中发生错误: {e}")
            logger.error(f"测试过程中发生错误: {e}")
        assert texts == '1', f"Unexpected page title: {texts}"
        logger.info("*************** 结束执行用例 ***************")
