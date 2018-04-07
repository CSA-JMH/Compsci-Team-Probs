import math

l = []
num = int(input())
for i in range(1, num + 1):
    if num % i is 0:
        l.append(i)
m = l[math.ceil(len(l) / 2)]
fnum1=int(m)
fnum2=int(num/m)
fsum=fnum1+fnum2
print(fsum)
