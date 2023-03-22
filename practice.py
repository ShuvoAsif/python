year_text = input('Insert your year: ')
year = int(year_text)
print(year % 4 == 0)

if year % 4 == 0:
    print('Your year is a leap year')
else:
    print('your year is not a leap year')
