def is_armstrong_number(num):
  num_str =str(num)
  num_digits = len(num_str)
  armstrong_sum=sum(int(digit)**num_digits for digit in num_str)
  return armstrong_sum==num
num = int(input("Enter the number :"))
if is_armstrong_number(num):
 print(f"{num} is an Armstrong number.")
else:
  print(f"{num} is not an Armstrong number ")
