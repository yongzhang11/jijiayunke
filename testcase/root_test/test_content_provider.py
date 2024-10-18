import random
import time

import pytest
import allure

from common.logger import logger
from common.yaml_config import GentConf
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
from config.college.PublicMethods import PublicMethods
from prodiver_element import element


@pytest.fixture(scope="class", autouse=True)
def some_data():
    PublicMethods().root_login(GentConf().get_env("root_username"), GentConf().get_env("root_password"))
    yield
    root_page.close()


root_page = DrissionpageDriverConfig().driver_config()
random_number = '1' + ''.join([str(random.randint(0, 9)) for _ in range(10)])


@allure.feature("后台管理")
class TestRootManagement:
    @pytest.mark.RootManagement
    @allure.story("创建内容供应商")
    def test_create_content_provider(self):
        try:
            root_page.ele(element.select('内容供应商管理')).click()
            root_page.ele(element.select_xpath(2)).click()
            root_page.ele(element.创建).click()
            assert '请输入内容供应商名称' in root_page.ele('@class=help-block').texts()
            root_page.ele(element.内容供应商名称).input('内容供应商名称1')
            root_page.ele(element.select_supplier_region(1)).click()
            root_page.ele(element.select_supplier_region(1) + '/option[2]').click()
            root_page.ele(element.select_supplier_region(2)).click()
            root_page.ele(element.select_supplier_region(2) + '/option[2]').click()
            root_page.ele(element.select_supplier_region(3)).click()
            root_page.ele(element.select_supplier_region(3) + '/option[2]').click()
            root_page.ele(element.内容供应商性质).click()
            root_page.ele(element.内容供应商性质 + '/option[8]').click()
            root_page.ele(element.管理员姓名).input('用户名')
            root_page.ele(element.管理员手机号).input('11123444444')
            root_page.ele(element.登录密码).input('jjyk@UAT123')
            root_page.ele(element.创建).click()
            assert '创建成功' in root_page.ele('@class=card-title').text
            time.sleep(0.5)
            root_page.ele(element.内容供应商设置).click()
            root_page.ele('text:发放培训证书').click()
            PublicMethods().delete_supplier_current(root_page)
        except Exception as e:
            logger.error(e)

    @pytest.mark.RootManagement
    @allure.story("主办方管理")
    def test_create_organizer(self):
        try:
            root_page.ele(element.select('主办方管理')).click()
            root_page.ele(element.select('创建主办方')).click()
            root_page.ele(element.内容供应商名称).input('主办方名称1')
            root_page.ele(element.管理员姓名).input('用户名')
            root_page.ele(element.管理员手机号).input(random_number)
            root_page.ele(element.登录密码).input('jjyk@UAT123')
            root_page.ele(element.创建).click()
        except Exception as e:
            logger.error(e)

    @pytest.mark.RootManagement
    @allure.story("院校管理")
    def test_create_organizer(self):
        try:
            root_page.ele(element.select('院校管理')).click()
            root_page.ele(element.select('创建院校')).click()
            root_page.ele(element.内容供应商名称).input('院校名称1')
            root_page.ele(element.select_supplier_region(1)).click()
            root_page.ele(element.select_supplier_region(1) + '/option[2]').click()
            root_page.ele(element.select_supplier_region(2)).click()
            root_page.ele(element.select_supplier_region(2) + '/option[2]').click()
            root_page.ele(element.select_supplier_region(3)).click()
            root_page.ele(element.select_supplier_region(3) + '/option[2]').click()
            root_page.ele(element.院校性质).click()
            root_page.ele(element.院校性质 + '/option[6]').click()
            root_page.ele(element.云上实验室).next(2).click()
            root_page.ele(element.代理).next(2).click()
            time.sleep(0.5)
            root_page.ele(element.所属代理).click()
            time.sleep(0.5)
            root_page.ele(element.代理列表).child(1).click()
            root_page.ele(element.地址).input('大学路')
            root_page.ele(element.姓名).input('用户名')
            root_page.ele(element.手机号).input(random_number)
            root_page.ele(element.登录密码).input('jjyk@UAT123')
            root_page.scroll.to_bottom()
            root_page.ele(element.select('线下支付')).next(1).child(1).child(1).click()
            root_page.ele(element.select('辅导员互动')).next(1).child(1).child(1).click()
            root_page.ele(element.创建).click()
        except Exception as e:
            logger.error(e)

    @pytest.mark.RootManagement1
    @allure.story("院校编辑")
    def test_create_agent(self):
        try:
            root_page.ele(element.select('院校管理')).click()
            root_page.ele(element.select('院校名称1')).next(11).child(1).child(2).click()
            root_page.ele(element.select('院校管理')).click()
            root_page.ele(element.select('院校名称1')).next(10).child(1).child(1).click()
            time.sleep(0.5)
            root_page.ele(element.select('上传自有资源')).next(1).child(1).child(1).click()
            root_page.ele('@class=el-select__input').click()
            root_page.ele('xpath://ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[3]').click()
            root_page.ele('@class=el-select__input').click()
            root_page.ele('text:保存').click()
            root_page.ele('text:功能设置').click()
            # 周期管理
            root_page.ele('#teaching-material-contract').click()
            root_page.ele('text:修改').click()
            root_page.ele('#contract-duration').clear()
            root_page.ele('#contract-duration').input('10')
            root_page.ele('#contract-num').clear()
            root_page.ele('#contract-num').input('10')
            root_page.ele('#contract-endTime').click()
            root_page.ele('@class=table-condensed').child(2).child(5).child(4).click()
            root_page.ele('text:保存').click()
            root_page.ele('text:返回周期管理').click()
            # 教材资源包管理
            root_page.ele('text:教材资源包管理').click()
            root_page.ele('@class=btn btn-outline-primary textBookResourceAdd').click()
            time.sleep(0.5)
            root_page.ele('@class=custom-control-indicator').click()
            root_page.ele('#relation-course').click()
        except Exception as e:
            logger.error(e)
