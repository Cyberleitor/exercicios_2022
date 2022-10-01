#!/usr/bin/bash

sudo -u postgres pg_dump postgres > bancopostgres.bkp
sudo -u postgres psql newbase < bancopostgres.bkp

\copy funcionarios
(
	funcionario_codigo,
	funcionario_nome,
	funcionario_situacao,
	funcionario_comissao,
	funcionario_cargo,
	data_criacao,
	data_atualizacao
)
from '/home/john-nada/Área de Trabalho/the_archives/programming/python/studies/script_essay/hacking/planilha.csv'
delimiter ','
csv header;

select * from funcionarios where funcionario_cargo = 'GARÇOM';

create index idx_cargo
	on funcionarios(funcionario_cargo);

create index idx_codigo
	on funcionarios using hash(funcionario_codigo);

create index concurrently idx_nome on
	funcionarios using btree(funcionario_nome);

create index idx_funcionario_id_codigo on
	funcionarios(id, funcionario_codigo);

create unique index idx_unique_codigo on
	funcionarios (funcionario_codigo);

analyze verbose;
analyze verbose funcionarios;
analyze verbose funcionario(funcionario_cargo);

reindex table funcionarios;

