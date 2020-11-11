#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.content_page import ContentPage
from app.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver

    def click_addmember(self) -> MemberInviteMenuPage:
        """
        点击添加联系人页面：滚动查找【添加成员】
        :return:
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()

        return MemberInviteMenuPage(self.driver)

    def click_del_member(self, member) -> MemberInviteMenuPage:
        """
        联系人页面：滚动查找【要删除的人名】
        :return:
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{name}").instance(0));'.format(name=member)).click()

        return ContentPage(self.driver)