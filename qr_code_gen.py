import PySimpleGUI as sg
import os
import qrcode
layout=[
    [sg.Input(size=(25,1),key="-WEB ADDRESS-")],
    [sg.Button("Generate QR Code")],
    [sg.Image(key="-IMAGE-",size=(300,300))]
]
window= sg.Window("QR Code Generator", layout)

def generate_qr_code(link):
    qr=qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(link)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="blue")
    file_name="qr_code" + ".png"
    path = os.path.join(os.getcwd(),file_name)
    print(path)
    img.save(path)
    return path

while True:
    event,values=window.read()
    if event=="Exit" or event==sg.WIN_CLOSED:
        break
    if event=="Generate QR Code":
        web_address= values["-WEB ADDRESS-"]
        qr_code_image_path=generate_qr_code(web_address)
        window["-IMAGE-"].update(filename=qr_code_image_path)
window.close
