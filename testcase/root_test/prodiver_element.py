class element:
    # #为ID定位
    def select(self):
        跳转 = 'text:{}'.format(self)
        return 跳转

    def select_xpath(self):
        内容供应商创建 = 'xpath://*[@id="nav-side"]/ul/li[{}]'.format(self)
        return 内容供应商创建

    def select_supplier_region(self):
        """
        :param level: 区域层级，1-省，2-市，3-区
        :return: 返回元素定位
        """
        供应商区域 = 'xpath=//div[@class="city flex-inline"]/select[{}]'.format(self)
        return 供应商区域
    创建 = '#saveBtn'
    内容供应商名称 = '#addmodel-name'
    内容供应商性质 = 'xpath=//select[@id="addmodel-providernature"]'
    管理员姓名 = '#addmodel-uname'
    管理员手机号 = '#addmodel-username'
    登录密码 = '#addmodel-password'
    内容供应商设置 = '@class=btn btn-outline-primary'
    代理 = '#addmodel-agentmode20'
    直销 = '#addmodel-agentmode10'
    所属代理 = '#select2-addmodel-agentid-container'
    代理列表 = '#select2-addmodel-agentid-results'
    地址 = '#addmodel-address'
    技能项目 = '#addmodel-scope10'
    云上实验室 = '#addmodel-scope20'
    姓名 = '#addmodel-orgusername'
    手机号 = '#addmodel-username'
    院校性质 = 'xpath=//select[@id="addmodel-orgnature"]'
