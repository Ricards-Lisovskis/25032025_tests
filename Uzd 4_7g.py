from random import*
from math import*
Vid=0
n=[]
lielvid=[]
for i in range (15):
    n.append(randint(-200, 200))
print(n)
Vid = sum(n)/len(n)
print(Vid)
for i in range (15):
    if (n[i])>Vid:
        lielvid.append(n[i])
print(lielvid)
maz=min(lielvid)
print("Mazakais skaitlis, kas lielaks par videjo ir ", maz)