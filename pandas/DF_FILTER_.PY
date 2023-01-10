# FILTER 
import pandas as pd
import datetime as dt
file1 = "C://CHKING//Neo_Chain_.csv"

def filter_edate(file,backmonth,datecolumn):
    today = int(dt.datetime.today().strftime("%m"))
    main_df = pd.read_csv(file, index_col=False)
    datecolumn = str(datecolumn)
    main_df[datecolumn] = pd.to_datetime(main_df[datecolumn])
    main_df["month__"] = main_df[datecolumn].dt.month
    filter_df2 = main_df.copy()
    # filter_df2 = main_df[main_df["month__"]<=today]
    # filter_df2 = main_df[main_df["month__"]>=today+backmonth]
    filter_df2.to_csv("C:/CHKING/111.csv")
    # filter_df2 = filter_df2.drop("month__", axis=1)
    print(filter_df2.head())
        

filter_edate(file1,0,"Booking_Date")
