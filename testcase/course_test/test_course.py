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
from DrissionPage.common import Keys
from positioned_element import element

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
            # 课程封面
            page.set.upload_files(r"./file/{}.jpg".format('正在'))
            page.ele('@class=holder').click()
            page.wait.upload_paths_inputted()
            # 选择课程分类
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select[1]').click()
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select['
                '1]/option[3]').click()
            # 保存课程信息
            page.ele('#courseSaveBtn').click()
            # 选择课程级别
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select[2]').click()
            page.ele(
                'xpath:/html/body/div[2]/div/div/div[2]/div/form/div[2]/div/div[2]/div/div[5]/div/div/select['
                '2]/option[4]').click()
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
            page.ele('#createmodel-hostlenattached').input("60")
            # 输入价格
            page.ele('#priceCert').input("0")
            # 保存课程信息
            page.ele('#courseSaveBtn').click()
            # 获取描述信息
            desc = page.ele('@class=desc').text
            logger.info(f"课程描述: {desc}")
            # 点击某个按钮
            page.ele('@class=btn btn-outline-primary').click()
            # 设置培训环节，点击线上课程链接
            page.ele('text:线上课程').children(locator='xpath://span[@class="text-gray"]/a')[0].click()
            # 添加课程
            page.ele('@class=btn btn-primary').click()
            page.ele('#listmodel-name').input('内部测试学习课程0724')
            page.ele(
                'xpath:/html/body/div[1]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span[1]').click()
            page.ele('@class=btn btn-primary addCourse').click()
            page.ele('#ajax-add-ids-confirm-ok').click()
            time.sleep(2)
            page.ele('@class=btn btn-outline-primary').click()
            title = page.ele('@class=title-content').text
            logger.info(f"课程名称: {title}")
            # 考试规则设置
            page.ele('@class=title').click()
            page.ele('text:规则设置').children(locator='xpath://span[@class="text-gray"]/a')[0].click()
            page.ele('#settingmodel-times').click()
            page.ele('@value=3').click()
            page.ele('@class=btn btn-primary').click()
            page.ele('#settingmodel-passscore').input("60")
            page.ele('@class=btn btn-primary').click()
            # 试卷设置
            page.ele('@class=title').click()
            page.ele('xpath://span[@class="text-gray"]/a').click()
            page.ele('@class=btn btn-primary addForm').click()
            kemuxingxi = page.ele('xpath://*[@id="w0"]/div/div').text
            match = re.search(r'（(.*?)）', kemuxingxi).group(1)
            logger.info(f"考试详情: {match}")
            page.ele('@class=btn btn-secondary cancel').click()
            # 添加试卷
            ele = page.ele('@class=jump')
            tab = ele.click.for_new_tab()  # 点击某个链接新建标签页
            tab.ele('@class=btn btn-primary').click()
            tab.ele('#create-paper-name').input('证书课程-{}'.format(current_date))
            tab.ele('#create-paper-examTime').input('120')
            tab.ele('#select2-create-paper-subject-container').click()
            time.sleep(1)
            tab.ele('@class=select2-search__field').input(match)
            tab.actions.key_down('ENTER')  # 输入按键名称
            tab.actions.key_down(Keys.ENTER)  # 从Keys获取按键名称
            tab.ele('@class=btn btn-primary').click()
            tab.ele('@class=btn btn-primary step-btn-final').click()
            tab.ele('@class=cell addItemSub').click()
            tab.ele('@class=form-control score-input spin-val').clear()
            tab.ele('@class=form-control score-input spin-val').input('60')
            tab.ele(
                'xpath:/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/ol/li/div[2]/div[2]/div[1]/div[2]/div/div/p').click()
            tab.ele('xpath://*[@class="edit-type-text"]/div[1]/div[2]/div/div').input('证书课程')
            tab.ele('@class=btn btn-primary success-item').click()
            time.sleep(1)
            tab.ele('@class=btn btn-primary publish-paper').click()
            tab.ele('#paper-publish-ok').click()
            tab.close()
            # 选择试卷(正式)
            page.ele(element.添加试卷按钮).click()
            time.sleep(1)
            page.ele(element.选择第一个试卷).click()
            page.ele(element.选择试卷确认按钮).click()
            # 选择试卷(试考)
            page.ele(element.试考试卷tab栏).click()
            page.ele(element.添加试卷按钮).click()
            time.sleep(1)
            page.ele(element.选择第一个试卷).click()
            page.ele(element.选择试卷确认按钮).click()
            # 设置培训证书
            page.ele(element.整体概况).click()
            page.ele(element.证书未设置按钮).click()
            page.ele(element.证书下来框).click()
            page.ele(element.选择证书).click()
            page.ele(element.保存按钮).click()
            # 证书课程上架
            page.ele(element.整体概况).click()
            page.ele(element.上架按钮).click()
            page.ele(element.确认按钮).click()
        except Exception as e:
            # 捕获异常并记录日志
            logger.error(f"测试过程中发生错误: {e}")
        # 断言描述信息是否符合预期
        assert desc == "证书课程创建成功", f"Unexpected page title: {desc}"
        assert title == "内部测试学习课程0724", f"Unexpected page title: {title}"
    @pytest.mark.content1
    @allure.story("购买证书课程")
    def test_purchase_certificate(self):
        try:
            page.get(element.课程供应商主页)
            ele = page.ele(element.URL)
            tab = ele.click.for_new_tab()  # 点击某个链接新建标签页
            tab.ele(element.Tab(2)).click()
            tab.ele(element.certificate_course_selection(1)).click()
            tab.ele(element.立即加购).click()
            tab.ele(element.加入课程).click()
            tab.close()
        except Exception as e:
            logger.error(f"测试过程中发生错误: {e}")
