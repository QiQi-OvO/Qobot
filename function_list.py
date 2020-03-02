from function_implementation import basic_function
from function_implementation import school_time_tables
from function_implementation import weibo_data
import main_sender


def default(data):
    sender_data = basic_function.no_function_tip(data)
    main_sender.send_data(data, sender_data)


def want_to_tell_me(data):
    sender_data = basic_function.tell_me(data)
    main_sender.send_data(data, sender_data)


def incorrect_format(data):
    sender_data = basic_function.incor_format(data)
    main_sender.send_data(data, sender_data)


def school_table(data):
    sender_data = school_time_tables.main_run(data)
    main_sender.send_data(data, sender_data)


def root_to_user(data):
    sender_data = basic_function.root_to_user(data)
    main_sender.send_data(data, sender_data)


def get_weibo_hot(data):
    sender_data = weibo_data.weibo_hot_search(data)
    main_sender.send_data(data, sender_data)


def square_extension(data):
    sender_data = basic_function.broadcast_message(data)
    main_sender.send_data(data, sender_data)


if __name__ == '__main__':
    str2 = "123 sjhid dhi"
    list2 = str2.split()
    print(list2)
