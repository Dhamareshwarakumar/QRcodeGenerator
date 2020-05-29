import pyqrcode


def generate(data, filename):
    qr = pyqrcode.create(data)
    qr.png(filename+".png", scale=8)
    print("QR Created Successfully")


if __name__ == "__main__":
    data = input("Enter Data to be encoded into a QR Code\n")
    filename = input("Enter a name for output image\n")

    generate(data, filename)
