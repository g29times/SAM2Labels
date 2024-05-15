import json
from datetime import datetime, timezone

# 假设你有一个包含datetime对象的字典
data = {
    'created_at': datetime.now(timezone.utc)
}

# 定义一个函数，用于将datetime对象转换为ISO格式的字符串
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        serial = obj.isoformat().replace('+00:00', 'Z')  # 将UTC的偏移转换为'Z'
        return serial
    raise TypeError("Type not serializable")

# 使用json.dumps转换字典为JSON字符串，通过default参数调用自定义的序列化器
json_str = json.dumps(data, default=json_serial)

print(json_str)