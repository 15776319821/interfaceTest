import requests
import time

def get_exchange_rates(app_id, base_currency='USD'):
    url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}&base={base_currency}"
    print(url)
    response = requests.get(url)
    print(response.json())
    return response.json()['rates']

def monitor_exchange_rate(app_id, threshold, target_currencies, check_interval=60):
    base_currency = 'USD'
    prev_rates = {currency: get_exchange_rates(app_id, base_currency)[currency] for currency in target_currencies}

    while True:
        time.sleep(check_interval)
        current_rates = get_exchange_rates(app_id, base_currency)

        for currency in target_currencies:
            current_rate = current_rates[currency]
            prev_rate = prev_rates[currency]
            change = (current_rate - prev_rate) / prev_rate

            if abs(change) >= threshold:
                print(f"汇率变化超过阈值! {base_currency} -> {currency}: {change * 100:.2f}%")
                prev_rates[currency] = current_rate

if __name__ == "__main__":
    YOUR_APP_ID = "81df0e7f2aa54f94a6c5ae2c4f04f119" # 替换为你的APP ID
    TARGET_CURRENCIES = ["CNY", "EUR", "JPY"] # 要监控的货币列表，例如：["CNY", "EUR", "JPY"]
    THRESHOLD = 0.01 # 变化阈值，例如：0.01 表示 1% 变化
    monitor_exchange_rate(YOUR_APP_ID, THRESHOLD, TARGET_CURRENCIES)