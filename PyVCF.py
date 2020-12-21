import pandas as pd

table = pd.read_table('/Users/Manasee/Documents/Vollenhovia/filtered2.recode.snpEff.vcf',skiprows=59,header=None,usecols=[0,1,9],nrows=10000000)
print(table)
table["new"]=table[9].str[0:3]
print(table)
count=table["new"].value_counts()
print(count)
