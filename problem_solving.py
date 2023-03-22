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
