import requests
import json

import sys
sys.path.append(r"D:\WorkHome\Projects\SELF\ML\utils")
import converte

# 调用sam查询结果，较慢需要轮询
def get_labels(to_xywh_file, project_id, url="https://api.replicate.com/v1/predictions/885cnspgyhrg80cfe8saewj96r", 
               width=1024, height=1024):
  print("< --- get_labels: " + url + " --- >")

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer r8_GmLBI6PscUUVaeOkZnZnhKVqe5OPAyg3iREsM'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  sam_json = json.loads(response.text)
  # print(pre_convert)
  print(sam_json["status"] + "------------------>")
  print(json.dumps(sam_json))

  # 转换坐标
  if "output" in sam_json:
    to_xywh_json = converte.convert_json(sam_json, project_id, width, height)
    converte.dump_file(to_xywh_json, to_xywh_file)
    return True
  else: # 请求无效
    return False

# 测试 885cnspgyhrg80cfe8saewj96r 2t2vs0v1nsrg80cffa98ed29e4 
# status: 
# - 401
# {"title":"Unauthenticated","detail":"You did not pass a valid authentication token","status":401}
# - starting 
# {"id":"aqc774wbc5rge0cffb9r3f1q24","model":"idea-research/ram-grounded-sam","version":"80a2aede4cf8e3c9f26e96c308d45b23c350dd36f1c381de790715007f1ac0ad","input":{"input_image":"https://archive.biliimg.com/bfs/archive/9f5abbb27c24e1a5cc616aeea1481b5332477842.jpg"},"logs":"","error":null,"status":"starting","created_at":"2024-05-15T05:57:15.233Z","urls":{"cancel":"https://api.replicate.com/v1/predictions/aqc774wbc5rge0cffb9r3f1q24/cancel","get":"https://api.replicate.com/v1/predictions/aqc774wbc5rge0cffb9r3f1q24"}}
# - succeeded 1 "input": {}
# "2024-05-13T13:44:44.02Z", "started_at": "2024-05-13T13:45:31.234589Z", "completed_at": "2024-05-13T13:45:32.202367Z", "urls": {"cancel": "https://api.replicate.com/v1/predictions/885cnspgyhrg80cfe8saewj96r/cancel", "get": "https://api.replicate.com/v1/predictions/885cnspgyhrg80cfe8saewj96r"}, "metrics": {"predict_time": 0.967778}}
# - succeeded 2 "status": "succeeded"
# {"id": "2t2vs0v1nsrg80cffa98ed29e4", "model": "idea-research/ram-grounded-sam", "version": "80a2aede4cf8e3c9f26e96c308d45b23c350dd36f1c381de790715007f1ac0ad", "input": {"input_image": "https://archive.biliimg.com/bfs/archive/9f5abbb27c24e1a5cc616aeea1481b5332477842.jpg"}, "logs": "Before NMS: 8 boxes\nAfter NMS: 5 boxes", "output": {"json_data": {"mask": [{"label": "background", "value": 0}, {"box": [568.2401123046875, 22.026947021484375, 1359.5457763671875, 811.490234375], "label": "robot", "logit": 0.5, "value": 1}, {"box": [2.1121978759765625, 615.1333618164062, 379.80902099609375, 774.0284423828125], "label": "stone", "logit": 0.4, "value": 2}, {"box": [3.78106689453125, 286.56927490234375, 1449.637939453125, 810.7224731445312], "label": "floor", "logit": 0.32, "value": 3}, {"box": [3.90240478515625, 269.78887939453125, 702.2015380859375, 809.5703735351562], "label": "desert", "logit": 0.25, "value": 4}, {"box": [265.821533203125, 486.33349609375, 441.8647155761719, 596.4161376953125], "label": "stone", "logit": 0.25, "value": 5}], "tags": "desert, floor, robot, stone, rocky, terrain, toy"}, "masked_img": null, "rounding_box_img": null, "tags": "desert, floo, "started_at": "2024-05-15T04:46:04.73268Z", "completed_at": "2024-05-15T04:46:05.904979Z", "urls": {"cancel": "httpsns/2t2vs0v1nsrg80cffa98ed29e4"}, "metrics": {"predict_time": 1.172299}}
# url = "https://api.replicate.com/v1/predictions/" + "aha299bh4drg80cffbj86s3zbc"
# response = get_labels(url)
# print(response)
