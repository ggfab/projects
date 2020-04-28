from random import seed
from random import random

#creazione dell'archivio di dimensione uguale a dimensione (terzo parametro),
# con numeri creati in modo casuale in accordo al seme
# (il seme serve a inizializzare la funzione random)
def creazioneArchivio(archivio,seme,dimensione):
    seed(seme)
    k=random()*1000
    for i in range(dimensione):
        archivio.append(int(k))
        k=random()*1000

#stampa l'archivio, 10 righe alla volta    
def stampaArchivio(archivio):
    print("L'archivio ha " + str(len(archivio)) + " elementi")
    i = int(len(archivio)/10)
    res = int(len(archivio)%10)
    j = 0
    for x in range(i):
        print(archivio[j*10:(j+1)*10])
        j=j+1
        #if res!=0:
         #   print(archivio[j*10:(j+1)*10])

#funzione di test      
def test(archivio,seme,dimensione):
    creazioneArchivio(archivio,seme,dimensione)
    stampaArchivio(archivio)
    archivio=inserimento(archivio,103)
    stampaArchivio(archivio)


#Aggiuntivi
def controllo(archivio):
    ordinato = True
    for i in range(len(archivio)-1):
        if archivio[i]>archivio[i+1]:
            ordinato = False
            break
    #print(ordinato)
    return ordinato

def ordinamento(archivio):
    arcapp=[archivio[0]]
    i=1
    while(i<len(archivio)):
        arcapp=inserimento(arcapp,archivio[i])
        i+=1
    return arcapp

def inserimento(archivio,elemento):
    ordinato=controllo(archivio)
    if(not ordinato):
        archivio=ordinamento(archivio)
    for i in range (len(archivio)+1):
        if(i==len(archivio)):
            archivio.append(elemento)
            break
        if(archivio[i]>elemento):
            archivio.insert(i,elemento)
            break
    return archivio

def ricerca(archivio,elemento):
    for i in range (len(archivio)):
        if(elemento==archivio[i]):
            return True
    return False
    

test([],2,100)