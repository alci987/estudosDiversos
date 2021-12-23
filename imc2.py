"""
Sistema Calculo IMC
Desenvolvido para testar conhecimentos.
"""
import time
import sys


email = input('Email: ')
senha = input('Senha: ')

eMail = 'hallsbraga@outlook.com'
senha1 = 'gtagta59'

idealMin = 18.5
idealMax = 24.99

if email == eMail and senha == senha1:
    print('Verificando Dados')
    print('Aguarde enquanto o sistema está carregando ...')
    animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    for i in range(len(animation)):
        time.sleep(0.3)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    print('Acesso Liberado! ')
    print()

else:
    print('Dados incorretos, tente novamente! ')
    exit()

idade = input('Digite sua idade: ')
if not idade.isnumeric():
    print('Erro, digite sua idade com numeros! ')
    print('Finalizando calculo!...')

else:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    imc = peso / altura ** 2

    print('Realizando Calculo IMC!')
    time.sleep(0.7)
    
    print(f'{nome} tem {idade} anos e {altura} de altura.')
    print(f'{nome} pesa {peso} kg e seu IMC é de {imc:.2F}.')

    if imc < 17:
        print(f'{nome} está muito abaixo do peso.')

    elif imc <= 18.49:
        print(f'{nome} está abaixo do peso.')

    elif imc <= 24.99:
        print(f'{nome} está com peso normal.')

    elif imc <= 29.99:
        print(f'{nome} está acima do peso.')

    elif imc <= 34.99:
        print(f'{nome} está com obesidade grau 1.')

    elif imc <= 39.99:
        print(f'{nome} está com obesidade grau 2.')

    else:
        print(f'{nome} está com obesidade morbida.')

