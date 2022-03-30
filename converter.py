a=[1,2,3,4,4,4,5,6]
b=[]
for i in a:
        if i not in b:
                b.append(i)
        else:
                pass
b.sort()
print(b)
