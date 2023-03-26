text = 'I am a good person'
count = 0
if len(text) > 0:
    count = 1
print(len(text))
for char in text:
    if char == " ":
        count = count + 1
print('Your total number of words is: ', count)
