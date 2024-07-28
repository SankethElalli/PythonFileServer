# QR Code File Server
- This project sets up a simple HTTP server that serves an HTML page displaying file_server folder to access files on the phone. 
- Generate and Scan the QR code with a phone allows access to the files on the server. 
- The QR code redirects to the server's IP address. 
- Move the files that are to be shared or accessed to the server folder before scanning.. 
- The QR code redirects to the file_server's folder.

## Features

- **QR Code Generation**: Automatically generates a QR code that links to the server's IP address.
- **File Access**: Allows access to files on the server through the scanned QR code.
- **Dynamic IP Detection**: Detects the local IP address of the server and incorporates it into the QR code.
- **Simple HTML Interface**: To access the server folder.
- **Easy Setup**: Minimal configuration required to get the server running.

 ***To generate a QR code for new IP run `generate_qr.py` file*.**

 ## Technologies Used

- **Python**: The core programming language used to create the HTTP server.
- **http.server**: Python's built-in module for handling HTTP requests.
- **socket**: Used to determine the local IP address of the server.
- **HTML**: For creating the simple web interface to access the files on server folder.
- **qrcode**: Python library to generate QR codes (if dynamically generating QR codes is desired).
- **PIL (Pillow)**: Python Imaging Library to handle image creation and manipulation (if dynamically generating QR codes is desired).
