import datetime

import numpy as np
import pandas as pd


white_belt = pd.Series([12,14,18,18,22,22,22,22], name='white_belt')
cover_3_3 = pd.Series([3,3,3,3,3])
cover_2_6 = pd.Series([2,2,2,2])
thread_high = pd.Series([50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50])
thread_cold = pd.Series([50,50,50,50,50,50,50,50,50,50,50,50])
provance_big = pd.Series([10,10,10,10,10,10])
provance_small = pd.Series([10,10,10,10])



#сохранить данные о бронировании. каждому сериес присвоить датафр, где ключ - длинна, значение дата брони.
psm_add = {
    'len':provance_small,
    'date': [[''],[''],[''],['']],
    'descr': [' ... ',' ... ',' ... ',' ... ']
}
psm_df = pd.DataFrame(psm_add)
copy_psm_df = pd.DataFrame(psm_add)

pbig_add = {
    'len': provance_big,
    'date': [[''],[''],[''],[''],[''],['']],
    'descr': [[''],[''],[''],[''],[''],['']]
}
pbig_df = pd.DataFrame(pbig_add)
copy_pbig_df = pd.DataFrame(pbig_add)


tc_add = {
    'len': thread_cold,
    'date':[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],
    'descr':[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']]
}
tc_df = pd.DataFrame(tc_add)
copy_tc_df = pd.DataFrame(tc_add)

c26_add = {
    'len': cover_2_6,
    'date': [[''],[''],[''],['']],
    'descr': [[''],[''],[''],['']]
}
c26_df = pd.DataFrame(c26_add)
copy_c26_df = pd.DataFrame(c26_add)

c33_add = {
    'len': cover_3_3,
    'date': [[''],[''],[''],[''],['']],
    'descr': [[''],[''],[''],[''],['']]
}
c33_df = pd.DataFrame(c33_add)
copy_c33_df = pd.DataFrame(c33_add)


tH_add = {
    'len' : thread_high,
    'date' :[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],
    'descr': [[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']]
}
tH_df = pd.DataFrame(tH_add)
copy_tH_df = pd.DataFrame(tH_add)


wb_add = {
    'len' : white_belt,
    'date':[[''],[''],[''],[''],[''],[''],[''],['']],
    'descr': [[''],[''],[''],[''],[''],[''],[''],['']]
}
wb_df = pd.DataFrame(wb_add)
copy_wb_df = pd.DataFrame(wb_add)

#обращение к ячейке и изменение её

#todo написать сеттеры и геттеры для дат и описаний
def getIndexOfLen(leng, type=pd.DataFrame):
    x = type[type['len']== leng].index.values.astype(int)
    return x

def getIndexOfDate(date, df=pd.DataFrame):
    #x = datetime.date.fromisoformat(date)
    y = df[df['date']==date].index.values.astype(int)
    return y

def getDescrFromDate(date, type=pd.DataFrame):
    y=date
    idx = getIndexOfDate(date,type)
    msg =[]
    for i in range(len(type)):
        x = type.iat[i,1]
        if y in x:
            z = type.iat[i,2]
            if z!=' ':
                msg.append(f'На дату: {x}, заметка: {z} ')
            else: return f'На дату {x}, заметок нет'
            # print(msg)
    return msg


def getDateFromLen(leng, type = pd.DataFrame,):
    i = getIndexOfLen(leng,type)
    result = []
    result2 = []
    for y in range(len(i)):
        z=i[y]
        result.append(type._get_value(z,'date'))
    return result

def setDateAndDescrToLen(leng, date,description, df=pd.DataFrame):
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

def removeDateAndDescrToLen(leng, date, df=pd.DataFrame):
    idx_of_len = df[df['len']==leng].index.values.astype(int)
    flag = False
    for i in range(len(idx_of_len)):
        #df_df = df.iat[idx_of_len[i], 1]
        if flag: break

        if date in df.iat[idx_of_len[i],1]:

            index = df.iat[idx_of_len[i], 1].index(date)
            df.iat[idx_of_len[i], 1].remove(date)
            df.iat[idx_of_len[i], 2].pop(index)
            # df.iat[idx_of_len[i], 2].append(description)
            flag = True

        if date not in df.iat[idx_of_len[-1], 1]:
            print('Нет таких дат в расписании')
            return 'Нет таких дат в расписании'
            flag = True
            break

def getDataOfLengs(leng,df = pd.DataFrame):
    idx_of_len = df[df['len'] == leng].index.values.astype(int)
    df_df = df.iloc[idx_of_len]
    print(df_df)
    return df_df

