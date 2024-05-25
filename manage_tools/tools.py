import base64
import os
from io import BytesIO

import qrcode
import requests

from manage_tools.discussion import get_discussion_id


def create_qr(data: str):
    # 创建 qr 对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 添加数据
    qr.add_data(data)
    qr.make(fit=True)

    # 创建二维码图片
    img = qr.make_image(fill='black', back_color='white')

    # 创建一个 BytesIO 对象并保存图片
    buffered = BytesIO()

    img.save(buffered)

    # 获取图片的 Base64 编码
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return img_str


def update_discussion(token, discussion_number, new_body):
    headers = {
        'Authorization': f'bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'query': '''
                mutation {
                  updateDiscussion(input: {discussionId: "%s", body: "%s"}) {
                    clientMutationId
                  }
                }
            ''' % (get_discussion_id(token, discussion_number), new_body),
    }
    response = requests.post('https://api.github.com/graphql', headers=headers, json=data)
    return response.json()


if __name__ == '__main__':
    print(update_discussion(os.getenv('GITHUB_TOKEN'), 7, "这是api修改后的内容"))
