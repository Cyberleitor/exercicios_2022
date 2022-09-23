#!/usr/bin/psql

insert into mesas (mesa_codigo,
		mesa_situacao,
		data_criacao,
		data_atualizacao)
	values ('00001',
		'A',
		'1/1/2016',
		'1/1/2016'
		);

insert into mesas (mesa_codigo,
                mesa_situacao,
                data_criacao,
                data_atualizacao)
        values ('00002',
                'A',
                '1/1/2016',
                '1/1/2016'
		);

insert into funcionarios (funcionario_codigo,
		funcionario_nome,
		funcionario_situacao,
		funcionario_comissao,
		funcionario_cargo,
		data_criacao)
	values ('00001',
		'VINICIUS CARVALHO',
		'A',
		'5',
		'GERENTE',
		'1/1/2016'
		);

insert into funcionarios (funcionario_codigo,
                funcionario_nome,
                funcionario_situacao,
                funcionario_comissao,
		funcionario_cargo,
                data_criacao)
        values ('00001',
		'SOUZA',
                'A',
                '5',
                'GERENTE',
                '1/1/2016'
                );

insert into produtos (produto_codigo,
		produto_nome,
		produto_valor,
		produto_situacao,
		data_criacao,
		data_atualizacao)
	values ('001',
		'REFRIGERANTE',
		10,
		'A',
		'1/1/2016',
		'1/1/2016'
		);

insert into produtos (produto_codigo,
                produto_nome,
                produto_valor,
                produto_situacao,
                data_criacao,
                data_atualizacao)
        values ('002',
                'AGUA',
                3,
                'A',
                '1/1/2016',
                '1/1/2016'
                );

insert into produtos (produto_codigo,
                produto_nome,
                produto_valor,
                produto_situacao,
                data_criacao,
                data_atualizacao)
        values ('003',
                'PASTEL',
                7,
                'A',
                '1/1/2016',
                '1/1/2016'
                );

insert into vendas (funcionario_id,
		mesa_id,
		venda_codigo,
		venda_valor,
		venda_total,
		venda_desconto,
		venda_situacao,
		data_criacao,
		data_atualizacao)
	values (2,
		1,
		'00001',
		'20',
		'20',
		'0',
		'A',
		'1/1/2016',
		'1/1/2016'
		);

insert into vendas (funcionario_id, 
                mesa_id,
                venda_codigo,
                venda_valor,
                venda_total,
                venda_desconto,
                venda_situacao,
                data_criacao,
                data_atualizacao)
        values (2,
                2,
                '00002',
                '21',
                '21',
                '0',
                'A',
                '1/1/2016',
                '1/1/2016'
                );

insert into itens_vendas (produto_id,
		vendas_id,
		item_valor,
		item_quantidade,
		item_total,
		data_criacao,
		data_atualizacao)
	values (1,
		1,
		10,
		2,
		20,
		'1/1/2016',
		'1/1/2016'
		);

insert into itens_vendas (produto_id,
                vendas_id,
                item_valor,
                item_quantidade,
                item_total,
                data_criacao,
                data_atualizacao)
        values (1,
                2,
                7,
                3,
                21,
                '1/1/2016',
                '1/1/2016'
                );

update produtos set produto_valor = 4
	where id = 2;

update produtos set data_criacao = '31/12/2016';
