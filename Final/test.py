a = '10'
b = '20'
d = (a,b)
e = (a,b)
#tuple(d)
#tuple(e)
f=(10,20)
g=('string','hello')
list=[]
list.append(d)
list.append(e)
list.append(f)
list.append(g)
tuple(list)
print(tuple(list))