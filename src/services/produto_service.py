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
        if qtd >= 0:
            if qtd > qtd_saida:
                quantidade_restante = qtd - qtd_saida 
            else:
                print('Quantidade inserida maior do que a disponível')
        else:
            print('O produto selecionado não tem no estoque')

        cursor.execute('UPDATE TB_PRODUTO SET qtd = ? WHERE id = ?', (quantidade_restante, id_produto))
        conn.commit()
        print(f'Venda realizada com sucesso! Restam {quantidade_restante} unidades.')

    except Exception as e:
        print('Erro ao dar baixa no produto!')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def criar_produto(descricao, quantidade, preco):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TB_PRODUTO(descricao, quantidade, preco) VALUES (?, ?, ?)',
                       (descricao, quantidade, preco)
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
        cursor.execute('SELECT descricao, quantidade, preco FROM TB_PRODUTO')
        produtos = cursor.fetchall()

        if produtos:
            for u in produtos:
                print(f'| {u}')
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
        produtos = cursor.execute('SELECT descricao, preco, quantidade FROM TB_PRODUTO WHERE id = ?', (id,))
        produtos = cursor.fetchone()

        if produtos:
            print(f'{30*'-'}Lista de produtos!{30*'-'}')
            for u in produtos:
                print(f'| {u}')
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
        produtos = cursor.execute('SELECT descricao, preco, quantidade FROM TB_PRODUTO WHERE descricao = ?', (produto,))
        produtos = cursor.fetchone()

        if produtos:
            for u in produtos:
                print(f'| {u}')
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
        CREATE TABLE TB_PRODUTO(
            ID INTEGER PRIMARY KEY,
            quantidade INTEGER NOT NULL,
            preco FLOAT,
            descricao VARCHAR(50)
        );
        ''')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
