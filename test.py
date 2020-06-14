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

		#case 2, A is rational no. and B is rational no. p/q form
		sol = self.app.get('/add?A=5/3&B=7/2')
		self.assertEqual(b'5.16666666667', sol.data)

	def test_add3(self):

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

	def test_div1(self):
		#case 1, A is n int B is an int
		sol= self.app.get('/div?A=10&B=5')
		self.assertEqual(b'2.0', sol.data)

	def test_div2(self):

		#case 2, A is rational no. and B is rational no. p/q form
		sol = self.app.get('/div?A=7/2&B=27/4')
		self.assertEqual(b'0.518518518519', sol.data)

	def test_div3(self):

		#case 3, A is a float and B is a float
		sol = self.app.get('/div?A=0.0789&B=9102.232')
		self.assertEqual(b'8.66820357908e-06', sol.data)

	def test_div4(self):

		#case 4, when A is float and B is int
		sol = self.app.get('/div?A=32.32&B=67')
		self.assertEqual(b'0.482388059701', sol.data)

	def test_div5(self):

		#case 5, when A is int and B is float
		sol = self.app.get('/div?A=70&B=8.2')
		self.assertEqual(b'8.53658536585', sol.data)

  	def test_sub1(self):
		#case 1, A is n int B is an int
		sol = self.app.get('/suA?A=7&B=3')
		self.assertEqual(b'4.0', sol.data)

	def test_sub2(self):

		#case 2, A is rational no. and B is rational no. p/q form
		sol = self.app.get('/sub?A=8/2&B=9/2')
		self.assertEqual(b'-0.5', sol.data)

	def test_sub3(self):

		#case 3, A is a float and B is a float
		sol = self.app.get('/sub?A=70.2&B=1.901')
		self.assertEqual(b'68.299', sol.data)

	def test_sub4(self):

		#case 4, when A is float and B is int
		sol = self.app.get('/sub?F=32.32&B=4')
		self.assertEqual(b'28.32', sol.data)

	def test_sub5(self):

		#case 5, when A is int and B is float
		sol = self.app.get('/sub?A=22&B=7.201')
		self.assertEqual(b'14.799', sol.data)

  	def test_mul1(self):
		#case 1, A is n int B is an int
		sol = self.app.get('/mul?A=90&B=5')
		self.assertEqual(b'450.0', sol.data)

	def test_mul2(self):

		#case 2, A is rational no. and B is rational no. p/q form
		sol = self.app.get('/mul?A=7/2&B=66/4')
		self.assertEqual(b'57.75', sol.data)

	def test_mul3(self):

		#case 3, A is a float and B is a float
		sol = self.app.get('/mul?A=0.07088&B=60000.00')
		self.assertEqual(b'4252.8', sol.data)

	def test_mul4(self):

		#case 4, when A is float and B is int
		sol = self.app.get('/mul?A=32.32&B=58')
		self.assertEqual(b'1874.56', sol.data)

	def test_mul5(self):

		#case 5, when A is int and B is float
		sol = self.app.get('/mul?A=1500&B=8.89')
		self.assertEqual(b'13335.0', sol.data)

   
if __name__ == '__main__':
	unittest.main()
