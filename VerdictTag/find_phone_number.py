import re


def find_phone_number(context):
    # 用正則找到判決書中的手機號碼並回傳位置
    # context: string 整篇或部分判決書

    regex = r"[^編帳]{1}[^ 第0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A：、警戶鑑-]{1}[ ]{0,2}([0-9]{10})[^0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A帳戶]{1}|[^編帳]{1}[^ 第0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A：、警戶鑑-]{1}[ ]{0,2}([0-9]{2}-[0-9]{8})[^0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A帳戶]{1}|[^編帳]{1}[^ 第0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A：、警戶鑑-]{1}[ ]{0,2}([0-9]{4}-[0-9]{6})[^0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A帳戶]{1}|[^編帳]{1}[^ 第0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A：、警戶鑑-]{1}[ ]{0,2}([0-9]{4}-[0-9]{3}-[0-9]{3})[^0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A帳戶]{1}"

    match_text = re.finditer(regex, context)
    phone_number_list = []

    for one in match_text:
        # groups() 回傳 regex 內所有的 group 其 match value
        non_none_list = [i for i in one.groups() if i != None]
        # 提取出唯一 match 的 group
        phone_number = non_none_list[0]
        text = one.group()
        start_pos = one.start() + text.find(phone_number)
        end_pos = start_pos + len(phone_number)

        phone_number_list.append({'start': start_pos, 'end': end_pos})

    return phone_number_list
