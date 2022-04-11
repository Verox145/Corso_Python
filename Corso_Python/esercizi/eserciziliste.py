# esercizio 10.1
# write a function nest_sum che prende una lista di liste di interi e somma gli elementi di tutte le liste.
def nested_sum(t):
    total = 0
    for annidata in t:
        total += sum(annidata)
    return total

t = [[1,2],[3,4],[5,6]]
print (nested_sum(t))

# esercizio 10.2
# write a function cumsum che prende una lista di numeri e restituisce la somma cumulata.
#restituisce una lista in cui l'iesimo elemento è la cumulata.
def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

t = [1,2,3]
print (cumsum(t))

# esercizio 10.3
# scrivi una funzione middle che crea una lista contenente tutti i numeri in una lista tranne il primo e l'ultimo.
def middle(t):
    return t[1:-1]

t = [1,2,3,4,5,6,7]
print (middle(t))

 # esercizio 10.4
 # scrivi una funzione chop che restituisce una lista privata del primo e dell'ultimo elemento
def chop(t):
    del t[1]
    del t[-1]
    
t = [1,2,3,4,5,6,7]
print (chop(t))

# esercizio 10.5
# scrivi una funzione di nome is_sorted che prende una lista come parametro e restituisce true se è in ordine ascendente, altrimenti false.

def is_sorted(t):
    return t == sorted(t)

t = [1,24,32]
print (is_sorted(t))
# esercizio 10.1
# write a function nest_sum che prende una lista di liste di interi e somma gli elementi di tutte le liste.
def nested_sum(t):
    total = 0
    for annidata in t:
        total += sum(annidata)
    return total

t = [[1,2],[3,4],[5,6]]
print (nested_sum(t))

# esercizio 10.2
# write a function cumsum che prende una lista di numeri e restituisce la somma cumulata.
#restituisce una lista in cui l'iesimo elemento è la cumulata.
def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

t = [1,2,3]
print (cumsum(t))

# esercizio 10.3
# scrivi una funzione middle che crea una lista contenente tutti i numeri in una lista tranne il primo e l'ultimo.
def middle(t):
    return t[1:-1]

t = [1,2,3,4,5,6,7]
print (middle(t))

 # esercizio 10.4
 # scrivi una funzione chop che restituisce una lista privata del primo e dell'ultimo elemento
def chop(t):
    del t[1]
    del t[-1]
    
t = [1,2,3,4,5,6,7]
print (chop(t))

# esercizio 10.5
# scrivi una funzione di nome is_sorted che prende una lista come parametro e restituisce true se è in ordine ascendente, altrimenti false.

def is_sorted(t):
    return t == sorted(t)

t = [1,24,32]
print (is_sorted(t))

# esercizio 10.6
# scrivi una is_anagram che restituisce true se due stringhe sono l'una l'anagramma dell'altra.

def is_anagram(t1,t2):
    return sorted(t1) == sorted(t2)

t1 = ['c','d','a','b','b']
t2 = ['a','b','f','d','b']

print (is_anagram(t1,t2))

    