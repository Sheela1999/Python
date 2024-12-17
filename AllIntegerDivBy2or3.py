 # print all the integers that are not divisible by either 2 or 3

def myInteger(start, end):

   for i in range(start, end + 1):
      if(i % 2 != 0 and i % 3 != 0):
          print(i)

myInteger(1, 10)

print("-------------------------------")

#divisible by 5 and 7 and multiple of 5 and 7

def myFunction(start, end):

    for i in range(start, end + 1):
        if(i % 5 == 0 and i % 7 == 0):
            print(i)
            
myFunction(1, 100)

print("-------------------------------------------")

# Find all the no's in a range divisible by a given number

def divisibleByNumInRange(start, end):
    for i in range(start, end + 1):
        if(i % 8 == 0):
            print(i)

divisibleByNumInRange(1,100)

print("------------------------------------")

#using user input for above question

n = int(input("enter a num: "))
print("The given number id divisible by: ", n)

def divbyNumber(start, end):
   for i in range(start, end + 1):
      if(i % n == 0):
         print(i)

divbyNumber(1,10)

print("--------------------------------------------------")

#python program to find sum of digits of number 

x = int(input("enter a num: "))# x = 50
def myFun(x):    
    sum = 0
    while(x > 0):# 50 > 0
        digit = x % 10 # digit = 50%10 = 0
        sum = sum + digit#0 + 0 = 0
        x //=10 #50//10 = 5, 5>0, 5%10=5, 0+5=5, 5//10=0, false
    return sum # 5
res = myFun(x)
print(res)
        


    
        
