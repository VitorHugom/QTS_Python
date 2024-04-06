import os
import sqlite3

def criar_banco_dados():
    # Obtém o caminho absoluto para o diretório raiz do programa
    diretorio_raiz = f"D:\Vitor\Projetos_Python\QTS_Python"
    caminho_banco_dados = os.path.join(diretorio_raiz, 'qts.db')

    # Conectar-se ao banco de dados (ou criá-lo se não existir)
    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    # Criar tabelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            codigo INTEGER PRIMARY KEY,
            nome_curso TEXT NOT NULL,
            carga_horaria INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disciplinas (
            codigo INTEGER PRIMARY KEY,
            nome_disciplina TEXT NOT NULL,
            carga_horaria INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos_disciplinas (
            curso_codigo INTEGER,
            disciplina_codigo INTEGER,
            FOREIGN KEY(curso_codigo) REFERENCES cursos(codigo),
            FOREIGN KEY(disciplina_codigo) REFERENCES disciplinas(codigo),
            PRIMARY KEY (curso_codigo, disciplina_codigo)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            codigo INTEGER PRIMARY KEY,
            nome_professor TEXT NOT NULL,
            dias_disponiveis TEXT,
            FOREIGN KEY(dias_disponiveis) REFERENCES dias_da_semana(dia_da_semana)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores_disciplinas (
            professor_codigo INTEGER,
            disciplina_codigo INTEGER,
            FOREIGN KEY(professor_codigo) REFERENCES professores(codigo),
            FOREIGN KEY(disciplina_codigo) REFERENCES disciplinas(codigo),
            PRIMARY KEY (professor_codigo, disciplina_codigo)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dias_da_semana (
            codigo INTEGER PRIMARY KEY,
            dia_da_semana TEXT NOT NULL,
            status BOOLEAN
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS horarios (
            id INTEGER PRIMARY KEY,
            dia_da_semana_codigo INTEGER,
            horario_inicio TEXT,
            horario_fim TEXT,
            FOREIGN KEY(dia_da_semana_codigo) REFERENCES dias_da_semana(codigo)
        )
    ''')

    # Commit e fechar conexão
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_banco_dados()
    print("Banco de dados do QTS criado com sucesso!")
