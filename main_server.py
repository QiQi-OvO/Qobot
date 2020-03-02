from flask import Flask, request
from json import loads
import requests
from function_judge import function_rec

bot_server = Flask(__name__)


@bot_server.route('/api/message', methods=['POST'])
# 路径是你在酷Q配置文件里自定义的

def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    function_rec.function_recognition(data)
    return ''


if __name__ == '__main__':
    bot_server.run(port=5701)