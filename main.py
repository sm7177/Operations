f1=open("new.txt","r")
f2=open("updated.txt","w")

counter=f1.readlines()
type(counter)

for i in range(1, len(counter)+1):
    if(i%2==0):
        f2.write(counter[i-1])
    else:
        pass
f1.close()

f2=open("updated.txt","r")
counter1=f2.read()

print(counter1)