# @Time：2024/8/5 13:53
# @Author: Allan
import datetime
import re
import time

from config.supplier.PublicMethod import PublicMethods
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
import pytest
import allure
from common.yaml_config import GentConf
from common.logger import logger

page = DrissionpageDriverConfig().driver_config()
current_date = datetime.datetime.now().strftime("%Y-%m-%d")


@pytest.fixture(scope="class", autouse=True)
def some_data():
    PublicMethods().login(GentConf().get_env("learning_course_username"))
    PublicMethods().content(1)
    yield
    # page.close()
    pass


@allure.feature("内容管理")
class TestContent:
    @pytest.mark.content2
    @allure.story("导入学习课程")
    def test_create_learning_course(self):
        try:
            PublicMethods().import_learning_courses(GentConf().get_env("learning_course_name"))
            time.sleep(5)
            page.refresh()
            page.wait.ele_displayed('@class=text-danger]', timeout=10)
            text = page.ele('@class=text-danger').text
            assert text == '未上架', f"Unexpected page title: {text}"
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")

    @pytest.mark.content2
    @allure.story("上架学习课程")
    def test_resource_display_correct(self):
        try:
            logger.info("*************** 开始执行用例 ***************")
            PublicMethods().enter_designated_learning_course("内部测试学习课程0724")
            texts = page.ele('@class=number').text
            logger.info(f"当前资源总数: {texts}")

            page.ele('@text()=基本信息').click()
            page.ele('@class=btn btn-primary').click()
            page.ele('#editmodel-direction').click()
            page.ele('xpath://*[@id="editmodel-direction"]/option[3]').click()
            # time.sleep(2)
            page.ele('#courseSaveBtn').click()
            time.sleep(1)
            page.ele(
                'xpath:/html/body/div[1]/div/div/div[2]/div/form/div/div/div[2]/div/div[5]/div/div/select[2]').click()
            page.ele(
                'xpath:/html/body/div[1]/div/div/div[2]/div/form/div/div/div[2]/div/div[5]/div/div/select[2]/option[4]').click()
            page.ele('#courseSaveBtn').click()

            page.ele('xpath://*[@id="nav-side"]/ul/li[4]/ul/li[2]/a').click()
            daxiao = page.ele('xpath:/html/body/div[1]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[4]').text
            while daxiao == "0 M":
                logger.info("视频转码中")
                time.sleep(1)
                page.refresh()
                daxiao = page.ele('xpath:/html/body/div[1]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[4]').text
                if daxiao != "0 M":
                    break
            page.ele('@class=title').click()
            page.ele('@class=btn ml-3 btn-sm btn-outline-primary publish-course').click()
            page.ele('#ajax-change-confirm-publish-course-ok').click()
            banben = page.ele(
                'xpath:/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/span[1]/span[1]').text
            numbers = re.findall(r'\d+', banben)
            page.ele('@class=text-decoration-none text-muted').click()
            banben1 = page.ele('xpath=/html/body/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]').text
            page.ele('@class=text-decoration-none postCourse').click()
            page.ele('#ajax-change-confirm-publish-ok').click()
            time.sleep(4)
            text = page.ele('xpath:/html/body/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[6]/span').text
            logger.info(f"上架状态: {text}")
        except Exception as e:
            # print(f"测试过程中发生错误: {e}")
            logger.error(f"测试过程中发生错误: {e}")
        assert texts == '2', f"Unexpected page title: {texts}"
        assert banben1 == numbers[0], f"Unexpected page title: {banben1}"
        assert text == '已上架', f"Unexpected page title: {text}"
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.content1
    @allure.story("创建证书课程")
    def test_certificate(self):
        try:
            # 打开课程页面
            page.get("https://content-fbt-uat.class-demo.com/supply/index/course?cType=2")

            # 点击创建按钮
            page.ele('@class=btn btn-primary').click()

            # 输入课程名称
            page.ele('#createmodel-name').input("证书课程{}".format(current_date))

            # 选择课程分类
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select[1]').click()
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select[1]/option[3]').click()

            # 保存课程信息
            page.ele('#courseSaveBtn').click()

            # 选择课程级别
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select[2]').click()
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select[2]/option[4]').click()

            # 再次保存课程信息
            page.ele('#courseSaveBtn').click()

            # 滚动到证书课程介绍处
            page.scroll.to_see('@text()={}'.format("证书课程介绍"))

            # 点击编辑框
            page.ele('#edui1_iframeholder').click()

            # 输入课程介绍
            page.ele('xpath:/html/body').input("证书课程{}".format(current_date))

            # 滚动到证书单价处
            page.scroll.to_see('@text()={}'.format("证书单价"))

            # 输入实训时长
            # 实训时长
            page.ele('#createmodel-hostlenattached').input("60")

            # 输入价格
            # 价格
            page.ele('#priceCert').input("0")

            # 保存课程信息
            page.ele('#courseSaveBtn').click()

            # 获取描述信息
            desc = page.ele('@class=desc').text

            # 点击某个按钮
            page.ele('@class=btn btn-outline-primary').click()

            # 设置培训环节，点击线上课程链接
            # 设置培训环节
            page.ele('text:线上课程').children(locator='xpath://span[@class="text-gray"]/a')[0].click()
        except Exception as e:
            # 捕获异常并记录日志
            logger.error(f"测试过程中发生错误: {e}")
        # 断言描述信息是否符合预期
        assert desc == "证书课程创建成功", f"Unexpected page title: {desc}"

