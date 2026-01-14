#%%
# Faça um programa que recebe 4 alturas usando um laço de repetição e realize a soma dessas alturas.

soma_altura = 0
qtd_entradas = 4
for i in range(qtd_entradas):
    altura = float(input("Entre com uma altura:"))
    soma_altura += altura
print("A somas das alturas é:", soma_altura)