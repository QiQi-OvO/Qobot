import requests
import message_judge.handle_message as handle_message


def send_data(data_to_type, data_to_send):
    if handle_message.get_message_type(data_to_type) == 'private':
        api_url = 'http://127.0.0.1:5700/send_private_msg'
    elif handle_message.get_message_type(data_to_type) == 'group':
        api_url = 'http://127.0.0.1:5700/send_group_msg'
    else:
        pass
    r = requests.post(api_url, data=data_to_send)
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
