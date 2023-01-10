import pandas as pd
import numpy as np
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
import requests
import json
import csv
import time
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from redash_dynamic_query import RedashDynamicQuery

redash = RedashDynamicQuery(
endpoint='https://redash.goibibo.com',
apikey='kdxvxHGOhFQcP5XMytV9Pn0kCzIEBk1lXS7pGpBW'
)
c_date = datetime.today().strftime("%Y_%m_%d")
print(c_date)

query_id = 41220
result = redash.query(query_id)
gi= pd.DataFrame(result['query_result']['data']['rows'])
# using for column sequence
gi=gi[['report_day','uuid','job_id','hotel_code','mmt_hotel_code','voyager_hotel_code','req_origin','sector','vendor','flavour','hotel_name','city_code','country_code','checkin','checkout','pax','MMT_Final_Price','MMT_Price_Rank','MMT_avg_rank','GIB_Final_Price','GIB_Price_Rank','GIB_avg_rank','BKG_Final_Price','BKG_Price_Rank','BKG_avg_rank','EXP_Final_Price','EXP_Price_Rank','EXP_avg_rank','AGD_Final_Price','AGD_Price_Rank','AGD_avg_rank','YTR_Final_Price','YTR_Price_Rank','YTR_avg_rank','HEG_Final_Price','HEG_Price_Rank','HEG_avg_rank','easemytrip_Final_Price','easemytrip_Price_Rank','easemytrip_avg_rank','CTP_Final_Price','CTP_Price_Rank','CTP_avg_rank','gommt_cheapest_price','top3_cheapest_price','rank_1_Final_Price','rank_1_Vendor','rank_2_Final_Price','rank_2_Vendor','rank_3_Final_Price','rank_3_Vendor','MBL','MBL_top3','MBL_vsB']]

file_name = "FW_HPA_Parity_Data#_Athena_" + c_date + ".csv"
gi.to_csv(file_name,index=False)
print("completed")