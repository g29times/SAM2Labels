import requests
import json

import sys
sys.path.append(r"D:\WorkHome\Projects\SELF\ML\utils")
import converte

# 调用sam查询结果，较慢需要轮询
def get_labels(url="https://api.replicate.com/v1/predictions/885cnspgyhrg80cfe8saewj96r"):
  print("< --- get_labels: " + url + " --- >")

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer r8_EbBfAjse8noKnlRKhs4JA0ateqqSsZX4g98P5'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  pre_convert = json.loads(response.text)
  # print(pre_convert)

  # 转换坐标
  if "output" in pre_convert:
    print("convert------------------>")
    converte.convert_json(pre_convert)
  else: # 请求无效
    print("return------------------>")
    return pre_convert["status"]

# 测试
url = "https://api.replicate.com/v1/predictions/885cnspgyhrg80cfe8saewj96r"
response = get_labels(url)
print(response)
