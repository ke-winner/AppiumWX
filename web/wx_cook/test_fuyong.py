import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestFuyong:
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self, method):
        # self.driver.quit()
        pass

    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853089205264'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'FtmoFNSv0E6o5jzeGauOJK1p5I6-BY4sMVq7s8Dqn1CYjLIkPujCG0XdjTi2QhHOdmQVcitnh_Bo5NDnJZiyW6RgmmHNLzptBoIq-9xgdBCXhxm3dOCZ1RNzURgbj58v96k8fUAW9F6rHfXst69vEit4cJF8YuSVRzoRwibZAY38ucvzeAOO8O-qDWfCtwubESCse4hYsd2caDvQgMBmJ2XP-alGtAqopzY6TMw3cT48riKuPKPYtL4THmtwTad21-ZEv-XtcH5mJUNXskhbGA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853089205264'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325123169904'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635311109, 'httpOnly': False,
        #                                     'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
        #                                     'secure': False, 'value': '1603722350,1603723738,1603723789,1603775109'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '2123906904'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a2887647'},
        #     {'domain': '.qq.com', 'expiry': 1603861515, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.421280773.1603716988'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603803039, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '7mdmvki'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1603775109'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '0273598'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'N5nmLtSou-TwDTmnccT0s6RgXXpsG8TemJqORQ0cHEoLAQYsvTggF1HvHhcvZoxD'},
        #     {'domain': '.qq.com', 'expiry': 1666847115, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.2075675907.1603368611'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634904591, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1606367275, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'}]
        db = shelve.open("cookies")
        cookies = db['cookie']
        # db['cookie'] = cookies
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()  # Ë¢ÐÂÒ³Ãæ
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys('E://test.xls')
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "test.xls" == filename
        sleep(3)

