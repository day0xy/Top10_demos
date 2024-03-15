import requests

url = 'https://console.volcengine.com/api/passport/security/verifyMFAStatus'

headers = {
    'Host': 'console.volcengine.com',
    'Cookie': 'isIntranet=0; hasUserBehavior=1; vcloudWebId=fc2023de-385c-44e1-8717-8284eda8b774; s_v_web_id=ltp58d3w_5ffTriRH_2kfE_4QUr_AcSS_W7qBGJiRp5p1; top_region=; ve_doc_history=6469; _tea_utm_cache_309138=undefined; starling-language=zh; __tea_cache_tokens_1603={%22web_id%22:%227345665931795056143%22%2C%22user_unique_id%22:%227345665931795056143%22%2C%22timestamp%22:1710296141686%2C%22_type_%22:%22default%22}; msToken=4WK_769LPG1ZaSUTJ2HFnPsN77LXRXpmuBiBH2R_m2xzoBw2w8Dkisjzy5YhKueKduPtR-O_Wn47CNV9qjD6fQoFTtkyuBgMzbP8WHUdifZ3bcsCsxI06LzMXlOLqyA=; LoginCredentialId=4f63d0de-bf41-468f-b1e2-cc22a3354960; LoginCredentialId=4f63d0de-bf41-468f-b1e2-cc22a3354960; connect.sid=s%3A2dc721e0-f9a2-4fa0-9624-9b3e9ed22980.LOh4k5DBHMl3IuXoXyDQuk9QY5Egx5IXX5J0Ya3RN8U; connect.sid=s%3A2dc721e0-f9a2-4fa0-9624-9b3e9ed22980.LOh4k5DBHMl3IuXoXyDQuk9QY5Egx5IXX5J0Ya3RN8U; csrfToken=0854168b31e98f82abf89aad85835c00; csrfToken=0854168b31e98f82abf89aad85835c00; vtm=%257B%2522vtm_aid%2522%253A%2522www.volcengine.com%2522%252C%2522vtm_bid%2522%253A%2522%252Factivity%252Fnew%2522%252C%2522vtm_render_id%2522%253A%252200b134a0-38a9-4e92-8cb6-11793c38edc5%2522%257D; referrer_title=%E6%96%B0%E4%BA%BA%E7%89%B9%E6%83%A0-%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A860%E5%85%83/%E5%B9%B4-%E7%81%AB%E5%B1%B1%E5%BC%95%E6%93%8E; __tea_cache_tokens_3569={%22web_id%22:%227101111153107805144%22%2C%22user_unique_id%22:%227101111153107805144%22%2C%22timestamp%22:1710296445160%2C%22_type_%22:%22default%22}; digest=4f63d0de-bf41-468f-b1e2-cc22a3354960; digest=4f63d0de-bf41-468f-b1e2-cc22a3354960; AccountID=2100927370; AccountID=2100927370; i18next=en',  # 将完整的Cookie数据粘贴在这里
    'Content-Length': '2',
    'Sec-Ch-Ua': '"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"',
    'Dnt': '1',
    'X-Csrf-Token': '0854168b31e98f82abf89aad85835c00',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://console.volcengine.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://console.volcengine.com/user/security/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

data = {"1":"1"}

response = requests.post(url, headers=headers, json=data)
print(response.text)
# byte_data=response.content
# decode_data=byte_data.decode('utf-8')
# print(decode_data)
