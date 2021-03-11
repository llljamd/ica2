def fibo(x):
	if x < 0:
		raise Exception("Invalid Input");

	elif x == 0 or x == 1:
		return x;

	else:
		return fibo(x - 1) + fibo(x - 2);

def fact(x):
	f = 1;
	for i in range(1, x + 1):
		f = fact * i;

	return f;
