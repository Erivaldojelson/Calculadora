while True:#loop infinto
    n = int(input('Digite um valor para fazer a tabuada dele: '))
    print('\033[35m-' * 150)
    if n < 0:#se for negativo ele para
        break#sinal de parada do loop infinito
    for c in range(1, 13):
        print(f'{n} x {c} = {n * c}')#vai fazer o calculo entre os dois
    print('\033[36m-' * 150)
print('\033[30mPrograma de tabuada terminando')