import unittest
import fibonacci
import pytest

#UnitTest
class test_fibo(unittest.TestCase):
	def test1(self):
		self.assertEqual(fibonacci.fibo(0), 0);

	def test2(self):
		self.assertEqual(fibonacci.fibo(3), 2);

	def test3(self):
		with self.assertRaises(TypeError):
			fibonacci.fibo("three");

	def test4(self):
		with self.assertRaises(Exception):
			fibonacci.fibo(-3);

if __name__ == '__main__':
	unittest.main();


#PyTest
def test_1():
	assert fibonacci.fibo(0) == 0;

def test_2():
	assert fibonacci.fibo(3) == 2;

def test_3():
	with pytest.raises(TypeError):
		fibonacci.fibo("three");

def test_4():
	with pytest.raises(Exception):
		fibonacci.fibo(-3);
