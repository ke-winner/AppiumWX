#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 注册信息
    def register(self):
        self.driver.find_element(By.ID, "manager_name").send_keys("tester")
        self.driver.find_element(By.ID, "corp_name").send_keys("keke")
        self.driver.find_element(By.ID, "register_tel").send_keys("12356760001")
        self.driver.find_element(By.ID, "iagree").click()
        self.driver.find_element(By.ID, "submit_btn").click()
        return True


    def register_fail(self):
        self.driver.find_element(By.ID, "manager_name").send_keys("测试人")
        self.driver.find_element(By.ID, "corp_name").send_keys("keke")
        self.driver.find_element(By.ID, "register_tel").send_keys("12356760001")
        self.driver.find_element(By.ID, "iagree").click()
        self.driver.find_element(By.ID, "submit_btn").click()
        return True
