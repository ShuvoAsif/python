nums = [47, 49, 51, 31, 35, 39, 37]
sum = 0
avg = 0
print('number of items', len(nums))
for num in nums:
    sum = sum + num
    avg = sum / len(nums)
print('avg of all numbers:', avg)
