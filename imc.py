nome = input("Qua seu nome? ")
idade = input("Informe sua idade: ")
peso = int(input("Quantos Kg pesa? "))
altura = float(input("Sua altura? "))

imc = peso / altura ** 2

import time
import sys
print("Gerando Dados:")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

print(F'Seu nome e {nome}, tem {idade} anos e {altura} de altura.')
print(F'Seu resultado do seu IMC foi de {imc:.2F}')
