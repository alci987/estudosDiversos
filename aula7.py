nome = 'Raul Braga'
idade = 23
peso = 87.3
altura = 1.93
ano_atual = 2021

ano_Nascimento = ano_atual - idade 
seuImc = peso / altura ** 2

print(F'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(F'O imc de {nome} e de {seuImc:.2F}.')
print(F'{nome} nasceu em {ano_Nascimento}.')

