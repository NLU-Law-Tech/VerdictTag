import re
#一開始就會先用正則找包含帳戶跟銀行的一段話 找銀行就只要再從那段話中抓出來名稱就好 
def find_bank(context):
    # 用正則找到判決書中的車牌並回傳位置
    # context: string 整篇或部分判決書

    regex = "((.{0,4})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)(.{0,5})(帳號|帳戶)?(?:(?!年|元|月|萬|千|百|第)\w)(.{0,11})(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(.{0,9})(帳戶|存簿))|((.{0,4})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)+(.{0,20})(帳號|帳戶|局號)(.{0,10})(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(?:(?!年|元|月|萬|千|百|第)\w)(號)?(帳戶)?(、)?[0-9]*)"


    match = re.finditer(regex, context)
    
    bank_list = []

    for one in match:
        print(one)
        start=one.span()[0]
        end=one.span()[1]
        value=context[start:end]
        if value.find('函')!=-1:
            continue
        regex_bankaccount="[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(-|─|－|—|–)?[0-9]{0,8}"
        match_bankaccount=re.finditer(regex_bankaccount, value)
        bank_account=''
        for i in match_bankaccount:
            
            account_start=i.span()[0]
            account_end=i.span()[1]
            bank_account=value[account_start:account_end]
#             bank_account += re.sub("([^\x00-\x7F])+","",bank)  去掉中文
#             bank_account+=bank
                                                                   #之後需要加上局號的值就把output的start提前幾個字(約10)然後再做一次正則(regex_bankaccount最前面加上局號 or 中間可以夾幾個垃圾字)找
        start+=account_start
        end=start+account_end-account_start
            
        
        bank_list.append({'start':start, 'end':end, 'value':bank_account,'type':'bank'})
    
    return bank_list
