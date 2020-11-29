import vcf
vcf_reader = vcf.Reader(open('/Users/Manasee/Documents/Vollenhovia/filtered2.recode.snpEff.vcf', 'r'))
while (1):
	record = next(vcf_reader, 'end')
	for sample in record.samples: 
			print(record.CHROM,record.POS,sample.sample,sample['GT'],record.INFO['ANN'])
			break
	else:
			print (record)
