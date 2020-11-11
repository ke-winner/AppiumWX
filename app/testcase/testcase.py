#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from app.page.app import AppPage


class TestContact:

    def setup(self):
        self.app = AppPage()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = "hogwarts__004"
        gender = "男"
        phonenum = "13500000003"
        result = self.main.goto_address().\
            click_addmember().\
            add_member_menual().\
            add_contact(name, gender, phonenum).\
            get_toast()
        assert '添加成功' == result

    def test_del_contact(self):
        name = "点点"
        self.main.goto_address().click_del_member(name).\
            click_to_content().\
            click_edit_member().\
            click_del_member()
        sleep(2)
        assert name in self.driver.page_source



