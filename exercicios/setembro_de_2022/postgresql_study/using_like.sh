#!/usr/bin/bash
insert into funcionarios(funcionario_codigo,
		funcionario_nome,
		funcionario_situacao,
		funcionario_comissao,
		funcionario_cargo,
		data_criacao)
	values('0100',
		'VINICIUS SOUZA',
		'A',
		2,
		'GARÇOM',
		'1/3/2016');

insert into funcionarios(funcionario_codigo,
                funcionario_nome,
                funcionario_situacao,
                funcionario_comissao,
                funcionario_cargo,
                data_criacao)
        values('0101',
                'VINICIUS SOUZA MOLIN',
                'A',
                2,
                'GARÇOM',
                '1/3/2016');

insert into funcionarios(funcionario_codigo,
                funcionario_nome,
                funcionario_situacao,
                funcionario_comissao,
                funcionario_cargo,
                data_criacao)
        values('0102',
                'VINICIUS RANKEL C',
                'A',
                2,
                'GARÇOM',
                '1/3/2016');

insert into funcionarios(funcionario_codigo,
                funcionario_nome,
                funcionario_situacao,
                funcionario_comissao,
                funcionario_cargo,
                data_criacao)
        values('0103',
                'BATISTA SOUZA LUIZ',
                'A',
                2,
                'GARÇOM',
                '1/3/2016');

insert into funcionarios(funcionario_codigo,
                funcionario_nome,
                funcionario_situacao,
                funcionario_comissao,
                funcionario_cargo,
                data_criacao)
        values('0104',
                'ALBERTO SOUZA CARDOSO',
                'A',
                2,
                'GARÇOM',
                '1/3/2016');

insert into funcionarios(funcionario_codigo,
                funcionario_nome,
                funcionario_situacao,
                funcionario_comissao,
                funcionario_cargo,
                data_criacao)
        values('0105',
                'CARLOS GABRIEL ALMEIDA',
                'A',
                2,
                'GARÇOM',
                '1/3/2016');

insert into funcionarios(funcionario_codigo,
                funcionario_nome,
                funcionario_situacao,
                funcionario_comissao,
                funcionario_cargo,
                data_criacao)
        values('0106',
                'RENAN SIMOES SOUZA',
                'A',
                2,
                'GARÇOM',
                '1/3/2016');

select funcionario_nome from funcionarios;

select funcionario_nome
	from funcionarios
	where funcionario_nome like 'VINICIUS%';

