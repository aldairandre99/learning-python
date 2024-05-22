# Using params

choice = int(input("\n\nWhat number would you like to choose: "))

def fizzBuzz(choice):
 for i in range(1,choice):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else: 
    print(i)
    
fizzBuzz(choice)
  