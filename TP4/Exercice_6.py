lst = [5 ,2 ,4 ,8 ,1 ,3]

for j in range (len(lst)-1):
    ocu = 0
    min = lst[j]
    LePlusPettit = min
    for i in range (len(lst)-j):
        if min > lst[j+i]:
            if LePlusPettit > lst[j+i]:
                LePlusPettit = lst[j+i]
                ocu = j+i
    if min > LePlusPettit:
        lst[j] = lst[ocu]
        lst[ocu] = min
    print (lst)


        




    