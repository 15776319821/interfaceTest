import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
from testCase.login import Get_Token
# import pythoncom
import readExcel
# pythoncom.CoInitialize()
import common.Log
log = common.Log.logger

ip_port = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
url = ip_port + readExcel.readExcel().get_xls('userCase01.xlsx', 'homepage_console_tips')[0][1] + '?'
print(url)
xls = readExcel.readExcel().get_xls('userCase01.xlsx', 'homepage_console_tips')

@paramunittest.parametrized(*xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
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

    def test_homepage_console_tips(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        token=Get_Token().get_Token()
        info = RunMain().run_main(self.method, url, self.query, token)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)# 将响应转换为字典格式
        res = json.dumps(ss, ensure_ascii=False, sort_keys=True, indent=2)
        print(res)
        log.info(data)
        # for i in range(len(xls)):
        #     # print(xls)
        #     print(xls[i][0])
        if self.case_name == 'checkStatus0' :  #如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['msg'], "操作成功")
        if self.case_name == 'checkStatus1':
            self.assertEqual(ss['msg'], "操作成功")





