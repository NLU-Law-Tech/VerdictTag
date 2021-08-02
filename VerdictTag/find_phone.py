import re


def find_phone(context):
    # 用正則找到判決書中的手機號碼並回傳位置
    # context: string 整篇或部分判決書

    regex = r"(?:手機號|行動號|電話號|手機電|行動電|電|門|手){1}[碼話號機]{1}[之為]?[ 「]{0,2}([0-9]{4}[-─－—–]?[0-9]{3}[-─－—–]?[0-9]{3})(?:SIM)?[^0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A帳戶]{1}|[^編帳]{1}[^ 第0-9\uFF10-\uFF19a-z\uFF41-\uFF5AA-Z\uFF21-\uFF3A：、│警戶鑑字-]{1}[ ]{0,2}([0-9]{4}[-─－—–]?[0-9]{3}[-─－—–]?[0-9]{3})[ ]{0,2}[手機行動電話門號碼SIM」]{1,5}"

    match_text = re.finditer(regex, context)
    phone_number_list = []

    for one in match_text:
        text = one.group()
        # groups() 回傳 regex 內所有的 group 其 match value
        non_none_list = [i for i in one.groups() if i != None]
        # 提取出唯一 match 的 group
        phone_number = non_none_list[0]
        start_pos = one.start() + text.find(phone_number)
        end_pos = start_pos + len(phone_number)

        phone_number_list.append({'start': start_pos, 'end': end_pos, 'value': phone_number, 'type': 'phone'})

    return phone_number_list
