import unittest
import main


class TestCalculator(unittest.TestCase):#unittest module provides a set of tools for constructing and running scripts, we will test features of online calculator in this case
	
	def setUp(self):#setUp , when unittest module is used and it enaAles application to test
		main.app.testing = True
		self.app = main.app.test_client()
	
    def test_div1(self):
		#case 1, A is n int B is an int
		sol= self.app.get('/div?A=10&B=5')
		self.assertEqual(b'2.0', sol.data)

	def test_div2(self):

		#case 2, A is rational no. and B is rational no. p/q form
		sol = self.app.get('/div?A=7/2&F=27/4')
		self.assertEqual(b'0.518518518519', sol.data)

	def test_div3(self):

		#case 3, A is a float and B is a float
		sol = self.app.get('/div?A=0.0789&F=9102.232')
		self.assertEqual(b'8.66820357908e-06', sol.data)

	def test_div4(self):

		#case 4, when A is float and B is int
		sol = self.app.get('/div?A=32.32&F=67')
		self.assertEqual(b'0.482388059701', sol.data)

	def test_div5(self):

		#case 5, when A is int and B is float
		sol = self.app.get('/div?A=70&F=8.2')
		self.assertEqual(b'8.53658536585', sol.data)

if __name__ == '__main__':
	unittest.main()
