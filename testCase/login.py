import requests
import json
from common.Log import logger
logger = logger

class Get_Token():

    def get_Token(self):
        login_data = {
            "username": "tianlei@123.com",
            "password": "332c87033116f0f941ea026da7b9c364"
        }
        login_result = requests.post(url='http://192.168.0.200:8333/api/login', data=login_data)
        login_res = json.dumps(login_result.json(), ensure_ascii=False, sort_keys=True, indent=2)
        print(login_res)
        token = login_result.cookies.items()[0][1]

        return token

if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确

    token=Get_Token().get_Token()
    print(token)