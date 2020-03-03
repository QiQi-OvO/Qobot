import http.client
import hashlib
import urllib
import random
import json
from message_judge import handle_message


CONFIG_PATH = 'C:/Users/Administrator/Desktop/translate_config.txt'  # 百度翻译API配置信息
language_dict = {
    '中文':'zh',
    '日语':'jp',
    '韩语':'kor',
    '英语':'en',
    '粤语':'yue'
}



def main_run(data):
    info_dict = get_info_by_config()
    appid = info_dict['appid'][0]
    secretKey = info_dict['secretKey'][0]
    message = (data['message'][0]['data']['text'])
    pre_dict = pre_translate(message)
    print(pre_dict)
    target_lang = pre_dict['toLang']
    q = pre_dict['q']
    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'  # 原文语种
    print(target_lang)
    toLang = language_dict[target_lang]  # 译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        print(result['trans_result'][0]['dst'])
        sender_message = result['trans_result'][0]['dst']

    except Exception as e:
        print(e)
        sender_message = '服务获取超时'
    finally:
        if httpClient:
            httpClient.close()
    type = handle_message.get_message_type(data)
    if type == 'private':
        sender_data = {
            'user_id' : data['user_id'],
            'message' : sender_message,
            'auto_escape': False
        }
        print(sender_data)
        return sender_data
    elif type == 'group':
        sender_data = {
            'group_id': data['group_id'],
            'message': sender_message,
            'auto_escape': False
        }
        return sender_data
    else:
        pass




def get_info_by_config():
    file = open(CONFIG_PATH, "r")
    info_list = []
    while True:
        mystr = file.readline()  # 表示一次读取一行
        if not mystr:
            # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
            break
        tmp_list = mystr.split()
        info_list.append(tmp_list)
    info_dict = {
        'appid':info_list[0],
        "secretKey":info_list[1]
    }
    return info_dict

def pre_translate(message):
    #   翻译韩语 中到韩       翻译英语 中到英  翻译日语 翻译粤语
    nPos = message.find('翻译')
    toLang = message[nPos + 2:nPos + 4]
    q = message[nPos + 4:]
    pre_info_dict = {
        'toLang': toLang,
        'q':q
    }
    return pre_info_dict

if __name__ == '__main__':
    message = ("翻译日语 你好啊")
    test_dict = pre_translate(message)
    print( test_dict )