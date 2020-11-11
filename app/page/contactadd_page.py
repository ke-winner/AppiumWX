#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from app.page.member_invite_menu_page import MemberInviteMenuPage

from app.page.base_page import BasePage


class ContactAddPage(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver

    # 需要将参数抽离出来
    def add_contact(self, name, gender, phonenum):
        # 设置 【用户名】【性别】【手机号】
        self.find(MobileBy.XPATH,
                  "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH,
                  '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)
        # 点击【保存】
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)

    def click_del_member(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        from app.page.adresslist_page import AddressListPage
        return AddressListPage(self.driver)