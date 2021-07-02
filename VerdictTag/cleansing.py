
def cleansing(context):
    #資料清洗 去掉換行符\r \n 半形空白 全形空白 tab
    context_clean = context.replace('\n', '').replace('\r', '').replace(" ","").replace('　','').replace("\t","")
    return context_clean