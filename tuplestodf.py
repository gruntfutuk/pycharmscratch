import pandas as pd
import numpy as np
import re

list1 = ['abc 1', 'abc 2', 'abc 3', 'abc 4']
list2 = ['zzz 1 zz', 'zzz zz 2', 'xxx 2 xx', 'zzz zz 4', 'yyy 4 yy']
list1 = [(entry + '::', re.search(r'\d+', entry).group()) for entry in list1]
list2 = [(entry, re.search(r'\d+', entry).group()) for entry in list2]
df = pd.DataFrame(list1+list2, columns='tag code'.split())
df['combined'] = df.groupby(by=['code'])['tag'].transform(lambda tag: ' '.join(tag))
df[['column1', 'column2']] = df['combined'].str.split('::', 1, expand=True)
df.drop(['tag', 'code', 'combined'], axis=1, inplace=True)
df.fillna(value=np.nan, inplace=True)
df = df.replace('::','', regex=True)
df.drop_duplicates(keep='first', inplace=True)
print(df)
