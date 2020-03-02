import function_list
import message_judge.handle_message as handle_message


def function_recognition(data):
    """
    通过字典建立 swtich，case映射调用相关的函数
    :param data: Json数据
    :return: 通过字典映射到各个功能的函数中去
    """
    type = handle_message.get_message_type(data)
    m_message = (data['message'][0]['data']['text'])
    m_font = (data['font'])
    m_message_id = (data['message_id'])
    m_message_type = (data['message_type'])
    m_post_type = (data['post_type'])
    m_raw_message = (data['raw_message'])
    m_qq_id = (data['self_id'])
    m_sender_info = (data['sender'])
    m_sub_type = (data['sub_type'])
    m_time = (data['time'])
    func_message = handle_message.get_message_content(m_message)
    key_words = handle_message.get_message_key_words(func_message)
    # print(func_message)
    switch = {
        '课表': function_list.school_table,
        'incor_format': function_list.incorrect_format,
        'tell_me': function_list.want_to_tell_me,
        'root': function_list.root_to_user,
        '微博热搜': function_list.get_weibo_hot,
        "推广广场": function_list.square_extension
    }
    switch.get(key_words, function_list.default)(data)


if __name__ == '__main__':
    str2 = "root 2763359332 123"
    if str2.startswith("root"):
        print(str2)
