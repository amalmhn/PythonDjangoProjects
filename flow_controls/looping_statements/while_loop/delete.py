lst=[1,2,3,4,6,7]

total=6

for i in lst:
    for j in lst:
        ctotal=i+j
        if ctotal==total:
            print((i,j))