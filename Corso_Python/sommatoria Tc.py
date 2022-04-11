def prodotto(ri,ti):
    return ri*ti

p=[] #lista pioggia stazione media
t = [] #lista temperatura stazione media

RiTi = [] #prodotto pioggia stazione

for ri in pioggia:
    for ti in temperature:
        RiTi.append(prodotto(ri,ti))
return RiTi

R = mean(p)

Tc = sum(RiTi)/R
return Tc #sommatoria