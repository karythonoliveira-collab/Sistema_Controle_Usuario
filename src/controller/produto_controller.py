from services import produto_service
import os
def gerenciar_produto():
    while True:
        
        print(f"{'-'*30} Gerenciamento de estoque! {'-'*30}")
        print('1. Cadastrar Produto')
        print('2. Editar Produto')
        print('3. Lista de Produtos')
        print('4. Buscar Produto')
        print('5. Excluir Produto')
        print('6. Realizar uma Venda')
        print('7. Voltar')
        opcao = input("Digite uma opção: ").strip()

        try:
            opcao = int(opcao)
        except Exception as e:
            print('A opção não é um número inteiro!', str(e))
            continue

        match opcao:
            case 1:
                try:
                    os.system('cls')
                    print(f"{'-'*30} Novo Produto! {'-'*30}")
                    descricao = input('Digite o nome do produto: ').strip().title()
                    preco = input('Digite o preco do produto: ').strip().replace(',', '.')
                    quantidade = input('Digite a quantidade: ').strip()

                    preco = float(preco)
                    quantidade = int(quantidade)
                    # ordem correta: descricao, quantidade, preco (conforme serviço)
                    produto_service.criar_produto(descricao, preco, quantidade)
                except Exception as e:
                    print('Erro ao cadastrar produto!', str(e))

            case 2:
                try:
                    # não limpar a tela aqui para permitir ver a lista
                    print(f"{'-'*30} Lista de produtos! {'-'*30}")
                    produto_service.listar_produto()
                    id_prod = input('Digite o ID do produto que deseja editar: ').strip()
                    try:
                        id_prod = int(id_prod)
                    except Exception:
                        print('O ID é um número inteiro!')
                        continue
                    # mostrar produto selecionado antes de editar
                    produto_service.listar_produto_id(id_prod)
                    print(f"{'-'*30} Editar Produto! {'-'*30}")

                    novo_preco = input('Digite o preco do produto: ').strip().replace(',', '.')
                    nova_quantidade = input('Digite a quantidade: ').strip()

                    novo_preco = float(novo_preco)
                    nova_quantidade = int(nova_quantidade)
                    produto_service.editar_produto(id_prod, novo_preco, nova_quantidade)

                except Exception as e:
                    print('Erro ao editar produto!', str(e))

            case 3:
                # listar sem limpar para facilitar visualização
                os.system('cls')
                print(f"{'-'*30} Lista de produtos! {'-'*30}")
                produto_service.listar_produto()


            case 4:
                os.system('cls')
                print(f"{'-'*30} Buscar Produto! {'-'*30}")
                produto = input('Digite o nome do produto que deseja pesquisar: ').strip().title()
                print(f"{'-'*30} Lista de produtos com esse nome! {'-'*30}")
                produto_service.listar_produto_nome(produto)

            case 5:
                os.system('cls')
                print(f"{'-'*30} Lista de produtos! {'-'*30}")
                produto_service.listar_produto()
                id_produto = input('Digite o id do produto que deseja excluir: ').strip()

                try:
                    id_produto = int(id_produto)
                    produto_service.excluir_produto(id_produto)
                except Exception as e:
                    print('O ID precisa ser um numero inteiro!', str(e))

            case 6:
                os.system('cls')
                print(f"{'-'*30} Lista de produtos! {'-'*30}")
                produto_service.listar_produto()

                print(f"{'-'*30} Painel de Venda! {'-'*30}")
                id_produto_venda = input('Digite o ID do produto que deseja vender: ').strip()
                qtd_saida = input('Digite a quantidade de itens vendidos: ').strip()
                try:
                    id_produto_venda = int(id_produto_venda)
                    qtd_saida = int(qtd_saida)
                    produto_service.vender(id_produto_venda, qtd_saida)
                except Exception as e:
                    print('Erro ao realizar uma venda!', str(e))

            case 7:
                break


        