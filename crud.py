from db import conectar 

    #----------------------  CRIAR   -----------------------------

def criar_aluno(nome, idade):
    conexao, cursor = conectar()
    if conexao: 
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade) VALUES (%s, %s)",
                (nome, idade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
        finally:
             
            cursor.close()
            conexao.close()

    #----------------------  LISTAR   -----------------------------

def listar_alunos():
    conexao, cursor = conectar()
    if conexao: 
        try:
            cursor.execute(
                "SELECT * FROM alunos ORDER BY id" 
            )
            return cursor.fetchall() #Retorna todas as linhas da tabela
        except Exception as erro:
            print(f"Erro ao listar {erro}")
            return[]
        finally:
             
            cursor.close()
            conexao.close()

   #----------------------  ATUALIZAR  -----------------------------

def atualizar_alunos(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE alunos SET idade = %s WHERE id = %s",
                (nova_idade, id_aluno)
            )
        except Exception as erro:
            print(f"Erro ao atualizar aluno {erro}")
        finally:
            cursor.close()
            conexao.close()

   #----------------------  DELETAR  -----------------------------

def deletar_aluno(id_aluno):
    cursor, conexao = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM alunos WHERE id = %s" ,(id_aluno,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar o aluno {erro}")
        finally:
            cursor.close()
            conexao.close()