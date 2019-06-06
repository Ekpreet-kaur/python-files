johnsAge = 30
print(johnsAge,hex(id(johnsAge)))

jenniesAge = 30
print(jenniesAge,hex(id(jenniesAge)))

#copy operation: not data copy but reference variable
jacksAge = johnsAge
print(jacksAge,hex(id(jacksAge)))

#del johnsAge
#print(jenniesAge,hex(id(jenniesAge)))

#ps: johnsage and jenniesage are reference variable