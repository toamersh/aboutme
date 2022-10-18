import socket
import psutil
import time

from flask import Flask
app = Flask(__name__)

from flask import jsonify

def getMyIpAddress():
	hostname=socket.gethostname()
	ipAddress=socket.gethostbyname(hostname)
	return ipAddress

def getUptime():
    return time.time() - psutil.boot_time()

@app.route('/aboutme', methods = ['GET'])
def aboutMe():
	return jsonify({'ipaddress': getMyIpAddress(), 'uptime': getUptime()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)