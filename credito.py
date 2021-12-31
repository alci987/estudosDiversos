print('#####################################')
print('Sistema de Credito T&P')
print('#####################################')

import time

nomeCliente = input('Nome Completo: ')
cpfCliente = input('CPF: ')
rendaCliente = input('Renda Mensal: ')
emailCliente = input('E-mail: ')

rendaCliente = float(rendaCliente)

calculoLimit = (rendaCliente / 100) * 30

while True:
    pergunt = input('Você tem restrição no seu Nome? Use s/n :')
    if pergunt == 'sim' or pergunt == 's' or pergunt == 'yes':
        print('Desculpe, credito não aprovado.')
        exit()
    elif pergunt == 'não' or pergunt == 'n' or pergunt == 'no':
        print('Ótimo, vamos Continuar..')
        break
    else:
        print()
        pass

while True:
    pergunt1 = input('Você trabalha atualmente? Use s/n : ')
    if pergunt1 == 'sim' or pergunt1 == 's' or pergunt1 == 'yes':
        pergunt1 = input('Nome da Empresa: ')
        break
    elif pergunt1 == 'não' or pergunt1 == 'n' or pergunt1 == 'no':
        print()
        break
    else:
        pass

while True:

    print('#####################################')
    print(f'Nome: {nomeCliente}')
    print(f'Cpf: {cpfCliente}')
    print(f'Renda: {rendaCliente}')
    print(f'Empresa onde Trabalha: {pergunt1}')
    print(f'Email: {emailCliente}')
    print('#####################################')
    correto = input('Seus dados estão corretos? Use s/n :')
    if correto == 'sim' or correto == 's' or correto == 'yes':
        print('Ok, enviando informações ')
        time.sleep(0.8)
        break
    elif correto == 'não' or correto == 'n' or correto == 'no':
        print('Vamos começar tudo de novo, então! ')
        exit()

    else:
        pass

print('Credito Aprovado! =) ')
time.sleep(0.6)

print(f'{nomeCliente} o limite aprovado em seu nome de acordo com suas informações é de R${calculoLimit:.2F}')
