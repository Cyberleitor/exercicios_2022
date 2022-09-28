#!/usr/bin/bash

alter table produtos
	disable trigger tri_log_produtos;

insert into produtos (produto_codigo,
		produto_nome,
		produto_valor,
		produto_situacao,
		data_criacao,
		data_atualizacao)
	values ('912',
		'SORVETE',
		6,
		'A',
		'1/1/2016',
		'1/1/2016');

select *
	from logs_produtos;

alter table produtos
	enable trigger tri_log_produtos;

update produtos set produto_valor = 10
	where produto_nome = 'SORVETE';

select *
        from logs_produtos;

