



def get_message_type(data):
    """
    判断消息来源
    :param data: 接受到的Json data
    :return: 数据的类型
    """
    m_message_type = (data['message_type'])
    return m_message_type


def get_message_content(m_message):
    """
    得到#后面的输入 如果没有#则返回 错误格式的字符串  特殊的我想对你说功能单独使用。用if来做判断
    :param m_message: 用户输入信息
    :return:
    """
    if m_message[0] == '#':
        if m_message[1:6] == '我想对你说':
            return 'tell_me'
        else:
            m_message = m_message[1:]
            return m_message
    else:
        return 'incor_format'


def get_message_key_words(func_message):
    """
    通过#号 后的字符输出关键字来得到映射
    :param func_message: #后的关键词
    :return:
    """
    # print(func_message)
    # 课表
    if func_message.startswith("课表"):
        return func_message
    elif func_message.startswith("root"):
        return "root"
    elif func_message.startswith("tell_me"):
        return func_message
    elif func_message.startswith("incor_format"):
        return func_message
    elif func_message.startswith("开启测温提示"):
        return "开启测温提示"
    elif func_message.startswith("关闭测温提示"):
        return "关闭测温提示"
    elif func_message.startswith("喷人") or func_message.startswith("骂人"):
        return "骂人"
    elif func_message.startswith("微博热") or func_message.startswith("微博热"):
        return "微博热搜"
    elif func_message.startswith("推广广场"):
        return "推广广场"
    else:
        pass