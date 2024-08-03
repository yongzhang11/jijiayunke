# @Time：2024/8/3 8:14
# @Author: Allan
import time
import re
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
from DrissionPage.common import Keys
import os

page = DrissionpageDriverConfig().driver_config()


class PublicMethods:
    # 院校端登录
    def login(username, password):
        page.get("https://org-fbt-uat.class-demo.com/login")
        page.ele('@class=more').click()
        page.ele('#username').input(username)
        page.ele('#pwd').input(password)
        page.ele('@class=btn btn-primary btn-block ').click()

    """
    username:账号名
    password:密码
    skill:技能项目名称
    class_name:班级名称
    play:付款方式 可取"在线支付"、"线下支付"
    payment_method:由谁付款 1学员自付，2老师代付
    enrolment：允许自主报名 可取 "1开启"、"2不开启"
    """

    def creating_skills_programme_classe(self, username, password, skill, class_name, play="在线支付", payment_method=1,
                                         enrolment="1"):
        PublicMethods.login(username, password)
        page.ele('xpath://ul[@class="submenu"]/li[{}]'.format(2)).click()
        # 创建班级
        page.ele('@class=btn btn-primary').check()
        page.ele('@class=icon').click()
        # 技能项目名称
        page.ele('#indexmodel-name').input(skill)
        page.ele('@class=btn btn-outline-primary').click()
        time.sleep(1)
        page.ele('@class=select-btn').click()
        page.ele('#addmodel-name').input(class_name)
        page.ele('#addmodel-starttime').click()
        # 日期
        page.ele('@data-title=r0c{}'.format(3)).check()
        page.ele('#addmodel-endtime').check()
        # 结束时间
        string_without_spaces = page.ele('#addmodel-direction-span').text
        class_name_suffix = string_without_spaces.replace(" ", "")
        print(class_name_suffix)
        page.ele('xpath://select[@id="addmodel-endtime"]/option[{}]'.format(4)).click()
        page.ele('@text()={}'.format(play), timeout=3).click()
        # page.scroll.to_bottom()
        page.scroll.to_see('@text()={}'.format("开启"))
        if play == "在线支付":
            # 在线支付 1是学员自付 2是老师代付
            page.ele('xpath://ul[@class="list-check"]/li[{}]'.format(payment_method)).click()
        # 允许自主报名,开启和不开启
        page.ele('@text()={}'.format("开启")).input((Keys.CTRL, '-'))  # ctrl+减号
        page.ele('xpath://*[@id="w0"]/div[3]/div/div[7]/div/div[1]/label[{}]/span[2]'.format(enrolment)).click()
        page.ele('#saveBtn').check()
        time.sleep(2)
        PublicMethods().class_import_students(username, password, class_name, class_name_suffix)

    """
    指定班级导入学员
    username:系统登录账户
    password:系统登录密码 
    class_name:班级名称
    class_management:班级操作 1概览|2包含课程|3学员管理|4付费情况|5学习情况|6考试管理
    """

    def class_import_students(self, username, password, class_name, class_name_suffix, class_management=3):
        page.get("https://org-fbt-uat.class-demo.com/research/index/index")
        try:
            page.ele('@class=main-nav-list').texts()
        except:
            PublicMethods().login(username, password)
            page.get("https://org-fbt-uat.class-demo.com/research/index/index")
        lists = len(page.eles('xpath:/html/body/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr'))
        name = []
        for i in range(1, lists + 1):
            class_names = page.ele(
                'xpath://table[@class="table table-custom table-bordered"]//tr[{}]/td[2]'.format(i)).text
            name.append(class_names.title())
        for i in name:
            if i == class_name + class_name_suffix:
                page.ele('@text()={}'.format(class_name + class_name_suffix), timeout=3).click()
                break
        page.ele('xpath://ul[@class="main-nav-list"]/li[{}]'.format(class_management)).click()
        PublicMethods().import_function()
        PublicMethods().class_status()

    # 导入功能
    def import_function(self=None):
        time.sleep(1)
        page.ele('xpath://span[@class="buttons-wrapper"]/a[{}]'.format(2)).click()
        # page.set.upload_files('D:\\jijiayunke\\config\\college\\file\\学员导入模板.xlsx')
        # page.set.upload_files('')
        current_directory = os.getcwd()
        print(current_directory)
        page.set.upload_files('./file/学员导入模板.xlsx')
        page('#excelfile-upload-area').click()
        page.wait.upload_paths_inputted()
        page.ele('@text()=导入').click()
        time.sleep(3)
        page.ele('@class=btn  btn-primary').click()

    # 班级状态
    def class_status(self=None):
        page.ele('xpath://ul[@class="main-nav-list"]/li[{}]'.format(1)).click()
        page.ele("#open_batch").click()
        page.ele('#open_confirm-ok').click()
        return page.url

    """
    分享班级，并加班
    identityNumber：证件号
    name：姓名
    student_account:学员账号
    code：验证码
    """

    def share_class(self, identityNumber, name, student_account, code=111111):
        url = PublicMethods().class_status()
        match = re.search(r'\d+', url).group(0)
        # print(match)
        page.get('https://org-fbt-uat.class-demo.com/course/my/batch-view?i={}'.format(match))
        class_password = page.ele('xpath://ul[@class="list-info list-info-two-column"]/li[5]//span/b').text
        page.ele('@class=class-share-info').click()
        learning_address = page.ele('xpath://span[@class="text student-study-address"]/a').attr('href')
        tab = page.new_tab()
        tab.get(learning_address)
        tab.ele('#pwd').input(class_password)
        tab.ele('#identityNumber').input(identityNumber)
        tab.ele('#name').input(name)
        try:
            tab.ele('#joinClass').click()
            tab.ele('@class=user-name').text
        except:
            tab.ele('#joinClass').click()
            time.sleep(2)
            tab.ele('#login-phone').click()
            tab.ele('#loginform-phone').input(student_account)
            tab.ele('#loginform-code').input(code)
            tab.ele('#mobile-login-idm-ok').click()
            time.sleep(2)
            tab.ele('#joinClass').click()
        tab.close()
