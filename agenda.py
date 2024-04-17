import os

lista_de_telefones = [{'nome': 'Roberto', 'sobrenome': 'Costa', 'email': 'roberto@gmail.com', 'numero': '081999995533'},
                         {'nome': 'Maria', 'sobrenome': 'Bela', 'email': 'maria@gmail.com', 'numero': '081999990000'},
                         {'nome': 'Alberto', 'sobrenome': 'Branco', 'email': 'alberto@gmail.com', 'numero': '081999991212'}]

def exibir_nome_do_programa():  

    print("""𝔸𝕘𝕖𝕟𝕕𝕒""")
    print("-------------------------")

def exibir_menu():
    print('1. Cadastrar Telefone')
    print('2. Listar Telefones')
    print('3. Atualizar Telefone')
    print('4. Deletar Telefone')
    print('5. Sair \n')

def opcao_invalida():
    print('Opção Invalida\n')
    input('Tecla qualquer tecla...')
    main()

def voltar_ao_ao_menu_principal():
    input('\nTecle qualquer tecla para continuar...')
    main()

def limpar_a_tela(texto):
    os.system('cls')
    linha = '*' * (len(texto)+4)
    print(linha)
    print(texto)
    print(linha)
    

def cadastrar_telefone():
    limpar_a_tela('Cadastro de Restaurantes')
    nome = input('Informe o nome: ')
    sobrenome = input(f'Informe o sobrenome de {nome}: ')
    email = input(f'Informa o email de  {nome}: ')
    telefone = input(f'Informe o telefone de {nome}: ')
    dados_do_telefone = {'nome':nome, 'sobrenome': sobrenome, 'email':email, 'numero': telefone}
    lista_de_telefones.append(dados_do_telefone)
    print('Cadastro realizado com sucesso !!!!')
    voltar_ao_ao_menu_principal()


def listar_telefones():
    limpar_a_tela('Lista de Telefones')
    print(f'{"Nome":<20} {"Sobrenome":<20} {"Email":<20} {"Telefone"}')
    for agenda in lista_de_telefones:
        nome = agenda['nome']
        sobrenome = agenda['sobrenome']
        email = agenda['email']
        telefone = agenda['numero']
        print(f'{nome:<20} {sobrenome:<20} {email:<20} {telefone}')
    voltar_ao_ao_menu_principal()


def atualizar_telefone():
    limpar_a_tela('Atualizando Telefone')
    nome = input('\nInforme o nome do telefone que você deseja atualizar: ')
    telefone = input(
        '\nInforme o número do telefone que você deseja atualizar: ')
    telefone_encontrado = False
    for agenda in lista_de_telefones:
        if nome == agenda['nome'] and telefone == agenda['numero']:
            nome_alterar = input(f'Altere o nome de {nome}: ')
            numero_alterar = input(f'Altere o telefone de {nome}: ')
            sobrenome = input(f'Informe o sobrenome de {
                              nome} que você deseja atualizar: ')
            email = input(f'Informe o email de {
                          nome} que você deseja atualizar: ')

            agenda['nome'] = nome_alterar
            agenda['numero'] = numero_alterar
            agenda['sobrenome'] = sobrenome
            agenda['email'] = email

            telefone_encontrado = True
            limpar_a_tela(f'O telefone de {
                          nome} foi atualizado com sucesso !!!')
            break
    if not telefone_encontrado:
        limpar_a_tela(f'O Telefone não foi encontrado!')
    voltar_ao_ao_menu_principal()



def deletar_telefone():
    limpar_a_tela('Deletando Telefone')
    nome = input('\nInforme o nome do telefone que você deseja deletar: ')
    telefone = input('\nInforme o número do telefone que você deseja deletar: ')
    telefone_encontrado = False
    for agenda in lista_de_telefones:
        if nome == agenda['nome'] and telefone == agenda['numero']:
           lista_de_telefones.remove(agenda)
           telefone_encontrado = True
           limpar_a_tela(f'O telefone de {nome} foi deletado com sucesso !!!')
           break
    if not telefone_encontrado:
        limpar_a_tela(f'O Telefone não foi encontrado!')
    voltar_ao_ao_menu_principal()


def processar_opcao_escolhida(opcao_escolhida):
    if opcao_escolhida == 1:
        cadastrar_telefone()
    elif opcao_escolhida == 2:
        listar_telefones() 
    elif opcao_escolhida == 3:
        atualizar_telefone()
    elif opcao_escolhida == 4:
        deletar_telefone()
    elif opcao_escolhida == 5: 
        finalizar_app()
    else:
        opcao_invalida()


    

def entrada_de_dados():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'\nVocê escolheu a opção {opcao_escolhida}!! ')
        processar_opcao_escolhida(opcao_escolhida)
    except: 
        opcao_invalida()

def finalizar_app():
    limpar_a_tela('Finalizando o App')
    
 

def main():
    os.system('cls')
    exibir_nome_do_programa()  
    exibir_menu()
    entrada_de_dados()

if __name__ == '__main__':
    main()

