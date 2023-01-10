# from cgi import print_arguments
# import pandas as pd

# excel_file = pd.ExcelFile("C:\CHKING\INDEX_MATCH\MASTER.xlsx")

# orders = pd.read_excel(excel_file, sheet_name="ID")
# order_details = pd.read_excel(excel_file, sheet_name="OrderDetails")
# products = pd.read_excel(excel_file, sheet_name="Products")

# df = pd.merge(
#     left=order_details,
#     right=products,
#     left_on="ProductID",
#     right_on="ID",
#     how="inner"
# )

# df["TotalPrice"] = df["ListPrice"] * df["Quantity"]
# df.to_csv("outputs/merge-output.csv", index=False)
