import json
import sys
import random
import string
import main

def generate_unique_id(length=10):
    # 确保ID长度不超过可用字符集的组合数
    if length > len(string.ascii_letters + string.digits):
        raise ValueError("ID长度不能超过可用字符集的组合数")
    
    # 随机选择字母和数字生成ID
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choices(characters, k=length))
    return unique_id

# 从文件中读取JSON数据
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# 转换函数
def convert_from_abcd_to_xywh(abcd, label, width, height):
    x, y, w, h = main.abcd_to_xywh(abcd[0], abcd[1], abcd[2], abcd[3], width, height)
    return {"x": x, "y": y, "width": w, "height": h, "rotation": 0, "rectanglelabels": [label]}

# 主函数
def convert_abcd_to_xywh(from_abcd_file, to_xywh_file, original_width, original_height):
    # 从文件中读取FromABCD的JSON数据
    from_abcd_json = read_json_file(from_abcd_file)

    # 创建ToXYWH的JSON结构
    to_xywh_json = {
        "id": 1,
        "annotations": [{
            "id": 1,
            "completed_by": 1,
            "result": [],
            "was_cancelled":False,
            "ground_truth":False,
            "created_at":"2024-05-10T11:31:03.293095Z",
            "updated_at":"2024-05-10T11:56:29.959859Z",
            "draft_created_at":None,
            "lead_time":848.264,
            "prediction":{},
            "result_count":0,
            "unique_id":"07977e78-6857-420c-a495-61cbc509b92b",
            "import_id":None,
            "last_action":None,
            "task":10,
            "project":3,
            "updated_by":1,
            "parent_prediction":None,
            "parent_annotation":None,
            "last_created_by":None
        }],
        "file_upload":"5f553810-label.png",
        "drafts":[],
        "predictions":[],
        "data":{"image":"\/data\/upload\/6\/5f553810-label.png"},
        "meta":{},
        "created_at":"2024-05-11T05:52:10.860735Z",
        "updated_at":"2024-05-11T05:54:02.451356Z",
        "inner_id":1,"total_annotations":1,"cancelled_annotations":0,
        "total_predictions":0,"comment_count":0,"unresolved_comment_count":0,
        "last_comment_updated_at":None,"project":5,"updated_by":1,"comment_authors":[]
    }

    # 执行转换
    for item in from_abcd_json["output"]["json_data"]["mask"]:
        if "box" in item and "label" in item:
            xywh = convert_from_abcd_to_xywh(item["box"], item["label"], original_width, original_height)
            to_xywh_json["annotations"][0]["result"].append({
                "original_width": original_width,
                "original_height": original_height,
                "image_rotation": 0,
                "value": xywh,
                "id": generate_unique_id(),
                "from_name": "label",
                "to_name": "image",
                "type": "rectanglelabels",
                "origin": "manual"
            })

    # 输出转换后的JSON
    # print(json.dumps(to_xywh_json, indent=4))

    # 将转换后的数据写入到ToXYWH.json文件中
    with open(to_xywh_file, 'w') as outfile:
        json.dump(to_xywh_json, outfile, indent=4)

# 确保有足够的命令行参数
if len(sys.argv) != 5:
    print("Usage: python script.py from_abcd_file to_xywh_file original_width original_height")
    sys.exit(1)

# 从命令行参数中获取文件路径和图像尺寸
from_abcd_file = sys.argv[1]
to_xywh_file = sys.argv[2]
original_width = int(sys.argv[3])
original_height = int(sys.argv[4])

# 执行转换
convert_abcd_to_xywh(from_abcd_file, to_xywh_file, original_width, original_height)