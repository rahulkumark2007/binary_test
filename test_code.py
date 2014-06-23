import unittest
from rahulkumar_2_5 import sortSalesData
from collections import OrderedDict,namedtuple


class SalesDataTest(unittest.TestCase):
	""" Unit test for testing the code for expected result. This test uses file sales_data.csv """
	
	def test_salesData(self):
		data = namedtuple('data', ['price', 'year', 'month'])
		expected_output = OrderedDict([('CompanyA', data(price=100, year='1990', month='Jan')), 
		('CompanyB', data(price=90, year='1990', month='Jan')), 
		('CompanyC', data(price=100, year='1990', month='March')), 
		('CompanyD', data(price=110, year='1990', month='March')), 
		('CompanyE', data(price=70, year='1990', month='April')), 
		('CompanyF', data(price=80, year='1990', month='Feb'))])
		
		self.assertDictEqual(sortSalesData('sales_data.csv'),expected_output)

		
if __name__ == '__main__':
	unittest.main()