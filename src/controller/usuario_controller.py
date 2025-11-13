from services import usuario_service

def gerenciar_usuario(id):
    print('1. Editar Perfil')
    print('2. Excluir Conta')
    opcao = input('Digite uma opção: ').strip()
    try:
        opcao = int(opcao)
        match opcao:
            case 1:
                usuario = usuario_service.listar_usuario_id(id)
                print(f"{'-'*30} Editar o Usuário {usuario}! {'-'*30}")

                novo_nome = input('Digite o novo nome: ').strip().title()

                usuario_service.editar_usuario(id, novo_nome)

            case 2:
                usuario_service.excluir_usuario(id)

    except Exception as e:
        print('A opção não e um numero inteiro!', str(e))