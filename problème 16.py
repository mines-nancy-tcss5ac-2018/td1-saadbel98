def solve(n):
    liste_des_chiffres=list(str(n))
    somme=0
    for x in liste_des_chiffres:
        somme+=int(x)  
    return somme   
assert solve(2**15)==26
print(solve(2**1000))

    
    
        