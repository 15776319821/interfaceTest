import requests
import json
from common.Log import logger
from testCase.login import Get_Token

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
                # Cookie
                "Cookie": "JSESSIONID=" + token,
                # 传输
                "Connection": "keep - alive",
                "Host": "192.168.0.244:8600",
                # 缓存
                "Cache-Control": "no-cache",
                "Content-Type": "application/json;charset=UTF-8",
                # 客户端
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.149Safari / 537.36",
                # 实体
                "Content - Length": "0",
                # 杂项
                "Referer": "http: // 192.168.0.244: 8600 /"

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
    token=Get_Token().get_Token()
    print(token)
    headers = {
        #Cookie
        "Cookie": "JSESSIONID=" + token,
        #传输
        "Connection": "keep - alive",
        "Host": "192.168.0.244:8600",
        #缓存
        "Cache-Control": "no-cache",
        "Content-Type": "application/json;charset=UTF-8",
        # 客户端
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.149Safari / 537.36",
        #实体
        "Content - Length": "0",
        #杂项
        "Referer": "http: // 192.168.0.244: 8600 /"

    }
    print(json.dumps(headers))
    data = '{123}'
    result = requests.post(url='http://192.168.0.244:8600/api/lg/one', data=data, headers=headers).json()
    res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
    print(res)