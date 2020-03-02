import datetime
import os
import message_judge.handle_message as handle_message

course_table = [[0 for j in range(0, 7)] for i in range(0, 20)]  # 课程的每周的上课 作全局变量
data_list = []  # 文件课程信息 全局变量
char_days = ['一', '二', '三', '四', '五', '六', '日']


CONFIG_PATH = "C:/Users/Administrator/Desktop/课表/" #作宏定义


def get_course_txt(path):
    file = open(path, "r")
    while True:
        mystr = file.readline()  # 表示一次读取一行
        if not mystr:
            # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
            break
        tmp_list = mystr.split()
        data_list.append(tmp_list)


def structured_list():
    course_num = len(data_list)
    for i in range(0, course_num):
        # print(data_list[i])
        course_name = data_list[i][0]
        start_week = int(data_list[i][1])
        end_week = int(data_list[i][2])
        studying_day = int(data_list[i][3])
        for tmp in range(start_week - 1, end_week):
            if course_table[tmp][studying_day - 1] == 0:
                course_table[tmp][studying_day - 1] = course_name
            else:
                course_table[tmp][studying_day - 1] += "+" + course_name


def calculate_day():  # 得到开学的第几周 星期几 date_list[0]是周 date_list[1]是星期几 已经减1了可以直接用，输出要加1
    now_time = datetime.datetime.now()
    # now_time = datetime.datetime(2020,3,2)
    start_school_time = datetime.datetime(2020, 2, 24)
    offfset_days = int((now_time - start_school_time).days)
    offfset_days = offfset_days + 1
    now_week = int(offfset_days / 7) + 1  # 这是第几周
    now_days = offfset_days % 7  # 这是星期几
    if now_days == 0:
        now_days = 7
    date_list = []
    date_list.append(now_week - 1)
    date_list.append(now_days - 1)
    # print()
    return date_list


def calculate_time():
    date_list = calculate_day()
    message = ""
    if course_table[date_list[0]][date_list[1]] == 0:  # 今天没有课
        now_month = datetime.datetime.now().month
        now_day = datetime.datetime.now().day
        message = str(now_month) + "月" + str(now_day) + "日 第" + str(date_list[0] + 1) + "周  星期" + char_days[
            date_list[1]] + "\n" + "今天没有课，好好放松一下吧"
        tmp_week = date_list[0]
        tmp_day = date_list[1] + 1
        while (1):
            if course_table[tmp_week][tmp_day] == 0:  # 如果没有课 继续遍历日期表
                tmp_day += 1
                if tmp_day == 7:
                    tmp_day = 0
                    tmp_week += 1
            else:  # 把最近的一堂课信息输出

                message += "\n" + "[CQ:face,id=30]记得离你最近的一堂课在第" + str(tmp_week + 1) + "周  星期" + char_days[int(tmp_day)]
                message += "\n" + str(div_mul_course(tmp_week, tmp_day))
                # print("记得离你最近的一堂课在第"+str(tmp_week+1)+"周  星期"+str(tmp_day+1))
                # print(div_mul_course(tmp_week,tmp_day))
                break
    else:
        message = "[CQ:face,id=74]新的一天，元气满满,今日课程:" + "\n" + str(div_mul_course(date_list[0], date_list[1]))
        # print("新的一天，元气满满今日课程:")
        # print(div_mul_course(date_list[0],date_list[1]))

    return message


def get_time_by_day_and_name(name, day):
    course_len = len(data_list)
    day = day + 1
    for i in range(course_len):
        if data_list[i][0] == name and int(data_list[i][3]) == int(day):
            message = data_list[i][4] + "-" + data_list[i][5]
            return message
    print("有BUG")


def get_place_by_day_and_name(name, day):
    course_len = len(data_list)
    day = day + 1
    for i in range(course_len):
        if data_list[i][0] == name and int(data_list[i][3]) == int(day):
            message = data_list[i][6]
            return message
    print("有BUG")


def div_mul_course(week, day):  # 把带有+号的datalist分割开来
    message = ""
    course_name = course_table[week][day]
    nPos = course_name.find("+")
    if nPos == -1:
        # print("课程名字:"+str(course_name))
        # print("周:"+str(week))
        # print("星期:"+str(day))
        # print(get_time_by_day_and_name(course_name,day))
        # print(get_place_by_day_and_name(course_name,day))
        message = ("课程的名字:") + course_name + "\n" + ("上课时间:  ") + get_time_by_day_and_name(course_name, day) + "\n" + (
            "上课地点:  ") + get_place_by_day_and_name(course_name, day)
        # print(message)
        return message

    course_tmp_list = []
    while (1):
        course_tmp_list.append(course_name[:nPos])
        course_name = course_name[nPos + 1:]
        nPos = course_name.find("+")
        if nPos == -1:
            course_tmp_list.append(course_name)
            break
    # print(course_tmp_list)
    message = ("有") + str(len(course_tmp_list)) + "节课,分别为:"
    for i in range(len(course_tmp_list)):
        message += "\n" + course_tmp_list[i] + "      上课时间:  " + str(
            get_time_by_day_and_name(course_tmp_list[i], day)) + "   上课地点:  " + str(
            get_place_by_day_and_name(course_tmp_list[i], day))
    return message


def main_run(data):
    global course_table
    data_list.clear()
    course_table.clear()
    course_table = [[0 for i in range(0, 7)] for j in range(0, 20)]
    type = handle_message.get_message_type(data)
    message = ""
    sender_qq = data['user_id']
    path = CONFIG_PATH + str(sender_qq) + ".txt"
    if os.path.exists(path) == False:
        sender_data = {
            'user_id': sender_qq,
            'message': "抱歉，您暂时没有被录入我们的课表系统哦,后续会推出提供文件输入我们的系统,现在请先尝试输入'#联系作者'与作者取得联系",
            'auto_escape': False
        }
        if type == 'private':
            return sender_data
        elif type == 'group':
            sender_data = {
                'group_id': data['group_id'],
                'message': "抱歉，您暂时没有被录入我们的课表系统哦,后续会推出提供文件输入我们的系统,现在请先尝试输入'#联系作者'与作者取得联系",
                'auto_escape': False
            }
            return sender_data
    else:
        get_course_txt(path)
        structured_list()
        message = calculate_time()

        if type == 'private':
            sender_data = {
                'user_id': sender_qq,
                'message': message,
                'auto_escape': False
            }
            return sender_data
        elif type == 'group':
            sender_info = data['sender']
            nick_name = sender_info['nickname']
            message = str(nick_name) + "的课表信息:" + '\n' + calculate_time()
            print(data['group_id'])
            sender_data = {
                'group_id': data['group_id'],
                'message': message,
                'auto_escape': False
            }
            return sender_data


if __name__ == "__main__":
    path = ("C:/Users/Administrator/Desktop/课表/526191197.txt")
    get_course_txt(path)
    structured_list()
    print(calculate_time())
    pass
