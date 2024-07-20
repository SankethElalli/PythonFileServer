import http.server
import socketserver
import socket
import os
import datetime

# Define the handler to serve files
Handler = http.server.SimpleHTTPRequestHandler

# Choose a port for the server
PORT = 8000

# Get the local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Get the current working directory
cwd = os.getcwd()

# Get the current time
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("=========================================")
    print("              Server Started             ")
    print("=========================================")
    print(f"Serving at: \t\t http://{local_ip}:{PORT}")
    print(f"Serving files from: \t {cwd}")
    print(f"Server started at: \t {current_time}")
    print("=========================================")
    httpd.serve_forever()
