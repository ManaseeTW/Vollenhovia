import vcf
import pandas as pd

vcf_reader = vcf.Reader(open('/Users/Manasee/Documents/Vollenhovia/filtered2.recode.snpEff.vcf', 'r'))
for sample in range(2,5):
	record = next(vcf_reader)

list = []
for sample in record.samples: 
	print(list.append((record.CHROM,record.POS,sample.sample,sample ['GT'],record.INFO['ANN'])))
print(list)



df = pd.DataFrame([list])
print(type(df))

df2 = pd.DataFrame()
df2 = df.append(pd.DataFrame([record.samples])).transpose()
print(df2)
