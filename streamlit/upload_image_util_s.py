import requests
import json
import image_base64

# 封装方法
def upload_image(file_path, url = "https://service-ijd4slqi-1253419200.gz.apigw.tencentcs.com/release/bili/upload"):
    payload = json.dumps({
      "cover": image_base64.encode_image_to_base64(file_path),
      "csrf": "bef6739b86a2b685b8c1e25bab0198c7",
      "SESSDATA": "f6a7d8a2%2C1731131782%2C0fcf9%2A52CjCWohrcZgDQinOF_Za8jeKX3kJ_SgykTjSHPC7JfvRBSDpXBhOU-gYagloFAf8A9XcSVkdUd003UVZ2TnM3UE51Z0VyM0pWLVlEMW50RmVaY1kyaVEyQXAtMVljUHRmQmV0ZHQzNUZOa1puM0RpbDh1dWVST3V2ZEpzV2hJSkphR2lEU3ZIMUF3IIEC"
    })
    headers = {
      'accept': '*/*',
      'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,en-US;q=0.6,fr;q=0.5,ja;q=0.4',
      'content-type': 'application/json',
      'dnt': '1',
      'origin': 'https://www.xiaojuzi.fun',
      'priority': 'u=1, i',
      'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    return requests.request("POST", url, headers=headers, data=payload)