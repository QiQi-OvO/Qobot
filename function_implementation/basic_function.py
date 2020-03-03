import message_judge.handle_message as handle_message

ROOT_ID = '2763359332'
BROADCAST_DATA = 'http://120.25.231.117:8080/'


def no_function_tip(data):
    """
    如果输入#好没有这个功能的话进行提示
    :param data:
    :return:
    """
    type = handle_message.get_message_type(data)
    if type == 'private':
        sender_qq = data['user_id']
        sender_data = {
            'user_id': sender_qq,
            'message': '[CQ:face,id=22] 作者暂时没有添加这个功能哦，如果你有什么好的想法想告诉作者的话 \n请使用 #我想对你说+你想说的话 后面就可以发你想对我说的话了 \n'
                       + '例如：#我想对你说你其实超帅的',
            'auto_escape': False
        }
        return sender_data
    elif type == 'group':
        pass
    else:
        pass


def tell_me(data):
    """
    功能你想对我说的实现
    :param data:
    :return:
    """
    type = handle_message.get_message_type(data)
    if type == 'private':
        m_message = (data['message'][0]['data']['text'])
        target_qq = '2763359332'
        m_sender_info = (data['sender'])
        sender_qq = m_sender_info['user_id']
        m_message = "QQ:" + str(sender_qq) + "  的用户想对你说\n" + m_message[6:]
        sender_data = {
            'user_id': target_qq,
            'message': m_message,
            'auto_escape': False
        }
        return sender_data
    elif type == 'group':
        pass
    else:
        pass


def incor_format(data):
    """
    格式不正确输出功能列表和使用方法
    :param data:
    :return:
    """
    type = handle_message.get_message_type(data)
    if type == 'private':
        m_sender_info = (data['sender'])
        sender_qq = m_sender_info['user_id']
        sender_data = {
            'user_id': sender_qq,
            'message': ' 请尝试输入#号加以下功能哦 \n 课表   (展示你的私人化定制课表) \n 微博热搜 （实时更新微博热点） \n 翻译(中/日/韩/英/粤)语  自动检测语言翻译成目标语言 ',
            'auto_escape': False
        }
        return sender_data
    elif type == 'group':
        pass
    else:
        pass


def root_to_user(data):
    """
    作者想对用户说的话
    :param data:
    :return:
    """
    root_id = data['user_id']
    if root_id != int(ROOT_ID):
        sender_data = {
            'user_id': root_id,
            'message': '只有作者才能启用此功能哦',
            'auto_escape': False
        }
        return sender_data
    else:
        m_message = (data['message'][0]['data']['text'])
        sender_message = m_message.split()
        target_qq = sender_message[1]
        message = sender_message[2]
        sender_data = {
            'user_id': target_qq,
            'message': '一名不愿透漏姓名的小可爱想对你说:' + message,
            'auto_escape': False
        }
        return sender_data


def broadcast_message(data):
    """
    广播的数据
    :param data:
    :return:
    """
    type = handle_message.get_message_type(data)
    if type == 'private':
        sender_data = {
            'user_id': data['user_id'],
            'message': BROADCAST_DATA,
            'auto_escape': False
        }
        return sender_data
    elif type == 'group':
        sender_data = {
            'group_id': data['group_id'],
            'message': BROADCAST_DATA,
            'auto_escape': False
        }
        return sender_data
