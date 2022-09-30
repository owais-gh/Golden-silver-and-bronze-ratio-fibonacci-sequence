import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

x,y,n,a,b = 0,1,0,0,1
f,s,t,r,rds = [],[],[],[],[]

while n <= 500:
    c = b + a
    t.append(c)
    s.append(b)
    f.append(a)
    a = b
    b = c
    n = n + 1

n=1
while n<= 500:
    z=s[n]/f[n]
    r.append(z)
    n += 1

n=1
iv=0
sv=1
while n<=499:
    rd=r[sv]-r[iv]
    iv+=1
    sv+=1
    n+=1
    rds.append(rd)

print("\nNumber of c values="+str(len(t))+" 4th c value="+str(t[4]))
print("Number of ratio values="+str(len(r))+" 2nd ratio value="+str(r[2]))
print("Number of ratio difference values="+str(len(rds))+" 2st ratio difference value="+str(rds[1]))

plt.plot(range(len(r)),r,color='red',linestyle='solid')
plt.title('The Fibonacci ratio difference')
plt.xlabel('Number of iteration(n)')
plt.ylabel('Difference of ratio(rd)')
plt.legend(['rd=r(n+1)-r(n)'])
plt.grid(True)
plt.show()