import re

from discussion_bot import DiscussionBot
from discussion import update_discussion


class Bot(DiscussionBot):
    @staticmethod
    def created_magic_fun(token, discussion):
        """
        创建讨论时，处理其中用到的魔法函数
        :param token: GitHub Token
        :param discussion: 讨论对象
        :return:
        """

        def parse_mark(data):
            # 修改正则表达式以匹配新的标记格式
            marked_texts = re.findall('\{\{(.*?)@(.*?)}}', data)

            marks = []

            for marked_text in marked_texts:
                name, params = marked_text
                # 使用 split 方法来分割参数
                param_list = params.split('|')
                # 使用一个字典来存储参数，这样可以处理多个参数
                marks.append({"name": name, "params": param_list, "raw": "{{%s@%s}}" % (name, params)})

            return marks

        for item in parse_mark(discussion.body):
            if item['name'] == 'rawlink':
                print(f"处理rawlink：{item['params']}")
                new_raw_link = f"[`🔗【资源链接】`](https://2061360308.github.io/legado/raw?rawlink={item['params'][0]})"
                discussion.body = discussion.body.replace(item['raw'], new_raw_link)

        update_discussion(token, discussion.number, discussion.body)


Bot().handle_event()
