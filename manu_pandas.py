from io import StringIO

# ManufacturerList.csv
import pandas as pd

manu_data = """Code, Manufacturer, Cat, Status
1167234,Apple ,phone,
2390112,Dell,laptop,
9034210,Dell,tower,
7346234,Lenovo,laptop,damaged
3001265,Samsung,phone,
2347800,Apple ,laptop,
1009453,Lenovo,tower,"""

#  PriceList.csv
price_data = """Code, Price
3001265,1200
2347800,999
2390112,799
1009453,599
1167234,534
9034210,345
7346234,239"""

# ServiceDateList.csv
service_dates = """Code, Dates
9034210,5/27/2022
2390112,7/2/2022
2347800,7/3/2022
7346234,9/1/2022
1009453,10/1/2023
1167234,2/1/2022
3001265,12/1/2023"""

manufacturing_df = pd.read_csv(StringIO(manu_data))
manufacturing_df['Manufacturer'] = manufacturing_df['Manufacturer'].str.strip()
priceList1_df = pd.read_csv(StringIO(price_data))
serviceList_df = pd.read_csv(StringIO(service_dates))
print(manufacturing_df, priceList1_df, serviceList_df, sep="\n\n")