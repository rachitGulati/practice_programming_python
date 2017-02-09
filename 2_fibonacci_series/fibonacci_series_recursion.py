'''
Title: Fibonaci series with recursion
Started On: 9th Feb,2017
Extra Knowledge: 
What are the practical example of the fibonacci series ?.
1) Fibonacci search technique.
In computer science, the Fibonacci search technique is a method of searching a sorted array using a divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers. Compared to binary search where the sorted array is divided into two arrays which are both examined recursively and recombined, Fibonacci search only examines locations whose addresses have lower dispersion.
2) Golden ratio (1.618)
In mathematics, two quantities are in the golden ratio if their ratio is the same as the ratio of their sum to the larger of the two quantities. The figure on the right illustrates the geometric relationship. Expressed algebraically, for quantities a and b with a > b > 0,
(a+b/a = a/b)

Output:
Enter no of elements in sequence: 15
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
'''
#Function to return nth term in fibonacci series:
def fibonacci(num):
	if num == 0:
		return 0;
	elif num == 1:
		return 1;
	else:
		return fibonacci(num -1) + fibonacci(num -2)

count = input('Enter no of elements in sequence: ')

for i in range(0, count):
	print fibonacci(i),

