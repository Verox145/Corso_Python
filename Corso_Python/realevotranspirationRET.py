import math
# calcolo del RET

P =[] #lista che contiene l'average annual pluviometric modulus, ossia i valori di P che leggo dalla regressione lineare delle piogge
L = 300 + 25*Tc + 0.05*Tc^3
def RET(p,L):
    for p in P:
        RET = P/math.sqrt(0.9+(P/L)^2)
    return RET