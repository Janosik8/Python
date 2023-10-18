import qrcode


def generate(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

generate("https://www.youtube.com/watch?v=pdy3nh1tn6I&t=4079s")