def trier(n):
    fichier=open(n,'r')
    l=[]
    for ligne in fichier:
        contenu1=ligne.split(',')
        l.extend(contenu1)
    contenu2=sorted(l)
    contenu3=",".join(contenu2)
    fichier.close()
    return contenu3
def somme(prenom):
    somme=0
    for lettre in prenom:
        a=ord(lettre)-64
        if 0<a<27 :
            somme+=a
    return somme
def solve(n):
    some=0
    l=trier(n)
    for i,x in enumerate(l):
        some+=(i+1)*somme(x)
    return some

    
    
    