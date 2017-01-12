'''img = []
for i in range(10):
    new = []
    for j in range(10):
        new.append(j)
    img.append(new)
for i in img:
    for j in i:
        tmp = i[j]
        
for i in img:
    print("\n")
    for j in i:
        print(i[j],end="\t")'''


def flip(a,b):
    tmp = a; a = b; b = tmp
a = 1
b = 3
flip(a,b)
print(a,b)
