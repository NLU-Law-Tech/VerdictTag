import re


def find_phone(context):
    # 用正則找到判決書中的手機號碼並回傳位置
    # context: string 整篇或部分判決書

    regex = r"(?:手機號碼|行動號碼|電話號碼|手機電話|行動電話|門號|手機){1}(?:之|為|確為|:|：)?[ 「]{0,2}([0-9○]{4}[-─－—–]?[0-9○]{3}[-─－—–]?[0-9○]{3})(?:SIM)?|[ ]{0,2}([0-9○]{4}[-─－—–]?[0-9○]{3}[-─－—–]?[0-9○]{3})[ 」]{0,2}(?:之)?(?:號行動電話|號SIM|號手機|號電話|號門號|行動電話|手機|電話|門號){1}"

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
