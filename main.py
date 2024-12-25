import pandas as pd

# Give the location of the file
amexfile = "amex.xlsx"
goexfile = "goexpense.xlsx"

dfamexraw = pd.read_excel(amexfile, skiprows=6)
dfgoexraw = pd.read_excel(goexfile)

dfamex = dfamexraw.copy(deep=True)
dfgoex = dfgoexraw.copy(deep=True)

dfamex.drop(['Foreign Spend Amount', 'Commission', 'Exchange Rate', 'Additional Information', 'Appears On Your Statement As', 'Address', 'Town/City', 'Postcode', 'Country'], axis=1, inplace=True)

dfgoex.drop(['Explanation Details','Item Status Date', 'Paid Date','Submission Date','Submitted By','Employee Name', 'Submission Office Name', 'Local Amount Currency', 'Receipt Required', 'Additional Detail', 'Receipts', 'Foreign Currency', 'Exchange Rate', 'Foreign Amount', 'Tax', 'Document Number', 'Item Number', 'Supplier Address', 'Supplier City', 'Supplier Chain'], axis=1, inplace=True)

dfgoex.insert(0, 'New_ID', range(880, 880 + len(dfgoex)))

print("AMEX columns")
print(list(dfamex))
print("\n")

print("Go Expense columns")
print(list(dfgoex))
print("\n")

print("AMEX columns")
print(dfamex)
print("\n")

print("Go Expense columns")
print(dfgoex)
print("\n")

autorecondf = pd.DataFrame(columns=['AMEXDate', 'AMEXProcessed', 'GoExDate', 'AMEXAmount', 'GoExAmount', 'AMEXDesc', 'GoExDesc', 'AMEXID', 'GoExID'])
#autoreconnned list
#persistent list with: all the transactions that have been processed 
#all the goexpense lines that have been mapped so far
#AMEX has Reference col as ID
#give 

#start with oneoff version
#then need to do a version that can take updated version of each file and check for (updated lines), new lines, lines that 'undo' previous ones 
