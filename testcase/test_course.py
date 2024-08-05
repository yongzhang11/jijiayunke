# @Time：2024/8/5 13:53
# @Author: Allan
from config.supplier.PublicMethod import PublicMethod
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
import pytest
import allure

page = DrissionpageDriverConfig().driver_config()


@pytest.fixture(scope="class", autouse=True)
def some_data():
    PublicMethod().login('15639799733')
    PublicMethod().content(1)
    PublicMethod().import_learning_courses("内部测试学习课程0724")
    yield
    page.close()


@allure.feature("内容管理")
class TestContent:
    # def setup_class(self):
    #     "每个类之前执行"
    #     PublicMethod().login('15639799733')
    #     PublicMethod().content(1)
    #     PublicMethod().import_learning_courses("内部测试学习课程0724")
    #
    # def teardown_class(self):
    #     "每个类之后执行"
    #     page.close()
    @pytest.mark.content
    @allure.title("判断学习课程是否上架")
    @allure.story("加入班级")
    def create_learning_course(self):
        text = page.ele('@class=text-danger').text
        assert text == '未上架', f"Unexpected page title: {text}"
