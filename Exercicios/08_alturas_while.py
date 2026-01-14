#%%
# Faça um programa que recebe 4 alturas usando um laço de repetição e realize a soma dessas alturas.


count = 4
soma = 0

while count > 0:
    altura = float(input("Qual é a altura ?"))
    soma += altura
    count -= 1

print("A soma de todas as alturas é:", soma)