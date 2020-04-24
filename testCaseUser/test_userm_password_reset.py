import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
from testCase.login import Get_Token
# pythoncom.CoInitialize()
import common.Log
log = common.Log.logger

ip_port = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
url = ip_port + readExcel.readExcel().get_xls('User.xlsx', 'userm_password_reset')[0][1]
print(url)
login_xls = readExcel.readExcel().get_xls('User.xlsx', 'userm_password_reset')   #用户列表

@paramunittest.parametrized(*login_xls)
class testUser(unittest.TestCase):
    def setParameters(self, case_name, path, query, method, lookup , result):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.lookup = str(lookup)
        self.result = str(result)

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

    def test_userm_password_reset(self):
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
        # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        # log.info(data1)
        # data2=json.dumps(data1)
        token = Get_Token().get_Token()
        info = RunMain().run_main(self.method, url, self.query.encode("utf-8"), token)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)# 将响应转换为字典格式

        log.info(url)
        print(info)
        for i in range(len(login_xls)):
            if self.case_name == login_xls[i][0]:  # 如果case_name是login，说明合法，返回的code应该为200
             self.assertEqual(ss[login_xls[i][4]], login_xls[i][5])

        # if self.case_name == 'login':# 如果case_name是login，说明合法，返回的code应该为200
        #     self.assertEqual(ss['state'], 0)
        # if self.case_name == 'login_error':# 同上
        #     self.assertEqual(ss['state'], 1)
        # if self.case_name == 'login_null':# 同上
        #     self.assertEqual(ss['state'], 1)



