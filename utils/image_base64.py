# https://www.xiaojuzi.fun/bili-short-url/upload.html
# https://www.bilibili.com/zhibi-image-upload
import base64
import os

def get_image_format(file_path):
    """根据文件扩展名获取图片格式"""
    extension = os.path.splitext(file_path)[1].lower().lstrip('.')
    return extension

def encode_image_to_base64(file_path):
    """将图片文件编码为Base64字符串，并指定MIME类型"""
    # 读取图片文件
    with open(file_path, 'rb') as image_file:
        img_data = image_file.read()

    # 编码为Base64
    img_base64 = base64.b64encode(img_data)
    img_base64_str = img_base64.decode('utf-8')

    # 获取图片格式
    image_format = get_image_format(file_path)

    # 构建Base64编码字符串
    img_base64_with_format = f'data:image/{image_format};base64,{img_base64_str}'
    
    return img_base64_with_format

# 测试
# # 图片文件路径
# image_path = 'robot.jpg'  # 替换为实际的图片文件路径

# # 输出文件路径
# output_path = image_path + '.txt'  # 替换为实际的输出文件路径

# # 编码图片并写入到文本文件
# base64_str = encode_image_to_base64(image_path)

# with open(output_path, 'w') as output_file:
#     output_file.write(base64_str)

# print(f'Base64 encoded image saved to {output_path}')