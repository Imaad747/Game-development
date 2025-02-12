vacantlist=[]
for i in range(5):
 groupname=input("Enter the group name.")
 sizeofgoroup=input("How big is the group.")
 dateoc=input("Enter the date.")
 venue=input("Enter where the group went to.")
 typeofmodel=input("Did you get gold, silver, or worthless bronze?")
 tg=(groupname,sizeofgoroup,dateoc,venue,typeofmodel)
 vacantlist.append(tg)
print(vacantlist)
