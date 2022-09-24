#!/usr/bin/bash

insert into produtos (produto_codigo,
	produto_nome,
	produto_valor,
	produto_situacao,
	data_criacao,
	data_atualizacao)
values ('2832',
	'SUCO DE LIMÃO',
	15,
	'C',
	'2/2/2016',
	'2/2/2016');

select * from produtos where produto_situacao = 'A' and produto_situacao = 'C';
select * from produtos where produto_situacao = 'A' or produto_situacao = 'C';
select * from produtos where not produto_nome = 'SUCO DE LIMÃO';
select * from produtos where produto_situacao = 'A' or (produto_situacao = 'C' and data_criacao = '2/2/2016');

select funcionario_codigo ||' '|| funcionario_nome
	from funcionarios
	where id = 1;

select char_length(funcionario_nome)
	from funcionarios
	where id = 2;

select upper('I am a hacker!');

select lower(funcionario_nome)
	from funcionarios;

select overlay(funcionario_nome placing '000000'
		from 3 for 5)
	from funcionarios
	where id = 1;

select substring(funcionario_nome from 3 for 5) from funcionarios where id = 1;

select position('CIUS' in funcionario_nome)
	from funcionarios
	where id = 1;

