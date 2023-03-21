# --------------------------------
# ------------function------------
# --------------------------------

def write():
    print("hello")
    print("can you here me")
    print("why don't you pick my phone")


write()

# parameter
# return


def multiply_double(num):
    result = num * 2
    return result


first_bank_amount = multiply_double(15)
second_bank_amount = multiply_double(35)
total = first_bank_amount + second_bank_amount
print('total money i have', total)
