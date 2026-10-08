import sqlite3
print("DATABASE CARREGANDO")

def conectar():
    return sqlite3.connect("tarefas.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS tarefas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       titulo TEXT NOT NULL,
                       concluida INTEGER NOT NULL DEFAULT 0
                       )
                   ''')
    conexao.commit()
    conexao.close()
    
    
def adicionar_tarefa(titulo: str):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        "INSERT INTO tarefas (titulo) VALUES (?)",
        (titulo,)
    )
    conexao.commit()
    conexao.close()
    
    
def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        "SELECT id, titulo, concluida FROM tarefas"
    )
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas



def concluir_tarefa(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id,)
    )
    conexao.commit()
    conexao.close()
    
    
    
def buscar_tarefa(id: int):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, titulo, concluida FROM tarefas WHERE id = ?",
        (id,)
    )

    tarefa = cursor.fetchone()

    conexao.close()

    return tarefa

def editar_tarefa(id: int, titulo: str):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE tarefas SET titulo = ? WHERE id = ?",
        (titulo, id)
    )

    conexao.commit()
    conexao.close()
    
def excluir_tarefa(id: int):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()