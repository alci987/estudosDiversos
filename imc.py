nome = input("Qua seu nome? ")
idade = input("Informe sua idade: ")
peso = int(input("Quantos Kg pesa? "))
altura = float(input("Sua altura? "))

imc = peso / altura ** 2

print("Gerando Dados, aguarde!")
from time import sleep
sleep(3)   

print(F'Seu nome e {nome}, tem {idade} anos e {altura} de altura.')
print(F'Seu resultado do seu IMC foi de {imc:.2F}')
