# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWX:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'CE920200701002'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # 弹框处理
        desired_caps['autoGrantPermissions'] = True
        # 不停止当前应用，直接运行
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['noReset'] = True
        # settings 动态设定appium属性，可变，可以在任何地方修改，动态页面时使用出去去
        desired_caps["settings[waitForIdleTimeout]"] = 0
        # 本机IP:端口4723，建立客户端和服务端的连接
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_contact(self):
        name = "xiaowang"
        gender = "男"
        phone_num = "12345677777"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text, "手机") and '
                                 'contains(@class, "TextView")]/..'
                                 '//android.widget.EditText').send_keys(phone_num)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(2)
        print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "添加成功" == result
        self.driver.back()

    def test_del_contacts(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='xiaowang']").click()
        self.driver.find_element_by_id('com.tencent.wework:id/hxm').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(2)
        self.driver.find_element_by_id('com.tencent.wework:id/hxw').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys("xiaowang")
        contacts = self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id, 'com.tencent.wework:id') "
                                                            "and contains(@text, 'xiaowang')]")
        assert contacts in self.driver.page_source



        





