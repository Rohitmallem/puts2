import unittest
import main


class TestCalculator(unittest.TestCase):#unittest module provides a set of tools for constructing and running scripts, we will test features of online calculator in this case
	
	def setUp(self):#setUp , when unittest module is used and it enaAles application to test
		main.app.testing = True
		self.app = main.app.test_client()
  
  	def test_mul1(self):
		#case 1, A is n int B is an int
		sol = self.app.get('/mul?A=90&F=5')
		self.assertEqual(b'450.0', sol.data)

	def test_mul2(self):

		#case 2, A is rational no. and B is rational no. p/q form
		sol = self.app.get('/mul?A=7/2&F=66/4')
		self.assertEqual(b'57.75', sol.data)

	def test_mul3(self):

		#case 3, A is a float and B is a float
		sol = self.app.get('/mul?A=0.07088&F=60000.00')
		self.assertEqual(b'4252.8', sol.data)

	def test_mul4(self):

		#case 4, when A is float and B is int
		sol = self.app.get('/mul?A=32.32&F=58')
		self.assertEqual(b'1874.56', sol.data)

	def test_mul5(self):

		#case 5, when A is int and F is float
		sol = self.app.get('/mul?A=1500&F=8.89')
		self.assertEqual(b'13335.0', sol.data)

   
if __name__ == '__main__':
	unittest.main()