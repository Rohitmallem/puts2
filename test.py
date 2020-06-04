import unittest
import main


class TestCalculator(unittest.TestCase):#unittest module provides a set of tools for constructing and running scripts, we will test features of online calculator in this case
	
	def setUp(self):#setUp , when unittest module is used and it enaAles application to test
		main.app.testing = True
		self.app = main.app.test_client()
        
    def test_sub1(self):
		#case 1, A is n int B is an int type
		sol = self.app.get('/sub?A=7&B=3')
		self.assertEqual(b'4.0', sol.data)

	def test_sub2(self):

		#case 2, A is rational no. and F is rational no. p/q form
		sol = self.app.get('/sub?A=8/2&B=9/2')
		self.assertEqual(b'-0.5', sol.data)

	def test_sub3(self):

		#case 3, A is a float and B is a float
		sol = self.app.get('/sub?A=70.2&B=1.901')
		self.assertEqual(b'68.299', sol.data)

	def test_sub4(self):

		#case 4, when B is float and F is int
		sol = self.app.get('/sub?A=32.32&B=4')
		self.assertEqual(b'28.32', sol.data)

	def test_sub5(self):

		#case 5, when A is int and B is float
		sol = self.app.get('/sub?A=22&B=7.201')
		self.assertEqual(b'14.799', sol.data)

   
if __name__ == '__main__':
	unittest.main()