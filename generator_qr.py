import qrcode

# URL que quieres codificar
url = "https://grillonegro.com.ar/contact-qr"

# Generar el código QR
qr = qrcode.QRCode(
    version=1,  # controla el tamaño del QR
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # nivel de corrección de errores
    box_size=10,  # tamaño de cada cuadro
    border=4,  # grosor del borde
)

qr.add_data(url)
qr.make(fit=True)

# Crear la imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar en un archivo
img.save("codigo_qr.png")

print("Código QR generado como codigo_qr.png")

