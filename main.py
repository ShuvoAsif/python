# --------------------
# ------variable------
# --------------------

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
if price < 5000 or storage > 126:
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
