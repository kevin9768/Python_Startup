#=====================================================================
#Libraries

import pandas as pd
import os

#=====================================================================
#Variables

csvfile = 'DJ_day_market_cap.csv'
df = pd.read_csv(csvfile)

#=====================================================================
#Function

def title(a):
    if 'Unnamed:' in a:
        return False
    else:
        return True

#=====================================================================
#Main Function

file_to_create = False
counter=0
d={}
ftc=str
for i in df.columns:
    if title(i):
        if file_to_create:
            write_df = pd.DataFrame(d)
            if not os.path.exists('./DJ_data'):
                os.mkdir('./DJ_data')
            write_df.to_csv("./DJ_data/%s.csv" % ftc, index=False)
        ftc = i
        d={}
    d[df.iloc[0][counter]]=df[i][1:]
    counter+=1
    file_to_create = True
