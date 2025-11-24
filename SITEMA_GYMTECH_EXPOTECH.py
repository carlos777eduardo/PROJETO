import mysql.connector
import time
import os


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="senha do mysql",  
        database="GymTech"
    )


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def aguardar():
    input("\nPRESSIONE ENTER PARA VOLTAR AO MENU...")



def cadastrar_aluno():
    limpar_tela()
    print("=== 🆕 CADASTRO DE NOVO ALUNO ===")
    conn = conectar()
    if not conn: return

    nome = input("Nome Completo: ")
    cpf = input("CPF (xxx.xxx.xxx-xx): ")
    print("Planos disponíveis: Mensal, Trimestral, Anual, Gold")
    plano = input("Escolha o Plano: ")

    cursor = conn.cursor()
    sql = "INSERT INTO alunos (nome, cpf, plano, status) VALUES (%s, %s, %s, 'Ativo')"
    valores = (nome, cpf, plano)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print(f"\n✅ SUCESSO! Aluno {nome} cadastrado com ID {cursor.lastrowid}.")
    except mysql.connector.Error as err:
        print(f"\n❌ Erro ao cadastrar: {err}")
    finally:
        conn.close()
        aguardar()

def listar_alunos():
    limpar_tela()
    print("=== 📋 LISTA GERAL DE ALUNOS ===")
    conn = conectar()
    if not conn: return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    resultados = cursor.fetchall()

   
    print(f"{'ID':<5} | {'NOME':<25} | {'CPF':<15} | {'PLANO':<10} | {'STATUS'}")
    print("-" * 75)

    for aluno in resultados:
        # aluno[0]=id, [1]=nome, [2]=cpf, [3]=plano, [4]=status
        print(f"{aluno[0]:<5} | {aluno[1]:<25} | {aluno[2]:<15} | {aluno[3]:<10} | {aluno[4]}")
    
    print("-" * 75)
    print(f"Total de alunos: {len(resultados)}")
    conn.close()
    aguardar()

def buscar_aluno_por_id():
    limpar_tela()
    print("=== 🔍 BUSCAR ALUNO ===")
    id_aluno = input("Digite o ID do aluno: ")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = %s", (id_aluno,))
    aluno = cursor.fetchone()
    
    if aluno:
        print(f"\n👤 Nome: {aluno[1]}")
        print(f"📄 Plano: {aluno[3]}")
        print(f"🟢 Status: {aluno[4]}")
        
       
        cursor.execute("SELECT descricao FROM treinos WHERE aluno_id = %s", (id_aluno,))
        treinos = cursor.fetchall()
        if treinos:
            print("\n🏋️  Últimos Treinos:")
            for t in treinos:
                print(f"   - {t[0]}")
        else:
            print("\n⚠️ Nenhum treino registrado ainda.")
    else:
        print("\n❌ Aluno não encontrado.")
    
    conn.close()
    aguardar()

def registrar_treino():
    limpar_tela()
    print("=== 💪 REGISTRAR TREINO (CHECK-IN) ===")
    conn = conectar()
    
    id_aluno = input("Digite o ID do aluno que vai treinar: ")
    treino = input("Descrição do treino (Ex: Costas e Bíceps): ")
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT nome FROM alunos WHERE id = %s", (id_aluno,))
    aluno = cursor.fetchone()
    
    if aluno:
        sql = "INSERT INTO treinos (aluno_id, descricao) VALUES (%s, %s)"
        cursor.execute(sql, (id_aluno, treino))
        conn.commit()
        print(f"\n✅ Treino registrado para {aluno[0]}!")
    else:
        print("\n❌ Aluno não encontrado. Verifique o ID.")
        
    conn.close()
    aguardar()


def menu():
    while True:
        limpar_tela()
        print("="*40)
        print("   EXPOTECH===GYMTECH===   ")
        print("="*40)
        print("1. ➕ Cadastrar Novo Aluno")
        print("2. 📋 Exibir Todos os Alunos")
        print("3. 🔍 Buscar Aluno (Dados/Treinos)")
        print("4. 💪 Registrar Treino (Check-in)")
        print("5. ❌ Sair")
        print("-" * 40)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno_por_id()
        elif opcao == '4':
            registrar_treino()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)


if __name__ == "__main__":
    menu()