#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.adresslist_page import AddressListPage
from app.page.base_page import BasePage


class MainPage(BasePage):

    """
    BasePage中封装，所以去除
    """
    # def __init__(self,driver):
    #     self.driver = driver

    ## 通讯录全局使用，所以定义为全局变量
    address_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    """由于每次都要使用self.driver，所以需要对其进行init"""
    def goto_message(self):
        """
        进入到消息页
        :return:
        """
        pass

    def goto_address(self) -> AddressListPage:
        """
        进入联系人页
        :return:
        """
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)

    def goto_workspace(self):
        """
        进入工作台
        :return:
        """
        pass

    def goto_me(self):
        """
        进入个人信息
        :return:
        """
        pass
