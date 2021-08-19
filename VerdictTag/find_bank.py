import re

def find_bank(context):
    # 用正則找到判決書中的車牌並回傳位置
    # context: string 整篇或部分判決書
    f = open('banklist.txt', 'r',encoding='utf-8')
    banknames=[]  #全台銀行名稱
    for line in f.readlines():
        banknames.append(line.replace('\n','').replace(' ',''))
    regex = "((.{0,10})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)(.{0,5})(帳號|帳戶)?(?:(?!年|元|月|萬|千|百|第)\w)(.{0,15})(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(.{0,9})(-|─|－|—|–)?[0-9]{0,3}(帳戶|存簿))|((.{0,8})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)+(.{0,15})(帳號|帳戶|局號)(.{0,15})(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(-|─|－|—|–)?[0-9]{0,3}(?:(?!年|元|月|萬|千|百|第)\w)(號)?(帳戶)?(、)?[0-9]*)"


    match = re.finditer(regex, context)
    
    bank_list = []
    
    for one in match:
#         print(one)
        bank_name=''
        start=one.span()[0]
        orgin_start=start
        end=one.span()[1]
        orgin_end=end
        value=context[start:end]
        if value.find('函')!=-1:
            continue
        bank_name_start=0
        
        regex_bankaccount="[0-9]{0,3}(-|─|－|—|–)?[0-9]{0,3}(-|─|－|—|–)?[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(-|─|－|—|–)?[0-9]{0,8}"
        match_bankaccount=re.finditer(regex_bankaccount, value)
        bank_accounts=[]
        for i in match_bankaccount:
            account_start=i.span()[0]
            account_end=i.span()[1]
            bank_accounts.append(value[account_start:account_end])
        
#             bank_account += re.sub("([^\x00-\x7F])+","",bank)  去掉中文
#             bank_account+=bank
                                        
        start+=account_start
        end=start+account_end-account_start
        branch=''
        for i in banknames:
                    match_bankname=re.finditer(i, value)
                    for j in match_bankname:
                        if bank_name_start<j.span()[0] and j.span()[0]+orgin_start<start:
                            bank_name_start=j.span()[0]
                            bank_name=j.group()
        bank_account=bank_accounts[0]
        if len(bank_accounts)==2:
            branch=bank_accounts[0]
            
            
#         print(bank_name)
#         if branch !='':
#             print("局號:",branch)
        
        bank_list.append({'start':start, 'end':end, 'value':bank_account,'type':'bank'})
    
    return bank_list
