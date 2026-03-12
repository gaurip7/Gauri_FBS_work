# Write a program to solve the following series :
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter value of n: "))
sum = 0
term = 1
for i in range(1, n + 1):
    sum = sum + term
    term = term * 2
print("Sum of geometric series =", sum)