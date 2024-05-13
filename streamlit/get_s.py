import requests

def get_labels(url = "https://api.replicate.com/v1/predictions/jvf8yt56e9rg80cfe7ctayv97c"):
  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer r8_EbBfAjse8noKnlRKhs4JA0ateqqSsZX4g98P5'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return response.text
