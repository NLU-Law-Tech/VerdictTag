import re

def find_bank(context):
    # 用正則找到判決書中的車牌並回傳位置
    # context: string 整篇或部分判決書
    f = open('banklist.txt', 'r',encoding='utf-8')
    bank_rgs = r"("
    for line in f.readlines():
        bank_rgs += line.replace('\n','') + '|'
    bank_rgs = bank_rgs[:-1] + ')'
    regex = "((.{0,10})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)(.{0,5})(帳號|帳戶)?(?:(?!年|元|月|萬|千|百|第)\w)(.{0,15})(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(.{0,9})(-|─|－|—|–)?[0-9]{0,3}(帳戶|存簿))|((.{0,8})(銀行|郵局|郵政|信託|世華|金庫|商銀|企銀|開發|信合社|漁會|農會|信用合作社|中央信託局)+(.{0,15})(帳號|帳戶|局號)(.{0,15})(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(-|─|－|—|–)?[0-9]{0,3}(?:(?!年|元|月|萬|千|百|第)\w)(號)?(帳戶)?(、)?[0-9]*)"


    match = re.finditer(regex, context)
    
    bank_list = []
    
    for one in match:
        print(one)
        bank_name=''
        start=one.span()[0]
        orgin_start=start
        end=one.span()[1]
        orgin_end=end
        value=context[start:end]
        if value.find('函') !=-1 or value.find('明細') !=-1:
            continue
        
        
        regex_bankaccount="[0-9]{0,3}(-|─|－|—|–)?[0-9]{0,3}(-|─|－|—|–)?[0-9]{1,7}(-|─|－|—|–)?(?:(?!年|元|月|萬|千|百|第)\w)[0-9]{3,15}(-|─|－|—|–)?[0-9]{0,8}"
        match_bankaccount=re.finditer(regex_bankaccount, value)
        bank_accounts=[]
        for i in match_bankaccount:
            account_start=i.span()[0]
            account_end=i.span()[1]
            bank_accounts.append(value[account_start:account_end])

        start+=account_start
        end=start+account_end-account_start
        branch=''
        bank_name_start=0
        match_bankname=re.finditer(bank_rgs, value)
        for j in match_bankname:
#             print(j)
            
            if bank_name_start<j.span()[0] and j.span()[0]+orgin_start<start:#最接近且不超過帳號本身位置
                bank_name_start=j.span()[0]
                bank_name=j.group()
#             print(bank_name_start)
        bank_account=bank_accounts[0]
        if len(bank_accounts)==2:
            branch=bank_accounts[0]
            
            
#         print(bank_name)
#         if branch !='':
#             print("局號:",branch)
        
        bank_list.append({'start':start, 'end':end, 'value':bank_account,'type':'bank','bank_name':bank_name,'branch':branch})
    
    return bank_list
