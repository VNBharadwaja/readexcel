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

for i in range(2, row_count+1):
    for j in range(1, col_count+1):
        key   = wsheet.cell(row=i, column=1).value

        value.append(wsheet.cell(row=i, column=j).value)
        print (value)
        dataDict[key] = value

#prompt user for input
userInput = input("Please enter an id to find a person's details: ")

print (dataDict.get(int(userInput)))
