class element:
    # #为ID定位
    确认按钮 = "#ajax-change-confirm-publish-ok"
    上架按钮 = '#postCourse'
    整体概况 = '@class=title'
    保存按钮 = '@class=btn btn-primary'
    选择证书 = 'xpath://*[@id="certmodel-certid"]/option[2]'
    证书下来框 = '#certmodel-certid'
    证书未设置按钮 = 'xpath:/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div/div/a'
    选择试卷确认按钮 = '@class=btn btn-primary relation-course'
    选择第一个试卷 = 'xpath://tbody/tr[1]/td[1]/label/span'
    添加试卷按钮 = '@class=btn btn-primary addForm'
    试考试卷tab栏 = 'xpath://*[@id="myTab"]/li[2]/a'
    # 课程供应商主页
    课程供应商主页 = 'https://content-fbt-uat.class-demo.com/supply/index/index'
    URL = '#site-url'

    def Tab(self):
        证书课程TAB栏 = 'xpath://div[@class="nav-tab"]/a[{}]'.format(self)
        return 证书课程TAB栏

    def certificate_course_selection(self):
        证书课程选择 = 'xpath://ul[@class="list-course-card hover-border"]/li[{}]'.format(self)
        return 证书课程选择
    立即加购 = '@class=btn btn-warning buy'
    证书加购状态 = "@class=handle"
    加入课程 = '@class=btn btn-primary  buy-dialog-ok'
    加入后的证书课程名称 = '@class=text text-overflow'
    资源总数 = 'xpath://html/body/div[1]/main/div/div/div/div/div[4]/div[1]/div[2]/div[1]/div[1]'
