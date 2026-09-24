import random

n = random.randint(1,10)

c = int(input("digite seu chute: "))


while c != n:
        if c > n: 
            print("menor")
        else:
            print("maior")
        c = int(input("tente de novo: "))
    
print("acertou")