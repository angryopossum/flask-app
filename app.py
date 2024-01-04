import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'
@app.route('/ip')
def ip():
    ip_address = socket.gethostbyname(socket.gethostname())
    return f"IP-адрес клиента: {ip_address}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

