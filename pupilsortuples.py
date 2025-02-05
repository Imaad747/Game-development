tupcup=("Flying Dorito",9112,True,"or",False,0,1)
print(type(tupcup))
print(tupcup[2])
for i in tupcup:
    print(i)
tupl=(0,7,919,1970)

#concatenation

print(tupl+tupcup)

#nestedtuple

print(tupl,tupcup)

#tupl slicing

print(tupl[1:3])

#eating a tuple

#del tupl
#print(tupl)

print(len(tupl))
l=[1,2,3,4,5,6,7,8,9,10]
t=tuple(l)
print(t)

#packing and unpacking

address=(711,"Old airport hangar apartments","This used to be a runway","Jeddah",1982)
dno,mautbaa,st,city,zip=address
print(mautbaa)