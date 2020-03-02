import requests
import re
import message_judge.handle_message as handle_message


def weibo_hot_search(data):
    url = "https://s.weibo.com/ajax/jsonp/gettopsug?uid=&ref=PC_topsug&url=https%3A%2F%2Fweibo.com%2F%3Fcategory%3D0&Mozilla=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F80.0.3987.122%20Safari%2F537.36&_cb=STK_15830732293633"
    header = {
        'User - Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        'Referer': "https: // weibo.com /?category = 0"
    }

    resp = requests.get(url, headers=header)
    result_list = (re.findall('(?<="word":")(.*?)(?=")', resp.text))
    print(result_list)
    # 去除列表中的重复项
    list_to_del = []
    for i in range(len(result_list)):
        for j in range(0, i):
            if result_list[i] == result_list[j]:
                list_to_del.append(i)
                break
    for i in range(len(list_to_del)):
        del result_list[list_to_del[i]]
    message = ""
    search_num = len(result_list)
    print(resp.text)
    print(result_list)
    for i in range(search_num - 1):
        if i == search_num - 2:
            message += str(i + 1) + ":" + result_list[i]
        else:
            message += str(i + 1) + ":" + result_list[i] + "\n"

    type = handle_message.get_message_type(data)
    if type == 'private':
        sender_data = {
            'user_id': data['user_id'],
            'message': message,
            'auto_escape': False
        }
        return sender_data
    elif type == 'group':
        sender_data = {
            'group_id': data['group_id'],
            'message': message,
            'auto_escape': False
        }
        return sender_data
    else:
        pass


if __name__ == "__main__":
    result_list = ['a', 'b', 'c', 'a']
    list_to_del = []
    for i in range(len(result_list)):
        for j in range(0, i):
            if result_list[i] == result_list[j]:
                list_to_del.append(i)
                break
    for i in range(len(list_to_del)):
        del result_list[list_to_del[i]]
    message = ""
    search_num = len(result_list)
    for i in range(search_num):
        if i == search_num - 1:
            message += str(i) + ":" + result_list[i]
        elif i == 0:
            message += "Top:" + result_list[i] + "\n"
        else:
            message += str(i) + ":" + result_list[i] + "\n"
    print(message)
