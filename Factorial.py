import math

x = 5
print(math.factorial(x))

# using User input with while
fact = 1
n = int(input("Enter the no: "))
while(n>0):
    fact = fact * n
    n = n-1
print(fact)

# Using for loop
def factorial(n):
    fact = 1

    if(n<0):
        print("Factorial does not exist")
        return 0
       # quit() and exit() fun are not work in this ide
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
          fact *= i
        return fact
num = 5
print("The factorial of " , num ," is: ", factorial(num))

#Using Recursive approach
def factorial(n):

#return 1 if (n==1 or n==0) else n * factorial(n - 1) 
    if(n == 1 or n == 0):
     return 1
    else:
        return n * factorial(n-1)
    
num = 4
print("factorial of number ", num, "is ", factorial(num))

#Iterative approach
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# Driver Code
num = 10
print("Factorial of",num,"is", factorial(num))

#Using One line Solution (Using Ternary operator)
def factor(n):
    
        return 1 if (n == 0 or n == 1) else n * factor(n-1)
num = 1
print("Factorial of",num,"is", factorial(num))    

        


