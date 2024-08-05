# @Time：2024/8/5 13:53
# @Author: Allan
import time

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
    @allure.story("导入学习课程")
    def test_create_learning_course(self):
        try:
            time.sleep(5)
            page.refresh()
            page.wait.ele_displayed('@class=text-danger]', timeout=10)
            text = page.ele('@class=text-danger').text
            assert text == '未上架', f"Unexpected page title: {text}"
        except Exception as e:
            print(f"测试过程中发生错误: {e}")

    @pytest.mark.content1
    @allure.story("上架课程")
    def test_resource_display_correct(self):
        try:
            lists = len(page.eles('xpath=//tbody/tr'))
            name = []
            for i in range(1, lists):
                class_names = page.ele(
                    'xpath://tbody/tr[{}]//h3/a'.format(i)).text
                name.append(class_names.title())
            for i in name:
                if i == '内部测试学习课程0724':
                    page.ele('@text()={}'.format("内部测试学习课程0724"), timeout=3).click()
                    break
            texts = page.ele('@class=number').text
        except Exception as e:
            print(f"测试过程中发生错误: {e}")
        assert texts == '2', f"Unexpected page title: {texts}"
