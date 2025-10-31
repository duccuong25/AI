'''
Definition
- a function call itself
- solve big problem by solving a smaller problem

loop <--> recursion
pros:
- compact code

cons:
- difficult to understand/debug
- limied stack memory

Categories
- tail recursion: a function called at the end of itself
- non-tail recursion:

'''

'''
write a function to calculate the factorial of 
an integer n (n!)
'''

def factorial(n):
    # 0! = 1
    if n==0: return 1 # -> base case
    return n * factorial(n-1) # -> inductive case

'''
write a function to calculate 
the n-th fibonacci number using recursion
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
s[k] = s[k-1] + s[k-2]
'''

def fibo(n):
    if n==1: return 0
    if n==2 or n==3: return 1
    return fibo(n-2) + fibo(n-1)

n = 8
print(f"the {n}-th fibonacci number: {fibo(8)}")

'''
write a function to calculate the x power of n
(x^n) where x is a real number, n is an integer
'''

def power(x, n):
    if n==0: return 1
    if n<0: return 1/power(x,-n)
    return x * power(x, n-1)

'''
write a function to check
whether an integer is palindrome
n = 12321 -> yes
n = 12312 -> no
'''

def isPalin(n):
    string = str(n)
    # def isPalin_(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return isPalin(string[1:-1])
    return False

n = 12312
print(f"{n} is Palindrome? {isPalin(n)}")


