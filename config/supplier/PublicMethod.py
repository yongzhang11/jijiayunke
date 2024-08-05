from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig

page = DrissionpageDriverConfig().driver_config()


class PublicMethod:
    def login(self, username='15639799733', password='8NBWmJ'):
        page.get("https://content-fbt-uat.class-demo.com/login")
        page.ele('@class=form-control').input(username)
        page.ele('#pwd').input(password)
        page.ele('@class=btn btn-primary btn-block ').check()

    """
    1:学习课程
    2：证书课程
    3：技能项目
    4：教材资源包
    5：直播管理
    """

    def content(self, type):
        page.ele('xpath://ul[@class="submenu"]/li[{}]'.format(type)).check()

    def import_learning_courses(self, zipname):
        page.ele('@class=btn btn-outline-primary import-course').check()
        page.set.upload_files('./file/{}.zip'.format(zipname))
        page('#ready-uploadZipCourse').click()
        page.wait.upload_paths_inputted()
        page.ele('#importBtnZipCourse').click()
        page.ele('#course-alert-import-unpack-ok').click()


