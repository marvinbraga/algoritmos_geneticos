CREATE database produtos-db;
CREATE USER admin@'%' IDENTIFIED BY 'Raposa789';
GRANT ALL PRIVILEGES ON produtos.* TO admin@'%';
FLUSH PRIVILEGES;

\c produtos-db

create table produtos (
  id_produto serial not null,
  nome varchar(50) not null,
  espaco float not null,
  valor float not null,
  quantidade int not null,
  constraint pk_produtos_id_produto primary key (id_produto)
);
