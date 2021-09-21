

def factorial(number):
      factorial = 1
    
      if(number<0):
            print("Factorial of negative number is not defined")

      elif(number == 0):
            print("Factorial of 0 is 1")

      else:
            for i in range(1,number+1):
                factorial = factorial * i
            return factorial
    
      



if __name__ == '__main__':
    print("Enter your number")
    number = int(input())

print("The factorial of ",number,"is ",factorial(number))
a = input()
 

    
        
