from connection import get_connet
from passlib.hash import pbkdf2_sha256 as sha256

def criar_usuario(nome, email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (?, ?, ?)',
                       (nome, email, senha)
        )
        conn.commit()
        print('Usuário cadastrado com sucesso!')

    except Exception as e:
        print(f'Falha ao criar usuario: {e}')


def listar_usuario():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO')
        usuarios = cursor.fetchall()

        if usuarios:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')
            for u in usuarios:
                print(f'| {u}')
        else:
            print('Nenhum usuário encontrado!')

    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

def excluir_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM TB_USUARIO WHERE ID=?
        """, (id,))
        
        conn.commit()


    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

def editar_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

def login(email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()

        senha_hash = sha256.hash(senha)
        usuario_encontrado = cursor.execute('SELECT email, senha FROM TB_USUARIO where email = ? AND senha = ?', (email, senha_hash))
        usuario_encontrado = cursor.fetchone()

        if usuario_encontrado:
            print('Login realizado com sucesso!')
            return True
        else:
            print("Erro ao realizar login! E-mail ou senha inválidos!")
            return False
    except Exception as e:
        print('Erro ao fazer login!', str(e))

    finally:
        conn.close()

def vender(id_produto, qtd_saida):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        
        qtd = cursor.execute('SELECT qtd FROM TB_PRODUTO WHERE id = ?', (id_produto,))
        cursor.fetchone()

        if not qtd:
            print('Produto não encontrado')
            return None

        if qtd > 0:
            if qtd > qtd_saida:
                quantidade_restante = qtd - qtd_saida 
            else:
                print('Quantidade inserida maior do que a disponível')
        else:
            print('O produto selecionado não tem no estoque')

        cursor.execute('UPDATE SET qtd = ? WHERE id = ?', (quantidade_restante, id_produto))
        conn.commit()

    except Exception as e:
        print('Erro ao dar baixa no produto!')

def listar_usuario_id(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

def criar_tabela():
    try:
        conn = get_connet()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE TB_USUARIO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
        );
        ''')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')

if __name__ == '__main__':
    #criar_tabela()
    nome = input('Digite um nome: ').strip().title()
    email = input('Digite um email: ').strip()
    senha = input('Digite uma senha: ').strip()
    senha = sha256.hash(senha)
    print(senha)

    criar_usuario(nome, email, senha)
    listar_usuario()
    excluir_usuario(1) 
    excluir_usuario(2) 
    excluir_usuario(3) 