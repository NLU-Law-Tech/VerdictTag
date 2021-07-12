import re

def find_bank(context):
    # 用正則找到判決書中的車牌並回傳位置
    # context: string 整篇或部分判決書

    regex = "(.{0,4})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)(.{0,5})(帳號|帳戶)?[^年元月萬千第百](.{0,11})[^年元月萬第千百][0-9]{0,4}(-|─|－|—|–)?[^年元月萬千百第][0-9]{3,15}(.{0,9})(帳戶|存簿)"
    regex2 = "(.{0,4})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)+(.{0,20})(帳號|帳戶|局號)(.{0,10})[^年元月萬第千百][0-9]{0,4}(-|─|－|—|–)?[^年元第月萬千百][0-9]{3,15}[^年元月第萬千百](號)?(帳戶)?(、)?[0-9]*"


    match = re.finditer(regex, context)
    match2= re.finditer(regex2, context)
    
    bank_list = []

    for one in match:
        start=one.span()[0]
        end=one.span()[1]
        bank_list.append({'start':start, 'end':end})
    for i in match2:
        new=True
        start=i.span()[0]
        end=i.span()[1]
        for j in bank_list:
             if j['start']==start or j['end']==end:
                    new=False
        if new == True:
            bank_list.append({'start':start, 'end':end})
    
    return bank_list
