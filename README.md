🎯 GymTech – Sistema de Gerenciamento de Academia
<p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge"> </p>

Sistema simples e funcional desenvolvido em Python + MySQL para gerenciamento de alunos em academias.
Permite registrar, consultar, listar e acompanhar treinos através de uma interface de terminal simples e intuitiva.

🏋️‍♂️ Funcionalidades

✔ Cadastro de alunos
✔ Listagem completa de todos os alunos
✔ Busca por ID (dados + treinos)
✔ Registro de treinos (check-in)
✔ Armazenamento no MySQL
✔ Interface limpa via terminal

🛠 Tecnologias Utilizadas

Python 3

MySQL / MariaDB

mysql-connector-python

Módulos nativos: os, time

📂 Estrutura do Projeto
GymTech/
│
├── gymtech.py        # Sistema principal
├── banco.sql         # Script de criação do banco e tabelas
└── README.md         # Documentação do projeto

🗃️ Banco de Dados (SQL)
CREATE DATABASE GymTech;
USE GymTech;

CREATE TABLE alunos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    plano VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Ativo'
);

CREATE TABLE treinos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    descricao VARCHAR(255),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

INSERT INTO alunos (nome, cpf, plano)
VALUES ('João da Silva', '123.456.789-00', 'Gold');

▶️ Como Executar
1️⃣ Instalar dependências
pip install mysql-connector-python

2️⃣ Criar o banco de dados

Execute o conteúdo de banco.sql no MySQL Workbench, DBeaver ou phpMyAdmin.

3️⃣ Configurar conexão (somente host/usuário/banco)

No arquivo gymtech.py, configure apenas:

host="localhost",
user="root",
password="SUA_SENHA",
database="GymTech"


🔒 Insira sua senha do MYSQL.

4️⃣ Rodar o sistema
python gymtech.py

📸 Demonstração do Menu
========================================
        EXPOTECH === GYMTECH
========================================
1. ➕ Cadastrar Novo Aluno
2. 📋 Exibir Todos os Alunos
3. 🔍 Buscar Aluno (Dados/Treinos)
4. 💪 Registrar Treino (Check-in)
5. ❌ Sair

🎓 Objetivo Acadêmico

Projeto desenvolvido como parte de demonstração prática de:

Desenvolvimento Python conectado a Banco de Dados

CRUD básico

Organização modular

Interface CLI

Boas práticas de versionamento (Git/GitHub)

👤 Autor

CARLOS EDUARDO MACHADO MARINHO
Projeto apresentado para ADS (ANALISE E DESENVOLVIMENTO DE SISTEMAS)
Instituição UNIFECAF
