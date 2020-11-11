#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 个人信息编辑成员页面
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.contactadd_page import ContactAddPage


class EditPage(BasePage):

    def click_edit_member(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return ContactAddPage(self.driver)