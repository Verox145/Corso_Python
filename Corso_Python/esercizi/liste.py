 #lista=sequenza di valori chiamati elementi o oggetti.

[10,20,30,40] #lista di quattro interi.
['crunchy frog','ram bladder','lark vomit'] #lista di tre stringhe.
['spam',2.0,5,[10,20]] #lista con una stringa, un float, un intero e un'altra lista.

#una lista dentro un'altra lista si dice annidata.

[] #lista vuota

cheeses = ['Cheddar','Edam','Gouda']
numbers = [42,123]
empty = []
print(cheeses,numbers,empty) #verranno visualizzate le tre liste una dopo l'altra.

cheeses[0] #il numero nelle parentesi specifica l'indice. l'elemento 0 di cheeses è Cheddar.

#le liste sono mutevoli.

numbers = [42,123]
numbers[1] = 5
numbers #la lista visualizzata sarà [42,5] perché le abbiamo detto di sostituire il valore associato all'indice 1 (123) con 5.

#L'operatore in funziona anche con le liste.

cheeses = ['Cheddar','Edam','Gouda']
'Edam' in cheeses #restituirà True perché Edam è nella lista.
'Brie' in cheeses #restituirà False perché Brie non è nella lista.

for cheese in cheeses: #in questo modo attraversiamo la lista.
    print(cheese)

for i in range(len(numbers)): #scorriamo la lista. len restituisce il numero di elementi nella lista.
    numbers[i] = numbers[i] * 2 #sostituiamo a tutti i valori il loro doppio.

for x in []: #un for loop in una lista vuota non funziona.
    print('Non accadrà mai.')

['spam',1,['Brie','Roquefort','Pol le Veq'], [1,2,3]] #la lunghezza di questa lista è 4.

#l'operatore + concatena le liste.

a =[1,2,3]
b = [4,5,6]
c = a + b # c=[1,2,3,4,5,6]

#l'operatore * ripete la liste per il numero di volte scelto.

[0] * 4 # [0,0,0,0]
[1,2,3] * 2 # [1,2,3,1,2,3]

# l'operatore fetta taglia le liste.
# omettendo il primo indice, il taglio parte dall'inizio.
#omettendo il secondo indice, il taglio parte dal primo indice e finisce alla fine.
#omettendo entrambi gli indici, il taglio sarà uguale alla lista iniziale.

t = ['a','b','c','d','e','f']
t[1:3] # ['b','c']
t[:4] # ['a','b','c','d']
t[3:] # ['d','e','f']
t[:] # ['a','b','c','d','e','f']

#usare l'operatore fetta nella parte sinistra ci permette di aggiornare più elementi.

t = ['a','b','c','d','e','f']
t[1:3] = ['x','y'] #['a','x','y','d','e','f']

# metodo append. aggiunge un elemento in fondo alla lista.

t = ['a','b','c']
t.append('d')
t # restituisce ['a','b','c','d']

# metodo extend. prende una lista e applica il metodo append a tutti gli elemnti di quella lista.

t1 = ['a','b','c']
t2 = ['d','e']
t1.extend(t2)
t1 # restituisce ['a','b','c','d','e']

# metodo sort. ordina gli elementi della lista dal più piccolo al più grande.

t = ['d','c','e','b','a']
t.sort()
t # restituisce la lista ordinata ['a','b','c','d','e']

# aggiungere tutti i numeri ad una lista.

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

# ogni volta che gira il ciclo, x prende un elemento dalla lista e si aggiorna la variabile total.
# total += è equivalente a total = total + x

t = [1,2,3]
sum(t) # restituisce la somma degli elementi presenti nella lista, cioè 6.

# un'operazione come questa che combina una sequenza di elementi in una sola value si chiama reduce.

def capitalize_all(t): #prende una lista di stringhe e restituisce una nuova lista che contiene le stringhe maiuscole.
    res = [] # creo una lista vuota.
    for s in t: # per ogni elemento della lista iniziale, faccio la funzione capitalize.
        res.append(s.capitalize()) # infilo gli elementi diventati maiuscoli nella lista vuota.
    return res # restituisce la nuova lista con gli elementi maiuscoli.

# applicare lo stesso metodo su tutti gli elementi di una lista si definisce "mappare".

def only_upper(t):
    res = []
    for s in t:
        if s.isupper(t): # prendi solo gli elementi maiuscoli.
            res.append(s) # aggiungi gli elementi maiuscoli alla lista vuota.
    return res # lista contenente solo le stringhe maiuscole.

# un'operazione come only_upper si chiama filtro perché seleziona solo alcuni elementi secondo un certo criterio.

t = ['a','b','c']
x = t.pop(1) # pop modifica la lista e restituisce l'elemento rimosso.
t # restituisce ['a','c']
x # restituisce ['b']

t = ['a','b','c']
del t[1] # rimuove definitivamente il valore associato all'indice 1.
t # restituisce ['a','c']

t = ['a','b','c']
t.remove('b') # si usa remove se conosco il valore, ma non il suo indice.
t # restituisce ['a','c']

t = ['a','b','c','d','e','f']
del t[1:5] # usando slice, rimuovo più di un elemento.
t # restituisce ['a','f']

s = 'spam'
t = list(s) # converto la stringa spam in una lista.
t # restituisce ['s','p','a','m']

s = 'pining for the fjords'
t = s.split() # divide la stringa nelle parole che la compone e infila le parole in una lista.
t # restituisce ['pining','for','the','fjords']

# delimiter = specifica quale carattere va usato come separatore delle parole.

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
t # restituisce ['spam','spam','spam']

# join = concatena gli elementi e crea una stringa.

t = ['pining','for','the','fjords']
delimiter = ' '
s = delimiter.join(t)
s # restituisce 'pining for the fjords'

a = 'banana'
b = 'banana'
a is b # restituisce True se si riferiscono alla stessa stringa.

a = [1,2,3]
b = [1,2,3]
a is b # restituisce False perché a e b sono due liste diverse ma con elementi uguali.
# a e b sono due liste equivalenti, ma non identiche.

a = [1,2,3]
b = a
b is a # restituisce True.

# l'associazione di una variabile ad un oggetto si chiama reference.
# un oggetto con più di una reference ha più di un nome, quindi si dice che è aliased.

b[0] = 42
a # restituisce [42,2,3] perché a e b sono la stessa cosa e abbiamo cambiando l'elemento all'indice 0 di b, quindi è mutato anche quello di a.
# aliasing non si presenta con oggetti immutabili come le stringhe.

def delete_head(t): # rimuove il primo elemento di una lista.
    del t[0]

letters = ['a','b','c']
delete_head(letters)
letters # restituisce ['b','c']

t1 = [1,2]
t2 = t1.append(3)
t1 # restituisce [1,2,3]
t2 # restituisce None perché il valore di restituizione di append è None.

t3 = t1 + [4]
t3 # restituisce [1,2,3,4]
t1 # restituisce [1,2,3]

def tail(t): # restituisce tutti gli elementi di una lista tranne il primo.
    return t[1:]

letters = ['a','b','c']
rest = tail(letters)
rest # restituisce ['b','c']

