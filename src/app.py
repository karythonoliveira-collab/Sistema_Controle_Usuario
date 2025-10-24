from controller import produto_controller, usuario_controller
import pwinput
import os
from services.barra_progresso import barra_progresso
def main(): 
    print('1. Login')
    print('2. Resgistre-se')
    opcao = input('Escolha uma opção: ').strip()

    try:
        opcao = int(opcao)
    except Exception as e:
        print(f'Digite uma opção válida! (Numero inteiro)', str(e))

    match opcao:
        case 1:
            print(f"{'-'*30} Login Usuário! {'-'*30}")
            email = input('Digite seu email: ').strip().lower()
            senha = pwinput.pwinput('Digite sua senha: ', mask='-').strip()
            logado = usuario_controller.usuario_service.login(email, senha)

            if logado:
                while True:
                    os.system('cls')
                    print(f"{'-'*30} Bem vindo ao Sistema! {'-'*30}")
                    print('1. Gerenciamento de Estoque')
                    print('2. Editar Usuario')
                    print('3. Sair')
                    opcao_sistema = input('Digite uma opção: ')

                    try:
                        opcao_sistema = int(opcao_sistema)
                        match opcao_sistema:
                            case 1:
                                produto_controller.gerenciar_produto()

                            case 2:
                                id = usuario_controller.usuario_service.listar_usuario_email(email)
                                usuario_controller.gerenciar_usuario(id)

                            case 3:
                                barra_progresso()
                                break

                    except Exception as e:
                        print('A opção não e um numero inteiro!')

                    
        case 2:
            print(f"{'-'*30} Cadastro de Usuário! {'-'*30}")
            nome = input('Digite seu nome: ').strip().title()
            email = input('Digite seu email: ').strip().lower()
            senha = pwinput.pwinput('Digite sua senha: ').strip()

            usuario_controller.usuario_service.criar_usuario(nome, email, senha)

    
if __name__ == '__main__':
    from services.produto_service import criar_tabela
    from services.usuario_service import criar_tabela_usuario
    criar_tabela_usuario()
    criar_tabela()
    main()