import requests   # 导入requests库，用于发起HTTP请求
import time       # 导入time库，用于设置时间间隔

# 设置API密钥和要监控的国家代码
API_KEY = "81df0e7f2aa54f94a6c5ae2c4f04f119"
COUNTRIES = ["USD_CNY", "USD_EUR", "USD_JPY"]   # 例子里的国家代码，需要改成您要监控的国家代码

# 设置涨幅阈值百分比，触发警报
THRESHOLD = 0.01

# 设置API请求之间的时间间隔（以秒为单位）
SLEEP_TIME = 60 * 60   # 1小时

# 获取指定国家的汇率
def get_exchange_rate(country):
    response = requests.get(f"https://api.currencyscoop.com/v1/convert?api_key={API_KEY}&from=USD&to={country}")
    data = response.json()   # 将API响应转换为JSON格式
    return data["response"]["to_amount"]   # 返回兑换汇率

# 循环不断地监控汇率变化
while True:
    for country in COUNTRIES:
        rate = get_exchange_rate(country)   # 获取指定国家的汇率
        print(f"Current exchange rate for {country}: {rate}")   # 输出当前汇率
        time.sleep(1)   # 等待1秒

    # 计算汇率百分比变化
    if len(COUNTRIES) > 1:
        last_rates = [get_exchange_rate(country) for country in COUNTRIES]   # 获取上次的汇率
        current_rates = [rate for rate in last_rates]   # 获取当前汇率
    else:
        last_rates = [get_exchange_rate(COUNTRIES[0])]
        current_rates = [rate for rate in last_rates]

    for i, last_rate in enumerate(last_rates):
        percentage_change = abs((current_rates[i] - last_rate) / last_rate * 100)   # 计算汇率变化的百分比
        if percentage_change > THRESHOLD:   # 如果变化超过阈值
            print(f"Alert: Exchange rate for {COUNTRIES[i]} has changed by {percentage_change:.2f}%")   # 输出警报信息

    time.sleep(SLEEP_TIME)   # 等待指定时间间隔再次发起API请求