import pandas as pd
#import numpy as np

def prepare_sheet():
	df = pd.ExcelFile(r"/home/varun/Desktop/Project/survey.xlsx")
	df = df.parse('Primary NAR',skiprows = 10 ,na_values = ['NA'])
	df.columns=['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11',
	'S12','S13','S14','S15','S16','S17','S18','S19','S20','S21','S22','S23','S24']
	df = df.drop(['S23','S24'],axis=1)
	#df = df.groupby(['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11',
	#'S12','S13','S14','S15','S16','S17','S18','S19','S20','S21','S22','S23','S24'])

	#df = pd.DataFrame(np.random.randn(6,24),columns=list('ABCDEFGHIJKLMNOPQRSTUVWX'))

	df = df.iloc[:-21,:]
	 
	df = df.dropna(axis='columns',how='all')
	#df = df.dropna(axis='rows',how='all')
	#df = df[df.C.str.contains("-") == False]

	df = df.convert_objects(convert_numeric=True)
	#df = df.dropna(axis='rows',how='any')


	#df = df.reset_index(drop=True)
	#df =list(df)
	df.to_excel('FIRST_cleaned_pnar.xlsx',index = False)

prepare_sheet()