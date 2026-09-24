nmax = 0
nmin = 9999999


for i in range(5):
    n = int(input("digite um numero: "))
    
    if n > nmax:
        nmax = n
    
    if n < nmin:
        nmin = n
        
print(f"O menor numero foi {nmin} e o maior foi {nmax} ")