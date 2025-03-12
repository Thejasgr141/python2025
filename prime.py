def thejas(num):
    if num <= 2:
      return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True 
number = int(input("Enter a number: "))
if thejas(number):
   print("The number is prime.")
else:
   print("The number is not prime.")
