studmarks=[4,78,34,37,62,12,24,89,99,32,11,23,45,79,1,22,56,82,76,20]
terriblemarks=[]
prettymidmarks=[]
verygoodmarks=[]
MiddleMatrix=[]
for i in studmarks:
    if i<=30:
        terriblemarks.append(i)
    elif i<=69 and i>30:
        prettymidmarks.append(i)
    elif i<=100 and i>69:
        verygoodmarks.append(i)

MiddleMatrix.append(terriblemarks)
MiddleMatrix.append(prettymidmarks)
MiddleMatrix.append(verygoodmarks)
print(MiddleMatrix)