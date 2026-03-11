# WAP to print all numbers in a range divisible by a given number.

number = int(input('Enter the number: '))
divisor = int(input('Enter the number that will divide all numbers: '))
for i in range(1,number+1):
    if i % divisor == 0:
        print(i)