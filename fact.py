def factor(n):
    fact = 1

    if(n<0):
        return 0
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
          fact *= i
        return fact
num = -1
print("The factorial of " , num ," is: ", factor(num))
