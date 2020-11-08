import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

'''
adb logcat: 查看手机产生的日志
查看应用包名进程：
    adb logcat | findstr -i  activitymanager
    adb shell dumpsys activity activities | findstr "Run"
    
'''

class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'CE920200701002'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # 弹框处理
        desired_caps['autoGrantPermissions'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['noReset'] = True
        # settings 动态设定appium属性，可变，可以在任何地方修改
        desired_caps["settings[waitForIdleTimeout]"] = 0
        # 本机IP:端口4723，建立客户端和服务端的连接
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_demo(self):
        el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/"
                                                "android.widget.LinearLayout/android.widget"
                                                ".FrameLayout/android.widget.RelativeLayout"
                                                "/android.widget.LinearLayout/android.view.ViewGroup"
                                                "/android.widget.RelativeLayout[3]/"
                                                "android.widget.RelativeLayout/android.widget.TextView")
        el1.click()
        # el2 = self.driver.find_element_by_xpath("")
        # time.sleep(5)

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # use = self.driver.find_element(MobileBy.XPATH, "//*[@text='立即使用']")
        # if use != null:
        #     use.click()
        # settings  提升速度
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 文字包含
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        # 显示等待
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        # assert "外出打卡成功" in self.driver.page_source
        print(self.driver.page_source)
        # 返回首页
        self.driver.back()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='消息']").click()