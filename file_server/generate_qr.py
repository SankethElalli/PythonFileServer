import qrcode
import socket

# Get the local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port = 8000
url = f"http://{local_ip}:{port}"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')
img.save("server_qr_code.png")

print(f"QR code generated for {url} and saved as server_qr_code.png")
