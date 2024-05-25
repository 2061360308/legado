import re


def parse_mark(data):
    # 修改正则表达式以匹配新的标记格式
    marked_texts = re.findall('\{\{(.*?)@(.*?)}}', data)

    marks = []

    for marked_text in marked_texts:
        name, params = marked_text
        # 使用 split 方法来分割参数
        param_list = params.split('|')
        # 使用一个字典来存储参数，这样可以处理多个参数
        marks.append({"name": name, "params": param_list})

    return marks


if __name__ == '__main__':
    data = """
    {{rawlink@https:123|456}}
    
    {{rawlink@https:123|789}}
    """
    print(parse(data))
