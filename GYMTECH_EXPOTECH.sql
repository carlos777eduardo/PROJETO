CREATE DATABASE GymTech;
USE GymTech;

CREATE TABLE alunos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    plano VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Ativo'
);


CREATE TABLE treinos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    descricao VARCHAR(255),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

INSERT INTO alunos (nome, cpf, plano) VALUES ('João da Silva', '123.456.789-00', 'Gold');

SELECT * FROM ALUNOS;

SELECT * FROM TREINOS;
