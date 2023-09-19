import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 设置OAuth2客户端ID和API密钥
creds = service_account.Credentials.from_service_account_file('path/to/credentials.json')

# 设置商品类型和Google开发者控制台API的版本
product_type = 'inapp'
version = 'v3'

# 读取Excel电子表格中的商品信息
df = pd.read_excel('path/to/products.xlsx', sheet_name='Sheet1')

# 设置支持的语言列表
supported_languages = ['en-US', 'tr', 'ar', 'es-MX', 'pt-BR']

# 循环遍历每个商品，并在Google开发者控制台中创建新商品
for index, row in df.iterrows():
    product_id = row['商品ID']

    # 使用每个支持的语言为商品设置名称和简介
    title = {}
    description = {}
    for lang in supported_languages:
        title[lang] = row[f'{lang}_商品名称']
        description[lang] = row[f'{lang}_商品简介']

    # 设置商品信息
    product = {
        'packageName': 'your.package.name',  # 您的应用程序包名称
        'sku': product_id,  # 商品ID
        'defaultLanguage': 'en-US',  # 默认语言
        'inapp': {
            'purchaseType': 'managedUser',
            'productId': product_id,
            'listings': {
                lang: {
                    'title': title[lang],
                    'description': description[lang]
                } for lang in supported_languages
            }
        }
    }

    # 使用Google开发者控制台API创建新商品
    service = build('androidpublisher', version, credentials=creds)
    result = service.inappproducts().insert(packageName=product['packageName'], body=product).execute()

    # 打印已创建的商品的SKU
    print(f'Product created: {result["sku"]}')