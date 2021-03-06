import csv
from collections import OrderedDict, namedtuple


def sortSalesData(fileName):
	salesData = OrderedDict()
	try:
	
		with open(fileName,'rb') as f:
			reader = csv.reader(f)
			data = namedtuple('data', ['price', 'year', 'month'])
			salesData = OrderedDict()
			names = next(reader)[2:]
			for name in names:
				#initialize the dict
				salesData[name] = data(0, 'year', 'month')
			for row in reader:
				year, month = row[:2]         # Use year, month, *prices = row 
				for name, price in zip(names, map(int, row[2:])): # map(int, prices) 
					if salesData[name].price < price:
						salesData[name] = data(price, year, month)

		print "Company\t\t","Year\t","Month\t","SharePrice(Max)\t"		
		for comp,compData in salesData.iteritems():

				print comp,"\t",compData.year,"\t",compData.month,"\t",compData.price #Print data finally from dict and namedTuple
	except IOError:
		print("Error in Reading File!")
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
		
	return salesData
	
	
sortSalesData('sales_data.csv') #provide File name to be read.