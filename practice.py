text = 'I am a good person'
count = 0
voweles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in text:
    # if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    if char in voweles:
        count = count + 1
print('Your total number of vowels is: ', count)
