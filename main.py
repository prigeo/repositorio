'''
O programa deverá exibir os dados da pessoa no console.
Obs: o usuário deverá informar os dados da pessoa.
'''

# dicionário
pessoa = {
    'Nome':(input('Qual seu nome? ')),
    'cpf':input('Qual seu CPF? '),
    'data_nascimento':input('Qual a data do seu nascimento? '),
    'genero':input('Qual seu gênero? '),
    'email':input('Qual seu email? '),
    'telefone':input('Qual seu telefone? '),
    'sanguineo':input('Qual seu tipo sanguineo? '),
    'profissao':input('Qual a sua profissão? '),
    'empresa':input('Onde você trabalha? '),
}

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')

for chave in pessoa:
    print(f'{chave}: {pessoa.get(type)}')