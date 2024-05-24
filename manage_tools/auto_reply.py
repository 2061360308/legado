import os
import json
from discussion import replay_discussion
from boot_mark import prase

# 获取环境变量中的事件数据文件路径
token = os.getenv('GITHUB_TOKEN')
event_path = os.getenv('GITHUB_EVENT_PATH')

# 读取事件数据文件
with open(event_path, 'r') as f:
    event_data = json.load(f)

# 获取触发事件的讨论的详细信息
discussion_number = event_data['discussion']['number']
"""
{'active_lock_reason': None, 'answer_chosen_at': None, 'answer_chosen_by': None, 'answer_html_url': None, 'author_association': 'OWNER', 'body': '测试自动回复5', 'category': {'created_at': '2024-05-24T08:53:40.000+08:00', 'description': '分享你编写或喜欢的书源以及书源合集', 'emoji': ':bulb:', 'id': 41831060, 'is_answerable': False, 'name': 'C书源发布', 'node_id': 'DIC_kwDOL_11UM4CfkqU', 'repository_id': 805139792, 'slug': 'c书源发布', 'updated_at': '2024-05-24T15:40:43.000+08:00'}, 'comments': 0, 'created_at': '2024-05-24T15:26:49Z', 'html_url': 'https://github.com/2061360308/legado/discussions/7', 'id': 6724303, 'locked': False, 'node_id': 'D_kwDOL_11UM4AZprP', 'number': 7, 'reactions': {'+1': 0, '-1': 0, 'confused': 0, 'eyes': 0, 'heart': 0, 'hooray': 0, 'laugh': 0, 'rocket': 0, 'total_count': 0, 'url': 'https://api.github.com/repos/2061360308/legado/discussions/7/reactions'}, 'repository_url': 'https://api.github.com/repos/2061360308/legado', 'state': 'open', 'state_reason': None, 'timeline_url': 'https://api.github.com/repos/2061360308
"""
print(event_data['discussion'])  # 打印讨论的详细信息
print(event_data['discussion']['title'])  # 打印讨论标题
print(event_data['discussion']['body'])  # 打印讨论内容
print(event_data['discussion']['number'])  # 打印讨论编号

# 解析讨论内容
marks = prase(event_data['discussion']['body'])
print(marks)  # 打印解析结果
# 生成具体的标签
replay_content = (f"非常感谢您的贡献。\n\n以下是您的资源导入链接\n\t[一键导入：](yuedu://booksource/importonline?src={marks['rawlink']})\n\t[下载json]({marks['rawlink']})")

# 使用GitHub API获取讨论
replay_discussion(token, discussion_number, replay_content)
