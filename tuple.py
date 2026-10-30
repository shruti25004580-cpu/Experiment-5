t=(10,20,30,40,50)

print("tuple : ",t)
print("first element : ",t[0])
print("last element : ",t[-1])
print("length : ",len(t))
print("count of 20 : ",t.count(20))
print("index of 30 : ",t.index(30))
print("maximum : ",max(t))
print("minimum : ",min(t))
print("sum : ",sum(t))
print("is 40 present? ",40 in t)

#convert to list
l=list(t)
print("converted tuple to list",l)

#convert list back to tuple
t2=tuple(l)
print("list converted to tuple: ",t2)
