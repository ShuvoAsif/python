nums = [43, 45, 55, 47, 59, 57, 77, 73, 79]
smallest = nums[0]
for num in nums:
    print(smallest, num)
    if num < smallest:
        print('condition is true')
        smallest = num
print('smallest number you have', smallest)
