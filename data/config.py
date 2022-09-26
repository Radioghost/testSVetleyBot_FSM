import os
from data import gars

import pandas as pd
from pandas import DataFrame
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins = [
    208068269
]


garlands = {
    'Белый белт': pd.DataFrame(gars.copy_wb_df),
    'Прованс (большой разъем)': pd.DataFrame(gars.copy_pbig_df),
    'Прованс (малый разъем)': pd.DataFrame(gars.copy_psm_df),
    'Нить теплая': pd.DataFrame(gars.copy_tH_df),
    'Нить холодная': pd.DataFrame(gars.copy_tc_df),
    'Занавес 2*6': pd.DataFrame(gars.copy_c26_df),
    'Занавес 3*3': pd.DataFrame(gars.copy_c33_df)
}

async def setDateAndDescrToLen(leng, date,description, df=pd.DataFrame):
    idx_of_len = df[df['len']==leng].index.values.astype(int)
    flag = False
    for i in range(len(idx_of_len)):
        #df_df = df.iat[idx_of_len[i], 1]
        if flag: break
        if date in df.iat[idx_of_len[-1],1]:
            print('Нет свободных в эту дату')
            return 'Нет сободных в эту дату'
            break
        if date in df.iat[idx_of_len[i],1]:
            continue
        else:
            df.iat[idx_of_len[i],1].append(date)
            df.iat[idx_of_len[i], 2].append(description)
            flag = True


