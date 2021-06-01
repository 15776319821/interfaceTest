import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import time
# import pythoncom
import readExcel
# pythoncom.CoInitialize()
from common.Log import logger

# url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase002.xlsx', 'message')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method, status, goType, userIds, targetLinkUrl, defaultContent):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :param status
        :param goType
        :param userIds
        :param targetLinkUrl
        :param defaultContent
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.status = str(status)
        self.goType = str(goType)
        self.userIds = str(userIds)
        self.targetLinkUrl = str(targetLinkUrl)
        self.defaultContent = str(defaultContent)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test002case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        # url1 = "http://www.xxx.com/login?"
        # new_url = url1 + self.query

        data = {
            "userIds": str(self.userIds),
            "countryGroupIds": "",
            "userTypeIds": "",
            "sendTime": '',
            "goType": self.goType,
            "targetLinkUrl": self.targetLinkUrl,
            "defaultImgUrl": "",
            "defaultContent": self.defaultContent,
            "status": 1
        }
        # time.sleep(5)
        print(data)
        info = RunMain().run_main('post', 'https://report.lamour.live/pp-admin/api/basic/notice/config/?', json.dumps(data))# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        # print(url)
        ss = json.loads(info)# 将响应转换为字典格式
        print(ss)
        logger.info(str(ss))
        if self.case_name == 'login':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        # if self.case_name == 'login_error':# 同上
        #     self.assertEqual(ss['code'], -1)
        # if self.case_name == 'login_null':# 同上
        #     self.assertEqual(ss['code'], 10001)


