# using + operator
x = 15
y = 10
z = x + y

print(z)

#using user Input, It will give in String format and and we need to convert into int
userinput1 = input("Enter 1st no: ")
userinput2 = input("Enter 2nd no: ")
print("The Sum of no is:" , int(userinput1) + int(userinput2))

#using Function
def sum(a , b):
    first = a
    second = b
    return a+b
    
print("sum is:" , sum(10, 20))

# using . format
def add(x, y):
    return x + y

num1 = 10
num2 = 40

sumOfTwoNos = add(num1, num2)

print("sum of {0} and {1} is {2};" .format(num1, num2,sumOfTwoNos))

# using user input with .format
num1
num2

# Using .add() method(import operator)
num1 = 5
num2 = 3

import operator
sum = operator.add(num1, num2)
print("sum is:", sum)

# lambda Function expression

add_nos = lambda x, y: x+y

n1 = 2
n2 = 2

sum = add_nos(n1,n2)
print("Addition is:" , sum)





    
