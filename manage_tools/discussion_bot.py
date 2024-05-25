import os
import json


class DiscussionBot:
    def __init__(self):
        # 获取环境变量中的事件数据文件路径
        self.token = os.getenv('TOKEN')
        event_path = os.getenv('GITHUB_EVENT_PATH')

        # 读取事件数据文件
        with open(event_path, 'r') as f:
            event_data = json.load(f)

        # 获取触发事件的类型
        self.eventType = event_data['action']
        print(self.eventType)  # 打印事件类型
        # 获取触发事件的讨论的详细信息
        discussion_number = event_data['discussion']['number']  # 讨论编号
        discussion_id = event_data['discussion']['node_id']  # 讨论全局ID
        discussion_category = event_data['discussion']['category']['name']  # 讨论分类名称
        discussion_title = event_data['discussion']['title']  # 讨论标题
        discussion_body = event_data['discussion']['body']  # 讨论内容
        print({
            'number': discussion_number,
            'id': discussion_id,
            'category': discussion_category,
            'title': discussion_title,
            'body': discussion_body
        })

        # 创建一个 Discussion 对象
        class Discussion:
            number = discussion_number
            id = discussion_id
            category = discussion_category
            title = discussion_title
            body = discussion_body

        self.discussion = Discussion

        # 创建字典来存储事件处理函数
        self.event_handlers = {}

    def handle_event(self):
        for method_name in dir(self):
            if method_name.startswith(self.eventType):
                print("处理事件：", method_name)
                method = getattr(self, method_name)
                method(self.token, self.discussion)
