CREATE DATABASE IF NOT EXISTS desafio_db;

USE desafio_db;

CREATE TABLE tb_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    quantidade INT,
    valor DECIMAL(10, 2),
    valor_36_meses DECIMAL(10, 2),
    valor_60_meses DECIMAL(10, 2)
);

