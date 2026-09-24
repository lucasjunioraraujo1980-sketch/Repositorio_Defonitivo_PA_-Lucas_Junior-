p = int(input("digite o preço do produto: "))

d = round(p * 15) / 100

m = round(p - d)

print(f"o desconto é de {d}R$ e o preço do produto com o desconto é {m}R$. ")