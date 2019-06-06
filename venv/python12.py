# bitwise operator

a = 8    # 1 0 0 0
b = 12   # 1 1 0 0
c = a & b     # 1 0 0 0
d = a | b     # 1 1 0 0
e = a ^ b     # 0 1 0 0

print(c)
print(d)
print(e)

"""
x = 12
y = 3
# right shift operation
# z = x >> y # 1 1 0 0 >> -> 0 0 0 1
z = x << y   # 1 1 0 0 << -> 1 1 0 0 0 0 0
print(z)
"""

x = -11   # 1 0 1 1
y = 2     # _ _ 1 0
z = x >> y
print("z is:",z)





