# -------swap variable-------

a = 5
b = 7
print('a', a, 'b', b)
temp = a
a = b
b = temp
print('a', a, 'b', b)

# alternative
c = 6
d = 7
print('c', c, 'd', d)
c, d = d, c
print('c', c, 'd', d)

# alternative
m = 3
n = 7
print('m', m, 'n', n)
m = m + n
n = m - n
m = m - n
print('m', m, 'n', n)

# -------detect a leap year-------

year_text = input('Insert your year: ')
year = int(year_text)
print(year % 4 == 0)

if year % 4 == 0:
    print('Your year is a leap year')
else:
    print('your year is not a leap year')

# -------max or min of multiple items-------

bill = int(input('How much money Bill has: '))
jeff = int(input('How much money Jeff has: '))
elon = int(input('How much money Elon has: '))

if bill > jeff and bill > elon:
    print('Bill is Richer', bill)
elif jeff > bill and jeff > elon:
    print('Jeff is Richer', jeff)
else:
    print('Elon is Richer', elon)

# alternative max
richest = max(bill, jeff, elon)
print('Richest person has', richest)

# alternative min
richest = min(bill, jeff, elon)
print('Poorest person has', richest)

# -------find sum or average of a list-------

nums = [47, 49, 51, 31, 35, 39, 37]
sum = 0
for num in nums:
    print('before adding:', sum)
    print(num)
    sum = sum + num
    print('after adding:', sum)

# -------largest or smallest number in list-------
# -------count words in a sentence-------
# -------number of vowels in a sentence-------
# -------sum of all digits in a number-------
# -------reverse a string in multiple ways-------
