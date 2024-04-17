import os
import pymongo


# Conexão com o banco de dados
client = pymongo.MongoClient("localhost", 27017)

# Criar o banco de dados
db = client["Agenda"]



def exibir_nome_do_programa():
    '''
    Esse comando define o nome do app
    '''
    print("""        𝓐𝓰𝓮𝓷𝓭𝓪   """)
    print("-------------------------")


def exibir_menu():
    '''
    Esse comando define o menu de navegacao do app
    '''
    print('1. Cadastrar Telefone')
    print('2. Listar Telefones')
    print('3. Atualizar Telefone')
    print('4. Deletar Telefone')
    print('5. Sair \n')


def opcao_invalida():
    '''
    Esse comando informa que a opção escolhida esta fora do escopo do app
    '''
    print('Opção Invalida\n')
    input('Tecla qualquer tecla...')
    main()


def voltar_ao_ao_menu_principal():
    '''
    Esse comando retorna para o menu do app
    '''
    input('\nTecle qualquer tecla para continuar...')
    main()


def limpar_a_tela(texto):
    '''
    Esse comando limpa a tela e informa a ação que esta sendo executada no app
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)


def cadastrar_telefone():
    '''
    Esse comando ira cadastrar o numero de telefone no app

    Inputs:
        nome, sobrenome, email e número de telefone

    Outputs
        registro dos dados informados no Inputs no banco de dados MongoDB
    '''
    limpar_a_tela('Cadastro de Telefones')
    nome = input('Informe o nome: ')
    sobrenome = input(f'Informe o sobrenome de {nome}: ')
    email = input(f'Informa o email de  {nome}: ')
    telefone = input(f'Informe o telefone de {nome}: ')
    dados_do_telefone = {'nome': nome, 'sobrenome': sobrenome,
                         'email': email, 'numero': telefone}
    
    #comandos de integração do app com o Banco de dados do Mongodb
    colecao = db["contatos"]
    resultado = colecao.insert_one(dados_do_telefone)

    print('Cadastro realizado com sucesso !!!!')
    voltar_ao_ao_menu_principal()


def listar_telefones():
    '''
    Esse comando pegará informação que foi registrada no banco de dados, transformara num dicionário na variável resultados 
    e será percorrida pelo laço for e exibida na tela.

    Outputs:
        nome, sobrenome, email e número de telefone
    '''
    limpar_a_tela('Lista de Telefones')
    print(f'{"Nome":<20} {"Sobrenome":<20} {"Email":<20} {"Telefone"}\n')

    # comandos de integração do app com o Banco de dados do Mongodb
    colecao = db["contatos"]
    resultados = colecao.find({})

    for documento in resultados:
        nome = documento['nome']
        sobrenome = documento['sobrenome']
        email = documento['email']
        telefone = documento['numero']
        print(f'{nome:<20} {sobrenome:<20} {email:<20} {telefone}')
    voltar_ao_ao_menu_principal()


def atualizar_telefone():
    '''
    Esse comando pegará informação que foi registrada no banco de dados, transformara num dicionário na variável resultados 
    e será percorrida pelo laço for e fará atualização do registro no Banco de Dados do MongoDb

    Inputs:
        nome, sobrenome, email e telefone que serão informados pelo usuário

    Outputs:
        nome, sobrenome, email e número de telefone que foram alterados pelo usuário e gravados no Banco de Dados MongoDb
    '''
    limpar_a_tela('Atualizando Telefone')

    # comandos de integração do app com o Banco de dados do Mongodb
    colecao = db["contatos"]
    resultados = colecao.find({})
    nome = input('\nInforme o nome do telefone que você deseja atualizar: ')
    telefone = input('\nInforme o número do telefone que você deseja atualizar: ')
    telefone_encontrado = False
    for agenda in resultados:
        if nome == agenda['nome'] and telefone == agenda['numero']:
            nome_alterar = input(f'Altere o nome de {nome}: ')
            numero_alterar = input(f'Altere o telefone de {nome}: ')
            sobrenome = input(f'Informe o sobrenome de {nome} que você deseja atualizar: ')
            email = input(f'Informe o email de {nome} que você deseja atualizar: ')
            atualizacoes = {"$set": {'nome':nome_alterar, 'sobrenome':sobrenome, 'email':email,'numero':numero_alterar}}

            # sinaliza as chaves que serão alteradas para o Banco de Dados e será incluída no camando de Update
            filtro = {"nome": nome, "numero": telefone}

            # comandos de integração do app com o Banco de dados do Mongodb
            resultados = colecao.update_one(filtro,atualizacoes)
            telefone_encontrado = True

            limpar_a_tela(f'O telefone de {nome} foi atualizado com sucesso !!!')
            break
    if not telefone_encontrado:
        limpar_a_tela(f'O Telefone não foi encontrado!\n')
    voltar_ao_ao_menu_principal()


def deletar_telefone():
    '''
    Esse comando pegará informação que foi registrada no banco de dados, transformara num dicionário na variável resultados 
    e será percorrida pelo laço for para localização do registro que será deletado pelo usuário

    Inputs:
        nome e telefone que serão informados pelo usuário

   
    '''
    limpar_a_tela('Deletando Telefone\n')

    # comandos de integração do app com o Banco de dados do Mongodb
    colecao = db["contatos"]
    resultados = colecao.find({})

    nome = input('\nInforme o nome do telefone que você deseja deletar: ')
    telefone = input('\nInforme o número do telefone que você deseja deletar: ')
    telefone_encontrado = False
    for agenda in resultados:
        if nome == agenda['nome'] and telefone == agenda['numero']:
           
           # sinaliza as chaves que serão alteradas para o Banco de Dados e será incluída no camando de Update
           filtro = {"nome": nome, "numero": telefone}

           # comandos de integração do app com o Banco de dados do Mongodb
           resultados = colecao.delete_one(filtro)

           telefone_encontrado = True
           limpar_a_tela(f'O telefone de {nome} foi deletado com sucesso !!!\n')
           break
    if not telefone_encontrado:
        limpar_a_tela(f'O Telefone não foi encontrado!\n')
    voltar_ao_ao_menu_principal()


def processar_opcao_escolhida(opcao_escolhida):
    '''
    Esse comando receberá qual a opção que o usuário deseja executar

    '''
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
    '''
    Esse comando testará o opção do usuário, caso seja a esperada, dará sequência, senão informara que a opção
    foi fora de escopo e solicitará nova opção até que seja a opção dentro do escopo do app
   
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        processar_opcao_escolhida(opcao_escolhida)
    except:
        opcao_invalida()


def finalizar_app():
    '''
    Esse comando será finalização do uso do app

    '''
    limpar_a_tela('Finalizando o App\n')
    print('\nBQB - Sua solução em Backend agradece vossa consulta !!!\n')
    print('Até a próxima.....\n')

def main():
    '''
    Programa principal
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    entrada_de_dados()

# definição do programa principal será o main()
if __name__ == '__main__':
    main()
