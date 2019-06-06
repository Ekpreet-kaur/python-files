data = [10,20,30,40]
#length = len(data)
#print(length)

print(len(data))
print(max(data))
print(min(data))

# iterate in list
for i in range(len(data)):
    print(data[i])

# enhanced for loop / for each loop
for elm in data:    # we can write anything instead of elm
    print(elm)

print([x**2 for x in data])

numbers = list(range(1,101,3))
print(numbers)

print([x+4 for x in data])



