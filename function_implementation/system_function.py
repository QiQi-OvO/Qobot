import message_judge.handle_message as handle_message
import main_server


ROOT_ID = '2763359332'

def power_off(data):
    type = handle_message.get_message_type(data)
    message = (data['message'][0]['data']['text'])
    if type == 'private':
        if message.find("开机") != -1:
            main_server.LAST_STATUS_REG = ""
            main_server.DATA_INVA_FLAG = 0
            sender_qq = data['user_id']
            sender_data = {
                'user_id': sender_qq,
                'message': "已经成功开启Qobot",
                'auto_escape': False
            }
            return sender_data
        else:
            return None
    elif type == 'group':
        # if message.find("关闭复读") != -1:
        #     main_server.LAST_STATUS_REG = ""
        #     main_server.DATA_INVA_FLAG = 0
        #     sender_data = {
        #         'group_id': data['group_id'],
        #         'message': "已经关闭恶心人的功能",
        #         'auto_escape': False
        #     }
        #     return sender_data
        # else:
        #     sender_data = {
        #         'group_id': data['group_id'],
        #         'message': (data['message'][0]['data']['text']),
        #         'auto_escape': False
        #     }
        #     return sender_data
        pass
    else:
        pass

