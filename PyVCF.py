import pandas as pd

table = pd.read_table('/Users/Manasee/Documents/Vollenhovia/filtered2.recode.snpEff.vcf',skiprows=59,header=None,usecols=[0,1,29],nrows=5000000)
table["new"]=table[29].str[0:3]
print(table)
count=table["new"].value_counts()
print(count)

table2 = pd.read_table('/Users/Manasee/Documents/Vollenhovia/filtered2.recode.snpEff.vcf',skiprows=59,header=None,usecols=[0,1,30],nrows=5000000)
table2["new"]=table2[30].str[0:3]
print(table2)
count2=table2["new"].value_counts()
print(count2)
