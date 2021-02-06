import pandas as pd
import re
class exceler():
    def __init__(self):
        return
    def find_date(self,file):
        data = pd.read_excel(file, sheet_name='Sheet1')
        print(data)
        print(data[(data.hire_date >= '2007-01-01')])
        return 
    def sort_dates(self, file):
        data = pd.read_excel(file, sheet_name='Sheet1')
        print(data)
        print(data.sort_values(by = 'hire_date'))
    pass




