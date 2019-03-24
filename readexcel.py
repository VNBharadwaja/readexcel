#! "C:\Program Files (x86)\Python37-32\python.exe"

import openpyxl

from openpyxl import load_workbook

file = "MOCK_DATA.xlsx"

#load the work book
wb_obj = load_workbook(filename = file)

wsheet = wb_obj['MOCK_DATA']

#dictionary to store data
dataDict = {}
value = []
row_count = wsheet.max_row
col_count = wsheet.max_column

for key, *values in wsheet.iter_rows():
    dataDict[key.value] = [v.value for v in values]

print (dataDict)

#prompt user for input
userInput = input("Please enter an id to find a person's details: ")

print (dataDict.get(int(userInput)))
