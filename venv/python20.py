technologies = ["ai","android","hadoop","jee"]
technologies[1] = "mobile app" # updation in list
print(technologies)

print()
del technologies[2]
print(technologies)

#print(technologies[0:2])
print(technologies[-1])

data = [1,2,3,4,5,"john","jennie","jim","john","joe"]
data.pop(3)
print(data)

data.remove(3)
print(data)

data.remove("john")
print(data)
