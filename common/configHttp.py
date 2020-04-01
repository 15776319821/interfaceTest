import requests
import json
from common.Log import logger

logger = logger
class RunMain():

    def send_post(self, url, data, headers):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data,headers=headers).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data ,headers):
        result = requests.get(url=url, data=data ,headers=headers)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None ,token = None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None

        if token!=None:
            headers = {
                "Cache-Control": "no-cache",
                "Accept": "*/*",
                "Content-Type": "application/json;charset=UTF-8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cookie": "SESSION=" + token
            }
        else:
            headers=None


        if method == 'post':
            result = self.send_post(url, data, headers)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data , headers)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    # result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=')
    # print(result)

    login_data = {
        "username": "tianlei@123.com",
        "password": "332c87033116f0f941ea026da7b9c364"
    }
    login_result = requests.post(url='http://192.168.0.200:8333/api/login', data=login_data)
    login_res = json.dumps(login_result.json(), ensure_ascii=False, sort_keys=True, indent=2)
    print(login_res)
    token = login_result.cookies.items()[0][1]
    print(token)
    headers = {
        "Cache-Control": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "SESSION=" + token
    }
    print(json.dumps(headers))
    data = "{}"
    result = requests.post(url='http://192.168.0.200:8333/api/term/topic', data=data, headers=headers).json()
    res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
    print(res)