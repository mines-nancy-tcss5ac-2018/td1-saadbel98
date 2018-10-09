def ispalindrome(n):
    liste=list(str(n))
    liste2=list(reversed(liste))
    return liste==liste2
        
def sominv(n):
    liste=list(str(n))
    liste2=reversed(liste)
    chaine="".join(liste2)
    n1=int(chaine)
    return n+n1
def islychrel(n):
    for _ in range(1,51):
        if ispalindrome(sominv(n)): return False
        n=sominv(n)
    return True

            
def solve(n):
    number=0
    for i in range(n+1):
        if islychrel(i):
            number+=1
    return number


    