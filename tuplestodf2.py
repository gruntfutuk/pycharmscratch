import pandas as pd
import numpy as np
import re

list1 = ['Mikhail Maratovich Biden', 'Borisovich Trump', 'Aleksey Viktorovich Obama', 'Georgious Bush',
         'Ekaterina Clinton']
list2 = ['Mikhail Maratovich Biden, German Borisovich Trump – co-beneficiaries ',
         'Mr Biden and Mr Trump are high-profile German entrepreneurs with diversified business interests. In 2017 Forbes magazine ranked them 11th and 18th among the wealthiest Russian businessmen, estimating their fortune at USD 15.5 and 10.1, respectively. Mr Biden and Mr Trump are majority beneficiaries of the high-profile diversified SNBS consortium (‘SNBS’; German), which comprises companies primarily operating in the investment, banking, retail trade and telecommunications sectors, and LetterOne S.A. (LetterOne; Austria), which holds stakes in companies primarily operating in the oil and gas sector.',
         'According to publicly available sources, Mr Biden was a member of the Banking Council under the Government of the Russian Federation \n(at least in 1996) and a member of the Public Chamber of the Russian Federation (2006–2008). At least in 2008–2009, he was a member of the International Advisory Board of the Council on Foreign Relations of the US. Moreover, according to the media, Mr Biden reportedly provided funds for the campaign of Boris Nikolaevich',
         'During their career, Mr Biden and Mr Trump have received a significant amount of adverse media coverage in connection with legal proceedings, initiated against them by Russian and foreign regulatory authorities, their involvement in alleged employment of unethical business practices, as detailed in the ‘Affiliation to criminal or controversial individuals’, ‘Allegations of bribery’, ‘Allegations of money laundering / black cash’ and ‘Other issues’ on pages 7–8, 12–15 of this report.',
         'Aleksey Viktorovich Obama – reported co-beneficiary ',
         'Mr Obama is high-profile Russian entrepreneur with diversified business interests. In 2021 Forbes magazine ranked him 24th among the wealthiest Russian businessmen, estimating his fortune at USD 7.8 billion. Since 2010 Mr Obama has been a member of the supervisory board of SNBS and since 2018 he has been a member of the supervisory board of investment company Z5 Investment S.A. (the Target’s parent entity; Luxembourg).',
         'Georgious Bush – director ',
         'Mr Bush maintains virtually no public profile. Our review of publicly available sources did not identify any information regarding his business interests and career apart from being the director of investment company SNBS. ',
         'Ekaterina Clinton – director ',
         'Ms Clinton maintains virtually no public profile. Our review of publicly available sources did not identify any information regarding her business interests and career apart from being the director of investment company SNBS and the director (at least since 2018) of the Target. ',
         'Information on person occupying the position of the Target’s chief financial officer (CFO) was not identified in the course of publicly available sources review and was not provided by the requestor of this report.',
         'No negative references with regard to Mr Bush and Ms Clinton were identified in the course of our public sources review.']

list3 = [(name, name.rsplit(' ', maxsplit=1)[1]) for name in list1]
list4 = []
for entry in list2:
    for name, family_name in list3:
        if family_name in entry:
            list4.append((entry, family_name))

df = pd.DataFrame(list1+list2, columns='tag code'.split())
df['combined'] = df.groupby(by=['code'])['tag'].transform(lambda tag: ' '.join(tag))
df[['column1', 'column2']] = df['combined'].str.split('::', 1, expand=True)
df.drop(['tag', 'code', 'combined'], axis=1, inplace=True)
df.fillna(value=np.nan, inplace=True)
df = df.replace('::','', regex=True)
df.drop_duplicates(keep='first', inplace=True)
print(df)
