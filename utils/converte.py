# kimi
import json
import random
import string
import coordinates
import timeutil
import uuid
import sys
from datetime import datetime, timezone


# 工具 UUID
def generate_unique_id(length=10):
    # 确保ID长度不超过可用字符集的组合数
    if length > len(string.ascii_letters + string.digits):
        raise ValueError("ID长度不能超过可用字符集的组合数")
    
    # 随机选择字母和数字生成ID
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choices(characters, k=length))
    return unique_id


# 工具 从文件中读取JSON数据
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# 工具 转换函数
def convert_from_abcd_to_xywh(abcd, label, width, height):
    x, y, w, h = coordinates.abcd_to_xywh(abcd[0], abcd[1], abcd[2], abcd[3], width, height)
    xywh = x, y, w, h
    print(f"Absolute coordinates [{label}] - {abcd[0], abcd[1], abcd[2], abcd[3]} convert to XYWH format: {xywh}")
    return {"x": x, "y": y, "width": w, "height": h, "rotation": 0, "rectanglelabels": [label]}


# 主函数 1 文件处理 可选
def convert_file(project_id, from_abcd_file="from_sam.json", fileName="origin.jpg", 
                 original_width=1024, original_height=1024):
    print("converter 处理文件 " + from_abcd_file)
    from_abcd_json = read_json_file(from_abcd_file)

    to_xywh_json = convert_json(from_abcd_json, project_id, fileName, original_width, original_height)
    
    dump_file(to_xywh_json, fileName)

    return to_xywh_json

# TODO 该项目号硬编码 仅开发
project_id = str(1)

# 主函数 2 纯json转换 必选
def convert_json(from_abcd_json_obj, project_id, fileName="origin.jpg", original_width=1024, original_height=1024):
    print("converter 处理json")
    # convert_file(from_abcd_json, width, height)
# 主函数
# def convert_file(from_abcd_file="from_sam.json", to_xywh_file="to_label.json", 
#                  original_width=1024, original_height=1024):
    # if(json_input is not None and json_input != ""):
    #     # print("--- json_input ---")
    #     from_abcd_json = json_input
    # elif(from_abcd_file is not None):
        # 从文件中读取FromABCD的JSON数据
    # from_abcd_json = read_json_file(from_abcd_file)
    # else:
    #     return
    timenow = datetime.now(timezone.utc)
    # formatted_now = timenow.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    
    # 生成一个UUID
    unique_id = uuid.uuid4()
    # 将UUID对象转换为字符串格式
    unique_id_str = str(unique_id)

    # 创建ToXYWH的JSON结构
    to_xywh_json = [{
        "id": 1,
        "annotations": [{
            "id": 1,
            "completed_by": 1,
            "result": [],
            "was_cancelled":False,
            "ground_truth":False,
            "created_at":timenow,
            "updated_at":timenow,
            "draft_created_at":None,
            "lead_time":666.666,
            "prediction":{},
            "result_count":0,
            "unique_id":unique_id_str,
            "import_id":None,
            "last_action":None,
            "task":1,
            "project":1,
            "updated_by":1,
            "parent_prediction":None,
            "parent_annotation":None,
            "last_created_by":None
        }],
        "file_upload":fileName,
        "drafts":[],
        "predictions":[],
        "data":{"image":"/data/upload/" + project_id + "/" + fileName},
        "meta":{},
        "created_at":timenow,
        "updated_at":timenow,
        "inner_id":1,"total_annotations":1,"cancelled_annotations":0,
        "total_predictions":0,"comment_count":0,"unresolved_comment_count":0,
        "last_comment_updated_at":None,"project":5,"updated_by":1,"comment_authors":[]
    }]

    # 执行转换
    for item in from_abcd_json_obj["output"]["json_data"]["mask"]:
        if "box" in item and "label" in item:
            xywh = convert_from_abcd_to_xywh(item["box"], item["label"], original_width, original_height)
            to_xywh_json[0]["annotations"][0]["result"].append({
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

    return to_xywh_json
    # 输出转换后的JSON
    # print(json.dumps(to_xywh_json, default=timeutil.json_serial))


# 主函数 3 导出文件 可选
def dump_file(to_xywh_json, fileName="to_label.json"):
    to_xywh_file = fileName + ".json"
    print("will store to: " + to_xywh_file)

    # 将转换后的数据写入到文件中
    with open(to_xywh_file, 'w') as outfile:
        json.dump(to_xywh_json, outfile, default=timeutil.json_serial, indent=4)


# 测试 运行streamlit时需注释
# convert_file("..\data\\boy.txt", "44126dcd-head.png", 400, 400)
# # 确保有足够的命令行参数
# if len(sys.argv) != 5:
#     print("Usage: python script.py from_file to_file _width _height")
#     sys.exit(1)

# # 从命令行参数中获取文件路径和图像尺寸
# from_abcd_file = sys.argv[1]
# to_xywh_file = sys.argv[2]
# original_width = int(sys.argv[3])
# original_height = int(sys.argv[4])

# # 执行转换 python utils\converte.py data\FromRobot.txt data\ToR.json 1456 816
# convert_file("", from_abcd_file, to_xywh_file, original_width, original_height)