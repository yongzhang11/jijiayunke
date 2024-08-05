# @Time：2024/8/3 10:40
# @Author: Allan
import pytest
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
from common.yaml_config import GentConf
from config.college.PublicMethods import PublicMethods
import allure

page = DrissionpageDriverConfig().driver_config()


@pytest.fixture(scope="class", autouse=True)
def browser():
    pass
    yield
    page.close()


@allure.feature("创建班级模块")
class Test1:

    @pytest.mark.create
    @allure.title("创建技能项目并加入班级")
    @allure.story("加入班级")
    def test_add(self):
        try:
            PublicMethods().creating_skills_programme_classe(GentConf().get_env("username"),
                                                             GentConf().get_env("password"),
                                                             GentConf().get_env("skill_project_name"),
                                                             GentConf().get_env("class_name"))
            PublicMethods().share_class(GentConf().get_env("id"), GentConf().get_env("student_name"),
                                        GentConf().get_env("student_account"))
            assert page.title == '技嘉云课·院校 - 概览', f"Unexpected page title: {page.title}"
        except Exception as e:
            print(f"测试过程中发生错误: {e}")

    @pytest.mark.create
    @allure.title("查看学生是否加入班级")
    def test_join_successfully(self):
        try:
            page.get("https://stu-fbt-uat.class-demo.com")
            PublicMethods().clllege_login(GentConf().get_env("student_account"), GentConf().get_env("code"))
            page.ele('@class=study-check ').click()
            element = page.ele('xpath:/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div/div/div[1]/h5/a').text
            last_dash_index = element.rfind('-')
            output_string = element[:last_dash_index + 1]
            print(output_string)
            assert output_string == GentConf().get_env("class_name") + "-", f"Unexpected page title: {element}"
        except Exception as e:
            print(f"测试过程中发生错误: {e}")
