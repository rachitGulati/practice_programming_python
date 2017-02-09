'''
Title: Fibonacci series with memorization
Started On: 9th Feb,2017
Output:
Enter element position sequence in fibonacci series: 8
21
Do want to continue Y/N: Y
Enter element position sequence in fibonacci series: 2
1
Do want to continue Y/N: Y
Enter element position sequence in fibonacci series: 3
2
Do want to continue Y/N: N
'''
import sys
#Function to return nth term in fibonacci series:
fibonacci_dic = []
fibonacci_dic.insert(0,0)
fibonacci_dic.insert(1,1)
def fibonacci(num):
	if len(fibonacci_dic) >  num:
		return fibonacci_dic[num]
	else:
		result = fibonacci(num-1) + fibonacci(num-2)
		fibonacci_dic.insert(num, result)
		return result
def looping():
	count = input('Enter element position in fibonacci series: ')
	print fibonacci(count)
	response = raw_input('Do you want to continue (Y/N)?: ')
	if response == 'Y':
		looping()
	else:
		sys.exit();

looping()

"""

EXTRA:

The difference is that raw_input() does not exist in Python 3.x, while input() does.
raw_input() takes exactly what the user typed and passes it back as a string.
input() first takes the raw_input() and then performs an eval() on it as well.
"""
