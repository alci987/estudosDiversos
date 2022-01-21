import getpass
import os 
import smtplib
import time
import sys
from email.message import EmailMessage

# Entrada de dados com E-mail e senha
EMAIL_ADDRESS = input('E-mail: ')
EMAIL_PASSWORD = getpass.getpass('Senha: ') #getpass usando para ocultar senha 

# Criar um e-mail
msg = EmailMessage()
msg['Subject'] = input('Assunto: ')
msg['From'] = EMAIL_ADDRESS
msg['To'] = input('Destinario: ')
msg.set_content(input('Escreva sua mensagem: '))

# Enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
    animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    for i in range(len(animation)):
        time.sleep(0.3) # Tempo de carregamento do anime
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    print('Mensagem Enviada!')
    
