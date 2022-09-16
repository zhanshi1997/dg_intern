import numpy as np
import pandas as pd
import xlrd
import pickle

workfile = xlrd.open_workbook(r"/Users/zhan/dg_intern/DataSets/US_trade_in_goods_and_services.xls")
sheet = workfile.sheet_by_index(0) # sheet 1
year =  sheet.cell(6:62,0).value
print(year[0])
