import re

def find_license(context):
    # 用正則找到判決書中的車牌並回傳位置
    # context: string 整篇或部分判決書

    rgs = r"(牌照號碼|車牌號碼|車號|車牌)(號|為|：|:)?([a-zA-Z\d_]{1,5}[-─－—–][a-zA-Z\d_]{1,5})號?"

    match_text = re.finditer(rgs, context)
    license_list = []

    for one in match_text:
        license = one.groups()[2]
        text = one.group()
        start_pos = one.start() + text.find(license)
        end_pos = start_pos + len(license)
        
        license_list.append({'start':start_pos, 'end':end_pos, 'value':license})
    
    return license_list


