import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
def generate_qr(data):
  try:
    qr = qrcode.QRCode(version = 1,box_size = 10,border = 5)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color = 'black',back_color = 'white')
    img.save("qr_code.png")
  except:
    return "INVALID"
def decode_qr(img):
  try:
    decocdeQR = decode(Image.open(img))
    return decocdeQR[0].data.decode('ascii')
  except:
    return "INVALID"
g=True
while g:
  d=int(input("""ENTER YOUR OPTION:
                 1.ENCODE QR
                 2.DECODE QR
                 3.EXIT"""))
  if d==1:
    data=input("ENTER THE DATA TO BE ENCODED")
    generate_qr(data)
  elif d==2:
    img=input("ENTER THE IMAGE PATH TO BE DECODED")
    print(decode_qr(img))
  else:
    g=False
    print("EXISTING...")
