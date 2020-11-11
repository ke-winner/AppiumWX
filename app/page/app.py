#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
app.py 模块，存放app相关的一些操作。
比如 启动应用，重启应用，停止应用，进入到首页
"""
import yaml
from appium import webdriver

from app.page.base_page import BasePage
from app.page.main_page import MainPage

"""使用yaml方式传入caps所需要的相关值"""
with open('../datas/caps.yaml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']

class AppPage(BasePage):

    def start(self):
        """为了避免第二次安装服务影响时间，对driver进行判断，如果已经存在，不再重复启动"""
        if self.driver == None:
            # 启动app
            # 定义了一个字典
            # caps = {}
            # caps["platformName"] = "Android"
            # caps["deviceName"] = "hogwarts"
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # # noReset 保留缓存， 比如登录状态
            # caps["noReset"] = "True"
            # # 不停止应用，直接运行测试用例
            # # caps["dontStopAppOnReset"] = "true"
            # caps['skipDeviceInitialization'] = 'true'
            # caps['skipServerInstallation'] = 'true'
            # # caps["settings[waitForIdleTimeout]"] = 0
            # # 关键  localhost:4723  本机ip:server端口
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)

        else:
            self.driver.launch_app()
         # self.driver.start_activity(package,activity)
        self.driver.implicitly_wait(5)

        return self

    def restart(self):
        # 重启 app
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        # 停止 app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入到首页
        return MainPage(self.driver)