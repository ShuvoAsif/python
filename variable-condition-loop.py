# --------------------------------
# ------------variable------------
# --------------------------------

# number
salary = 1000
age = 19

# string
person = "Tamim"

# boolean
isRich = True

print(salary)
print(person)
print(isRich)

# ------input------

status = input("Are you single?: ")
print("this person is", status)

name = input("What's your name: ")
age = int(input("What's your age: "))

# int to str
age = 45
age = str(age)

# fraction number
salary = float(input("Your salary: "))

print("all inputs are", name, age, salary)

# ----------------------------
# ----------condition---------
# ----------------------------

price = 1500
if price < 1500:
    print("then i will buy it")
else:
    print("i wont buy it")

# and
price1 = 9000
storage = 1024
if price < 5000 and storage > 512:
    print("i will buy it")
else:
    print("i wont buy it")

# or
price1 = 7000
storage = 126
if price < 5000 and storage > 126:
    print("i will buy three")
elif price < 5000 or storage > 126:
    print("i will buy it")
else:
    print("i wont buy it")

# ------------------------------
# --------------list------------
# ------------------------------

grocery = [1000, 3000, 5000, 7000, 9000]
friends = ["tamim", "shakib", "tanvir", "shaon", "tonoy"]
# length
count = len(friends)
print(count)

# get element value by index
friend = friends[3]
print(friend)

# use append to add element in the last
friends.append("robin")
print(friends)

# use remove to delet an element
friends.remove("robin")
print(friends)

# set element value by index
friends[1] = "taskin"
print(friends)

# -----------------------------------------
# -------------------loop------------------
# -----------------------------------------

# for loop
for item in grocery:
    # indentantion
    if item > 3000:
        print(item)


for item in grocery:
    if item > 3000:
        # stop the loop
        break
    print(item)

for item in grocery:
    if item > 5000:
        # use continue to ignore
        # use item < 0 to ignore - number
        continue
    print(item)

# while loop
num = 0

while num < 10:
    num = num + 1
    print(num)

while num <= 50:
    num = num + 1
    if num < 30:
        continue
    print(num)

while num <= 50:
    num = num + 1
    if num > 30:
        break
    print(num)
