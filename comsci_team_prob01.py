flinedata=input().split()

numseq=flinedata[0]
for i in range(int(numseq)):
    numitems=int(flinedata[1])
    list_str = input().split()
    l = [int(i) for i in list_str]
    s = 0
    for i in l:
        if (i + 1) in l:
            num = abs(l.index(i)-l.index(i+1))
            s += num
    print(s)
