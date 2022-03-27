import qrcode
from config.config import qr_path, qr_img


def text_to_qr_generator(data):
    qr = qrcode.QRCode(
        version=2,  # Range from 1 to 40
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    datastring = '''Details are\n'''
    for x in data:
        datastring = datastring + "{} : {} ".format(x, data[x]) + "\n"
    print(datastring)
    qr.add_data(datastring)
    qr.make(fit=True)

    qrimg = qr.make_image(fill_color="black", back_color="white")
    qrimg.save(qr_path + qr_img)
