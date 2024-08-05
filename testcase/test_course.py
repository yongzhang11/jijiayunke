# @Time：2024/8/5 13:53
# @Author: Allan
from config.supplier.PublicMethod import PublicMethods
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
import pytest
import allure

page = DrissionpageDriverConfig().driver_config()


@pytest.fixture(scope="class", autouse=True)
def some_data():
    PublicMethods().login('15639799733')
    PublicMethods().content(1)
    PublicMethods().import_learning_courses("内部测试学习课程0724")
    yield
    page.close()


@allure.feature("内容管理")
class TestContent:
    @pytest.mark.content1
    @allure.title("判断学习课程是否上架")
    @allure.story("加入班级")
    def test_create_learning_course(self):
        text = page.ele('@class=text-danger').text
        assert text == '未上架', f"Unexpected page title: {text}"
