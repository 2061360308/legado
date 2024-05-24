import re


def prase(data):
    marked_texts = re.findall('@boot@(.*?)\|(.*?)@', data)

    marks = {}

    for marked_text in marked_texts:
        data_type, content = marked_text
        marks[data_type] = content

    return marks


if __name__ == '__main__':
    data = """
    @boot@type|content@
    """
    print(prase(data))
