import base64
from io import BytesIO

import qrcode


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


if __name__ == '__main__':
    a = create_qr(
        "https://gist.githubusercontent.com/2061360308/5984645ef963ea2567777d3f144af2b2/raw/bb021c1e10e555e7aeab78495832223dc5fa91be/test.json")

    print(a)