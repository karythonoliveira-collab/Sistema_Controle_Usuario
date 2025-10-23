from connection import get_connet
from passlib.hash import pbkdf2_sha256 as sha256

def criar_usuario(nome, email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        senha_crip = sha256.hash(senha)
        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (?, ?, ?)',
                       (nome, email, senha_crip))
        conn.commit()
        print('Usuário cadastrado com sucesso!')
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def listar_usuario():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL FROM TB_USUARIO')
        usuarios = cursor.fetchall()

        if usuarios:
            print(f"{'-'*30} Lista de usuários {'-'*30}")
            for u in usuarios:
                print(f'| Nome: {u[0]} | Email: {u[1]}')
        else:
            print('Nenhum usuário encontrado!')
    except Exception as e:
        print(f'Falha ao listar usuarios: {e}')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def excluir_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TB_USUARIO WHERE ID=?", (id,))
        conn.commit()
        print('Usuário excluído com sucesso!')
    except Exception as e:
        print(f'Falha ao excluir usuario: {e}')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def editar_usuario(id, novo_nome, nova_senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        nova_senha_hash = sha256.hash(nova_senha)
        cursor.execute("UPDATE TB_USUARIO SET nome = ?, senha = ? WHERE id = ? ",
                       (novo_nome, nova_senha_hash, id))
        conn.commit()
        print('Usuário editado com sucesso!')
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def login(email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT senha FROM TB_USUARIO WHERE email = ?', (email,))
        usuario = cursor.fetchone()

        if usuario and sha256.verify(senha, usuario[0]):
            print('Login realizado com sucesso!')
            return True
        else:
            print("Erro ao realizar login! E-mail ou senha inválidos!")
            return False
    except Exception as e:
        print('Erro ao fazer login!', str(e))
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def listar_usuario_email(email):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM TB_USUARIO WHERE email = ?', (email,))
        usuario = cursor.fetchone()
        return usuario[0] if usuario else None
    except Exception as e:
        print(f'Falha ao buscar usuario: {e}')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def nome_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM TB_USUARIO WHERE id = ?', (id,))
        usuario = cursor.fetchone()
        return usuario[0] if usuario else None
    except Exception as e:
        print(f'Falha ao buscar nome de usuario: {e}')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def criar_tabela_usuario():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS TB_USUARIO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
        );
        ''')
        conn.commit()
        print("Tabela criada com sucesso!")
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
