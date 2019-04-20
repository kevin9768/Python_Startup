#==========================================================
# Libraries

import requests
from io import StringIO
import pandas as pd
from datetime import datetime

#==========================================================
# Function
def reviseno(no):
    no_list = list(no)
    if no_list[0]=='0':
        no = '="' + no + '"'
    return no

def getno(dt):
    no = str(input("證券代號: "))
    no = reviseno(no)
    while not no in dt['收盤價']:
        if no == "exit":
            return no
        print("無此代號！")
        no = str(input("證券代號: "))
        no = reviseno(no)
    return no


#==========================================================
# Main Function

# 取得現在時間
datestr = datetime.today().strftime('%Y-%m-%d')

print("請勿頻繁開關此程式，以免無法存取證交所資料。")
print("資料讀取中，請稍候。")
# 下載股價
r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
print("讀取完畢。")

# 整理資料，變成表格
df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
for i in r.text.split('\n') 
    if len(i.split('",')) == 17])), header=0)

dt = df.set_index('證券代號').to_dict()


print("輸入exit以退出。")

no = getno(dt)
while no!="exit":

    print("收盤價: %s" % dt['收盤價'][no])
    no = getno(dt)