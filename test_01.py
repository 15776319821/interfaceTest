import requests
import time
import random
import common.Log
log = common.Log.logger

while True:
    try:
        i=1
        url = "https://api.telescope.vip/user-web/user/profile/get"
        # header = {"Accept":"*/*","UserToken":"abdafb278a17386cc4347748e497e360c183eb6afe744a791d7cafaf5eff394b0bb2f1b39c64f870652ba9e04198dca434795187298d30b22f732b42a5f6cc1d","Content-Type":"application/json"}
        header = {"Appid": "6XDE5FO6AI1WVR", "Accept": "application/x-protobuf",
         "UserAgent": "Android/google version/1.3.0 build/1300 model/Xiaomi-lancelot-M2004J19C os/10 feature/66 appkey/oasis pk/com.dhn.oasis tracker/google smd/20201109114847bae241e586e72a4516d8b3a9bf36f52b019b6bb125f0001d cc/CN",
         "Accept-Language": "zh-CN",
         "UserToken": "70c30d16c784e3fd1720fbd8b263e951bec1e2685edc90ace3140e64d917768c294d7cd454f83f7cfad7ce569625a2c534795187298d30b22f732b42a5f6cc1d",
         "Content-Type":"application/json"}
        par={"vuid":120284824,"visitSwitch":0}
        #par = {"vuid":10051638,"visitSwitch":0}
        x=requests.post(url=url,json=par,headers=header)
        # print(x.text)
        log.info(x.text)
        y=random.randint(15, 30)
        print(y)
        time.sleep(y)
    except Exception as e:
        times = time.asctime()
        print("在时间%s,出现错误%s" % (times,e))
        break