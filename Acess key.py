print('\033[36m-' * 150)
senha = str(input('Digite a senha de acesso: '))#Nome que a pessoa tem que digitar
if senha == 'Erivaldo':# Se o nome for diferente de Erivaldo ou outro exibe a mensagem de erro
    from time import sleep #fução para importar a bibílioteca de tempo
    for c in range(1, 1000, 2):#Vezes em que a mensagem será exibida
        sleep(0.2)#Tempo em que o computador precisa dormir até exibir a mensagem
        print('\033[30mSeja bem vindo chefe...')
    print('\033[32mGostei de o ver')
elif senha == 'Jurelma' or 'Bruna' or 'Lito' or 'Emma white':
    from time import sleep
    for c in range(1, 1000, 2):
        sleep(0.2)
        print('\033[31mBela tentativa')
    print('\033[34mNão volte a tentar')

