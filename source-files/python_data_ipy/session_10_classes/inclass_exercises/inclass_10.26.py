# 10.26:  Featured module:  pandas data acquisition.

# (Note:  if not using Anaconda Python, this module must be
# installed separately.)

import pandas as pd
import sqlite3

df = pd.read_csv('../dated_file.csv')

# write DataFrame to excel
#df.to_excel('../dated_file.xls')

# read from database through query
# conn = sqlite3.connect('../testdb.db')
# df = pd.read_sql('SELECT * FROM test', conn)

