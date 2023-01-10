import os
from pathlib import Path

filepath1 = 'C:/CHKING/file_001.csv'
filepath2 = 'C:/CHKING/002.xlsx'
filepath3 = 'C:/CHKING/macro_file.xlsm'
filepath4 = 'C:/CHKING/binary_file.xlsb'

absolute_path = Path(filepath1 ).resolve()
print(absolute_path)
os.system(f'start excel.exe "{absolute_path}"')