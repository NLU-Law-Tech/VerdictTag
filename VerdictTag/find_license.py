import re

def find_license(context):
    # 用正則找到判決書中的車牌並回傳位置
    # context: string 整篇或部分判決書

    with open('VerdictTag/vehicleType.txt', 'r',encoding='utf-8') as f:
        car_rgs = r"("  
        for line in f.readlines():
            car_rgs += line.replace('\n','') + '|'
        car_rgs = car_rgs[:-1] + ')?'

    rgs = r"(牌照號碼|車牌號碼|車號|車牌|駕駛|駕駛之|駕駛的)(號|為|：|:)?([a-zA-Z0-9]{1,5}[-─－—–][a-zA-Z0-9]{1,5})號?之?的?" + car_rgs

    match_text = re.finditer(rgs, context)
    license_list = []

    for one in match_text:
        license = one.groups()[2]
        vehicleType = one.groups()[3]

        text = one.group()
        start_pos = one.start() + text.find(license)
        end_pos = start_pos + len(license)
        
        license_list.append({'start':start_pos, 'end':end_pos, 'value':license, 'type': 'car', 'vehicleType': vehicleType})
    
    return license_list


