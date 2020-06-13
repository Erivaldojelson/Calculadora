sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmmFf':
    sexo = str(input('Dados invalidos.invalidos por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso'.format(sexo))