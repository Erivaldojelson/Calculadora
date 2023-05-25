from importlib.resources import contents
import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()


with open('chave.key' , 'rb') as key:
    secretkey = key.read()

for file in os.listdir():
    if file == 'madará.py' or file == 'chave.key' or file == 'sensei_master.py':
        continue
    if os.path.isfile(file):
        files.append(file)


for file in files:
    with open (file, 'r') as arquivo:
        conteúdo = arquivo.read()
    conteúdo_decrypted = Fernet(secretkey).decrypt(conteúdo)
    with open(file, 'wb') as arquivo:
        arquivo.write(conteúdo_decrypted)

    