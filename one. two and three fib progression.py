import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
import math
from matplotlib.animation import FuncAnimation


n,sn,tn,qn = 0,0,0,0
f,sf,tf,qf = [],[],[],[]
s,ss,ts,qs = [],[],[],[]
t,st,tt,qt = [],[],[],[]
r,sr,tr,qr=[],[],[],[]
rds,srds,trds,qrds=[],[],[],[]
a,sa,ta,qa = 0,0,0,0
b,sb,tb,qb = 1,1,1,1
iv,siv,tiv,qiv=0,0,0,0
sv,ssv,tsv,qsv=1,1,1,1

while n <= 500:
    c = b + a
    t.append(c)
    s.append(b)
    f.append(a)
    a = b
    b = c
    n = n + 1
while sn <= 500:
    sc = (2*sb) + sa
    st.append(sc)
    ss.append(sb)
    sf.append(sa)
    sa = sb
    sb = sc
    sn = sn + 1
while tn <= 500:
    tc = (3*tb) + ta
    tt.append(tc)
    ts.append(tb)
    tf.append(ta)
    ta = tb
    tb = tc
    tn = tn + 1
while qn <= 500:
    qc = (4*qb) + qa
    qt.append(qc)
    qs.append(qb)
    qf.append(qa)
    qa = qb
    qb = qc
    qn = qn + 1

n,sn,tn,qn=1,1,1,1
while n<= 500:
    z=s[n]/f[n]
    r.append(z)
    n += 1
while sn<= 500:
    sz=ss[sn]/sf[sn]
    sr.append(sz)
    sn += 1
while tn<= 500:
    tz=ts[tn]/tf[tn]
    tr.append(tz)
    tn += 1
while qn<= 500:
    qz=qs[qn]/qf[qn]
    qr.append(qz)
    qn += 1

n,sn,tn,qn=1,1,1,1
while n<=499:
    rd=r[sv]-r[iv]
    iv+=1
    sv+=1
    n+=1
    rds.append(rd)
while sn<=499:
    srd=sr[ssv]-sr[siv]
    siv+=1
    ssv+=1
    sn+=1
    srds.append(srd)
while tn<=499:
    trd=tr[tsv]-tr[tiv]
    tiv+=1
    tsv+=1
    tn+=1
    trds.append(trd)
while qn<=499:
    qrd=qr[qsv]-qr[qiv]
    qiv+=1
    qsv+=1
    qn+=1
    qrds.append(qrd)

print("\nc values = ",len(t)," 4th c value = ",t[4])
print("c values = ",len(st)," 4th c value = ",st[4])
print("c values = ",len(tt)," 4th c value = ",tt[4])
print("c values = ",len(qt)," 4th c value = ",qt[4])

print("\nNo. of r values = ",len(r)," 2nd r value = ",r[2])
print("No. of r values = ",len(sr)," 2nd r value = ",sr[2])
print("No. of r values = ",len(tr)," 2nd r value = ",tr[2])
print("No. of r values = ",len(qr)," 2nd r value = ",qr[2])

print("\nRd values = ",len(rds)," 2nd rd value = ",rds[1])
print("Rd values = ",len(srds)," 2nd rd value = ",srds[1])
print("Rd values = ",len(trds)," 2nd rd value = ",trds[1])
print("Rd values = ",len(qrds)," 2nd rd value = ",qrds[1])

print("\nLast r value = ",r[-1]," Obs/the value = ",r[-1]/((1+math.sqrt(5))/2))
print("Last r value = ",sr[-1]," Obs/the value = ",sr[-1]/(1+math.sqrt(2)))
print("Last r value = ",tr[-1]," Obs/the value = ",tr[-1]/((3+math.sqrt(13))/2))
print("Last r value = ",qr[-1]," Obs/the value = ",qr[-1]/(2+math.sqrt(5)))


plt.plot(range(len(r)),r,color='r',linestyle='solid')
plt.plot(range(len(sr)),sr,color='b',linestyle='dotted')
plt.plot(range(len(tr)),tr,color='y',linestyle='dashed')
plt.plot(range(len(qr)),qr,color='k',linestyle='dashdot')
plt.title('The One,Two,Three and Four Fib ratio difference comparision')
plt.xlabel('Number of iteration(n)')
plt.ylabel('Fib progression()')
plt.legend(['One fib','Two fib','Three fib','Four Fib'])
plt.grid(True)
plt.show()