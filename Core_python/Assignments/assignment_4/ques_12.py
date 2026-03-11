#  Write a program to check if given number is Armstrong number or not. 
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input('Enter a number: '))
original = num
digits = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10
if sum == original:
    print(original, 'is an Armstrong number')
else:
    print(original, 'is not an Armstrong number')