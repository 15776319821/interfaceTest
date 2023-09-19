import requests
import time
import datetime
import json
import os

def get_exchange_rates(app_id, base_currency='USD', date='latest'):
    url = f"https://openexchangerates.org/api/{date}.json?app_id={app_id}&base={base_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: API 请求失败。HTTP 状态码：{response.status_code}")
        return None

    try:
        return response.json()['rates']
    except Exception as e:
        print(f"Error: 解析 JSON 数据时出现问题。异常信息：{e}")
        return None

def save_rates_to_file(rates, filename):
    with open(filename, 'w') as f:
        json.dump(rates, f)

def load_rates_from_file(filename):
    if not os.path.exists(filename):
        return None

    with open(filename, 'r') as f:
        return json.load(f)

# 添加这个新函数
def send_feishu_message(webhook_url, text):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "msg_type": "text",
        "content": {
            "tect": "任务已执行",
            "text": text
        }
    }
    response = requests.post(webhook_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("成功发送飞书消息。")
    else:
        print(f"发送飞书消息失败，HTTP 状态码: {response.status_code}")

def monitor_exchange_rate(app_id, threshold, target_currencies, feishu_webhook_url, days_to_compare=7, check_interval=86400):
    base_currency = 'USD'
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    compare_date = (datetime.datetime.now() - datetime.timedelta(days=days_to_compare)).strftime('%Y-%m-%d')

    rates_file = f"exchange_rates_{today}.json"
    prev_rates_file = f"exchange_rates_{compare_date}.json"

    current_rates = get_exchange_rates(app_id, base_currency)

    if current_rates is not None:
        save_rates_to_file(current_rates, rates_file)
        print(f"已保存 {today} 的汇率到文件 {rates_file}")
    else:
        print("Error: 无法获取当前汇率。")

    prev_rates = load_rates_from_file(prev_rates_file)

    if prev_rates is None:
        print(f"未找到 {compare_date} 的汇率文件 {prev_rates_file}")
        return

    for currency in target_currencies:
        if currency not in prev_rates:
            print(f"Error: 无法找到 {currency} 在 {compare_date} 的汇率。")
            continue

        current_rate = current_rates[currency]
        prev_rate = prev_rates[currency]
        change = (current_rate - prev_rate) / prev_rate

        if abs(change) >= threshold:
            message = f"汇率变化超过阈值! {base_currency} -> {currency}: {change * 100:.2f}%"
            print(message)
            send_feishu_message(feishu_webhook_url, message)

if __name__ == "__main__":
    YOUR_APP_ID = "81df0e7f2aa54f94a6c5ae2c4f04f119"  # 替换为你的APP ID
    TARGET_CURRENCIES = ["AED", "BHD", "EGP", "IRR", "IQD", "JOD", "KWD", "LBP", "LYD", "MAD", "OMR", "PKR", "QAR", "SAR", "TND", "YER", "ARS", "BOB", "BRL", "CLP", "COP", "USD", "EUR", "GYD", "PYG", "PEN", "SRD", "UYU", "VEF", "BND", "MMK", "KHR", "USD", "IDR", "LAK", "MYR", "PHP", "SGD", "THB", "VND", "USD", "CAD", "MXN", "EUR", "BGN", "HRK", "CZK", "DKK", "HUF", "ISK", "NOK", "PLN", "RON", "SEK", "CHF", "GBP"] # 要监控的货币列表，例如：["CNY", "EUR", "JPY"]
    THRESHOLD = 0.1  # 变化阈值，例如：0.1 表示 10% 变化
    DAYS_TO_COMPARE = 1  # 要进行对比的天数，例如：7表示与上一周的汇率进行对比
    FEISHU_WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/11b0e38f-8d1f-4021-806f-a9a39b5ec9ab"  # 替换为你的飞书群机器人API网址

    monitor_exchange_rate(YOUR_APP_ID, THRESHOLD, TARGET_CURRENCIES, FEISHU_WEBHOOK_URL, DAYS_TO_COMPARE)