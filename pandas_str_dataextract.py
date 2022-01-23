import pandas as pd

"""want to extrac lattitude and longitude data from a column containing
multiline strings where the lat and long are in the last line in the format
(<lat>, <long>)
"""

data = [['name', 'geo'],
        ['alpha', '145 Here Raod\nThere, Place\n(10.7654, -94.54332)'],
        ['beta', '12121 Audelia Road\nDallas, Texas\n(32.91251, -96.718124)'],
        ]

df = pd.DataFrame(data[1:], columns=data[0])
df[['Lat', 'Long']] = df['geo'].str.rsplit('\n', n=1).str[1].str.slice(1, -1).str.split(',', expand=True)

print(df[['name', 'Lat', 'Long']])
