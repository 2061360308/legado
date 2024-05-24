import os
import json

# 获取环境变量中的事件数据文件路径
event_path = os.getenv('GITHUB_EVENT_PATH')

# 读取事件数据文件
with open(event_path, 'r') as f:
    event_data = json.load(f)

# 获取触发事件的讨论的详细信息
discussion = event_data['discussion']
print(discussion['title'])  # 打印讨论标题
print(discussion['body'])  # 打印讨论内容