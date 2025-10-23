from services import usuario_service
import pwinput

def gerenciar_usuario(id):
    print('1. Editar Perfil')
    print('2. Excluir Conta')
    opcao = input('Digite uma opção: ').strip()
    try:
        opcao = int(opcao)
        match opcao:
            case 1:
                usuario = usuario_service.nome_usuario(id)
                print(f"{'-'*30} Editar o Usuário {usuario}! {'-'*30}")

                novo_nome = input('Digite o novo nome: ').strip().title()
                nova_senha = pwinput.pwinput('Digite a nova senha: ').strip()

                usuario_service.editar_usuario(id, novo_nome, nova_senha)

            case 2:
                usuario_service.excluir_usuario(id)

    except Exception as e:
        print('A opção não e um numero inteiro!', str(e))