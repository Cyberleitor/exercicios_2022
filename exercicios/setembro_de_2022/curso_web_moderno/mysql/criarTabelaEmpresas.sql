create table if not exists empresas (
	id int unsigned not null auto_increment,
	nome varchar(255) not null,
	cnpj int unsigned,
	primary key (id),
	unique key (cnpj)
);

create table if not exists empresas_unidades (
	empresa_id int unsigned not null,
	cidade_id int unsigned not null,
	sede tinyint(1) not null,
	primary key (empresa_id, cidade_id)
);

alter table empresas modify cnpj varchar(14);

insert into empresas (nome, cnpj)
values
	('Bradesco', 29456871234856),
	('Vale', 69458722366549),
	('Cielo', 66966548213745);

insert into empresas_unidades
	(empresa_id, cidade_id, sede)
values
	(1, 2, 1),
	(2, 5, 0),
	(3, 4, 1),
	(2, 1, 1);
