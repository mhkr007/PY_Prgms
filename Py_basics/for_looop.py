
def m(list):
    v = list[0]
    print("v is ",v)
    for e in list:
      print("ee issssss---",e)
      if v < e:
          v = e
          print("!@@##$$#$%#$%   ---",v)
    return v
 
values = [[3, 4, 5, 1], [33, 6, 1, 2]]
 
for row in values: 
    print(m(row), end = " ")
print("--------------------------------")
arr=[1,2,3]
for a in range(0,4):
    print(a)
