nome_cliente = input('Digite seu nome: ')
idade = int(input('Idade: '))
renda = int(input('Qual sua renda? '))
cpf = (input('Informe seu CPF: '))

# Requisitos
idade_menor = 18
renda_minima = 800

# Anime Carregamento
import time
import sys
print("Verificando Dados")
animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

for i in range(len(animation)):
    time.sleep(0.5) #Tempo para carregar
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush

print("\n")

if idade >= idade_menor:
    print(f'Idade Aprovada')
else:
    print(f'Idade recusada, deve ser maior de 18 anos.')

if renda >= renda_minima:
    print(f'Renda Aprovada')

else:
    print(f'Renda Recusada, inferior a R$800,00.')

print()
print(f'Seus dados: ')
print()
print(f'Seu nome é: {nome_cliente}')
print(f'Idade: {idade} anos')
print(f'Renda mensal de: {renda}')
print(f'CPF: {cpf}')
