# @Time：2024/8/3 10:40
# @Author: Allan
import pytest

from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
from common.yaml_config import GentConf
from config.college.PublicMethods import PublicMethods


class Test1:
    @pytest.mark.create
    def test_add(self):
        page = DrissionpageDriverConfig().driver_config()
        PublicMethods().creating_skills_programme_classe(GentConf().get_env("username"), GentConf().get_env("password"),
                                                         GentConf().get_env("skill_project_name"),
                                                         GentConf().get_env("class_name"))
        PublicMethods().share_class(GentConf().get_env("id"), GentConf().get_env("student_name"),
                                    GentConf().get_env("student_account"))
        assert page.title == '技嘉云课·院校 - 概览', f"Unexpected page title: {page.title}"
        page.close()
