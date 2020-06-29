s0 = int(input())
slist = []
i = 1
slist.append(s0)
while s0 != 1:
	while slist[i-1] != 0:
        slist.insert(i,0)
		slist[i] += (slist[i-1]%10)**2
		slist[i-1] = slist[i-1]//10
	i+=1
print(slist)