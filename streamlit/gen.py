import requests
import json

def upload_image(input_image, url = "https://api.replicate.com/v1/predictions"):
  payload = json.dumps({
    "version": "80a2aede4cf8e3c9f26e96c308d45b23c350dd36f1c381de790715007f1ac0ad",
    "input": {
      "input_image": input_image
    }
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer r8_EbBfAjse8noKnlRKhs4JA0ateqqSsZX4g98P5'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return response.text
