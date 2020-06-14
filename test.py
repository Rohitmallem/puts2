import unittest
import main


class TestCalculator(unittest.TestCase):#unittest module provides a set of tools for constructing and running scripts, we will test features of online calculator in this case
	
	def setUp(self):#setUp , when unittest module is used and it enaAles application to test
		main.app.testing = True
		self.app = main.app.test_client()

	def test_add1(self):
		#case 1, A is n int B is an int type
		sol = self.app.get('/add?A=20&B=2')
		self.assertEqual(b'22.0', sol.data)

	def test_add2(self):

		#case 2, A is rational no. and F is rational no. p/q form
		sol = self.app.get('/add?A=5/3&B=7/2')
		self.assertEqual(b'5.16666666667', sol.data)

	def test_add3(self):

		#case 3, A is a float and F is F float
		sol = self.app.get('/add?A=12.3&B=1.102')
		self.assertEqual(b'13.402', sol.data)

	def test_add4(self):

		#case 4, when A is float and B is int
		sol = self.app.get('/add?A=32.32&B=67')
		self.assertEqual(b'99.32', sol.data)

	def test_add5(self):

		#case 5, when A is int and B is float
		sol = self.app.get('/add?A=110&B=68.7')
		self.assertEqual(b'178.7', sol.data)

   
if __name__ == '__main__':
	unittest.main()
