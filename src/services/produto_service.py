from connection import get_connet

def vender(id_produto, qtd_saida):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        
        cursor.execute('SELECT quantidade FROM TB_PRODUTO WHERE id = ?', (id_produto,))
        qtd = cursor.fetchone()

        if not qtd:
            print('Produto não encontrado')
            return None

        qtd = qtd[0]
        if qtd <= 0:
            print('O produto selecionado não tem no estoque')
            return None

        if qtd < qtd_saida:
            print('Quantidade inserida maior do que a disponível')
            return None

        quantidade_restante = qtd - qtd_saida

        cursor.execute('UPDATE TB_PRODUTO SET quantidade = ? WHERE id = ?', (quantidade_restante, id_produto))
        conn.commit()
        print(f'Venda realizada com sucesso! Restam {quantidade_restante} unidades.')

    except Exception as e:
        print('Erro ao dar baixa no produto!')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def criar_produto(descricao, preco, quantidade):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TB_PRODUTO(descricao, preco, quantidade) VALUES (?, ?, ?)',
                       (descricao, preco, quantidade)
        )
        conn.commit()
        print('Produto cadastrado com sucesso!')

    except Exception as e:
        print(f'Falha ao criar produto: {e}')
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def listar_produto():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT id, descricao, preco, quantidade FROM TB_PRODUTO ORDER BY id')
        produtos = cursor.fetchall()

        if produtos:
            for u in produtos:
                # u = (id, descricao, quantidade, preco)
                print(f'| ID: {u[0]} | Descrição: {u[1]} | Preço: R${u[2]:.2f} | Quantidade: {u[3]:.0f}')
        else:
            print('Nenhum produto encontrado!')

    except Exception as e:
        print(f'Falha ao criar produto: {e}')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def excluir_produto(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM TB_PRODUTO WHERE ID=?
        """, (id,))
        
        conn.commit()

    except Exception as e:
        print(f'Falha ao criar produto: {e}')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def editar_produto(id, novo_preco, nova_quantidade):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("UPDATE TB_PRODUTO SET preco = ?, quantidade = ? WHERE id = ? ", (novo_preco, nova_quantidade, id))
        conn.commit()
        print('Produto editado com sucesso!')

    except Exception as e:
        print(f'Falha ao criar produto: {e}')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def listar_produto_id(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT id, descricao, preco, quantidade FROM TB_PRODUTO WHERE id = ?', (id,))
        produtos = cursor.fetchone()

        if produtos:
            # produtos = (id, descricao, preco, quantidade)
            print(f"{'-'*30} Produto selecionado {'-'*30}")
            print(f'| ID: {produtos[0]} | Descrição: {produtos[1]} | Preço: R${produtos[2]} | Quantidade: {produtos[3]}')
        else:
            print('Nenhum produto encontrado!')

    except Exception as e:
        print(f'Falha ao listar produto: {e}')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def listar_produto_nome(produto):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT id, descricao, preco, quantidade FROM TB_PRODUTO WHERE descricao = ?', (produto,))
        produtos = cursor.fetchall()

        if produtos:
            for u in produtos:
                # u = (id, descricao, preco, quantidade)
                print(f'| ID: {u[0]} | Descrição: {u[1]} | Preço: R${u[2]} | Quantidade: {u[3]}')
        else:
            print('Nenhum produto encontrado!')

    except Exception as e:
        print(f'Falha ao listar produto: {e}')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def criar_tabela():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS TB_PRODUTO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao VARCHAR(50),      
            preco float NOT NULL,
            quantidade INTEGER NOT NULL
            
        );
        ''')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
