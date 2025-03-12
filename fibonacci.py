def fibonacci(n):
sequence = []
a, b = 0, 1
for _ in range(n):
sequence.append(a)
a, b = b, a + b
return sequence
terms = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fibonacci(terms))
3. Use the `math` Module to Solve a Problem
