#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 个人信息页面
from app.page.base_page import BasePage
from app.page.edit_page import EditPage


class ContentPage(BasePage):

    def click_to_content(self):
        self.driver.find_element_by_id('com.tencent.wework:id/hxm').click()
        return EditPage(self.driver)