from github import Github
import os
import json

# 获取环境变量中的事件数据文件路径
token = os.getenv('GITHUB_TOKEN')
event_path = os.getenv('GITHUB_EVENT_PATH')

# 读取事件数据文件
with open(event_path, 'r') as f:
    event_data = json.load(f)

# 获取触发事件的讨论的详细信息
discussion_number = event_data['discussion']['number']
print(event_data['discussion'])  # 打印讨论的详细信息
print(event_data['discussion']['title'])  # 打印讨论标题
print(event_data['discussion']['body'])  # 打印讨论内容
print(event_data['discussion']['number'])  # 打印讨论编号

# 使用GitHub API获取讨论
g = Github(token)
repo = g.get_repo("2061360308/legado")  # 替换为你的仓库主名和仓库名
discussion = repo.get_discussion(discussion_number)

# 对讨论进行自动回复
discussion.create_comment("你的回复内容")