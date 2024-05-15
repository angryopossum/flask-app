import socket,os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'
@app.route('/ip')
def ip():
    ip_address = socket.gethostbyname(socket.gethostname())
    return f"IP-адрес клиента: {ip_address}"
@app.route('/env')
def env():
    env_vars = os.environ
    env_vars_str = "<br>".join([f"{key}: {value}" for key, value in env_vars.items()])
    return f"Environment variables:<br>{env_vars_str}"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

