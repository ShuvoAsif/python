num = int(input("Enter your number:"))
sum = 0
# fraction rounded by //
while num > 0:
    last_digit = num % 10
    print(num, last_digit)
    sum = sum + last_digit
    num = num // 10
print(sum)
