names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]
 
names2[0] = 'Alice'
names3[1] = 'Bob'
print("names1 is",names1)
print("names2 is",names2)
print("names3 is",names3)
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
 
print (sum)
