num = 2

def checkNumber(num):

  if num % 2 == 0:
    print("even number")
  else:
    print("odd number")

checkNumber(num)


#Using User Input
def evenOrodd(num):
  if num % 2 == 0:
    return "Even no"
  else:
    return "Odd no"

number = int(input("Enter a value: "))
print("The number is ", evenOrodd(number))

#Using user input with Try and Except
def checkEvenorOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def main():
    
    try:
        number = int(input("Enter a number: "))
        result = checkEvenorOdd(number)
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()


# using and operation(Bitwise symbol)
def isEvenOrOdd(num):

  if num & 1 == 0:
     return True
  else:
     return False

number = int(input("Eneter a number: "))

if isEvenOrOdd(number):
    print("The number is even.")
else:
    print("The number is odd.")


# using Lambda Function

def is_Even(num):

  return "Even" if num % 2 == 0 else "odd"
num = 2
print(is_Even(num))
