import vcf
vcf_reader = vcf.Reader(open('/Users/Manasee/Documents/Vollenhovia/filtered2.recode.snpEff.vcf', 'r'))
record = next(vcf_reader)
for sample in record.samples: print(record.CHROM,record.POS,sample.sample,sample ['GT'],record.INFO['ANN']) 