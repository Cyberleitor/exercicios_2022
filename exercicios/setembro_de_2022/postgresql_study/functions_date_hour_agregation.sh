#!/usr/bin/bash

# Another script writed while I read PostgreSQL: banco de dados para aplicações web modernas, by Vinicius Carvalho.

show datestyle;
alter database postgres set datestyle to iso, dmy; # making the change without login in database
set datestyle to iso, dmy; # making the change with login in database

select age(timestamp '15/7/1972');
select age(timestamp '8/6/1982',
	timestamp '25/9/2022');

select date_part('day', timestamp '4/11/1988 8:12:49');
select date_part('month', timestamp '4/11/1988 8:12:49');
select date_part('year', timestamp '4/11/1988 8:12:49');
select date_part('hour', timestamp '4/11/1988 8:12:49');
select date_part('minute', timestamp '4/11/1988 8:12:49');
select date_part('second', timestamp '4/11/1988 8:12:49');

select justify_days(interval 'dias days');
select justify_hours(interval 'horas hours');
select justify_interval(interval 'meses mon - horas hours');

select extract(century from timestamp '4/11/1988 12:21:13');
select extract(day from timestamp '4/11/1988 12:21:13');
select extract(decade from timestamp '4/11/1988 12:21:13');
select extract(hour from timestamp '4/11/1988 12:21:13');
select extract(year from timestamp '4/11/1988 12:21:13');
select extract(minute from timestamp '4/11/1988 12:21:13');
select extract(month from timestamp '4/11/1988 12:21:13');
select extract(second from timestamp '4/11/1988 12:21:13');

select extract(year from data_criacao)
	from funcionarios where id = 1;

select count(*)
	from funcionarios;
select sum(venda_total)
	from vendas;
select avg(produto_valor)
	from produtos;
select max(produto_valor), min(produto_valor)
	from produtos;

insert into vendas(id,
	funcionario_id,
	mesa_id,
	venda_codigo,
	venda_valor,
	venda_total,
	venda_desconto,
	venda_situacao,
	data_criacao,
	data_atualizacao)
values(10000,
	1,
	1,
	'10201',
	'51',
	'51',
	'0',
	'A',
	'1/1/2016',
	'1/1/2016');
insert into itens_vendas(produto_id,
	vendas_id,
	item_valor,
	item_quantidade,
	item_total,
	data_criacao,
	data_atualizacao)
values(4,
	10000,
	15,
	2,
	30,
	'1/1/2016',
	'1/1/2016');
insert into itens_vendas(produto_id,
        vendas_id,
        item_valor,
        item_quantidade,
        item_total,
        data_criacao,
        data_atualizacao)
values(3,
        10000,
        7,
        3,
        21,
        '1/1/2016',
        '1/1/2016');

insert into vendas(id,
        funcionario_id,
        mesa_id,
        venda_codigo,
        venda_valor,
        venda_total,
        venda_desconto,
        venda_situacao,
        data_criacao,
        data_atualizacao)
values(10001,
        1,
        1,
        '10201',
        '20',
        '20',
        '0',
        'A',
        '1/1/2016',
        '1/1/2016');

insert into itens_vendas(produto_id,
	vendas_id,
	item_valor,
	item_quantidade,
	item_total,
	data_criacao,
	data_atualizacao)
values(1,
	10001,
	10,
	2,
	20,
	'1/1/2016',
	'1/1/2016');

insert into vendas(id,
        funcionario_id,
        mesa_id,
        venda_codigo,
        venda_valor,
        venda_total,
        venda_desconto,
        venda_situacao,
        data_criacao,
        data_atualizacao)
values(10002,
        1,
        1,
        '10002',
        '45',
        '45',
        '0',
        'A',
        '1/1/2016',
        '1/1/2016');
insert into itens_vendas(produto_id,
	vendas_id,
	item_valor,
	item_quantidade,
	item_total,
	data_criacao,
	data_atualizacao)
values(4,
	10002,
	15,
	3,
	45,
	'1/1/2016',
	'1/1/2016');

select produto_id, sum(item_total)
	from itens_vendas
	group by produto_id;

create or replace function
retorna_nome_produto(prod_id int)
returns text as
$$
declare
nome text;
begin
	select produto_nome
	into nome
	from produtos
	where id = prod_id;
		return nome;
end
$$
language plpgsql;

select retorna_nome_produto(produto_id), sum(item_total)
	from itens_vendas
	group by produto_id;

select retorna_nome_produto(produto_id) PRODUTO,
		sum(item_total) VALOR_TOTAL_PRODUTO
        from itens_vendas
        group by produto_id
	order by valor_total_produto, produto;

select retorna_nome_produto(produto_id) PRODUTO,
                sum(item_total) VALOR_TOTAL_PRODUTO
        from itens_vendas
        group by produto_id
        order by valor_total_produto desc, produto;

select retorna_nome_produto(produto_id),
	count(id) QUANTIDADE
	from itens_vendas
	group by produto_id;

select retorna_nome_produto(produto_id) PRODUTO,
		count(id) QUANTIDADE
	from itens_vendas
	group by produto_id
	having count(produto_id) >= 2
	order by QUANTIDADE;select retorna_nome_produto(produto_id) PRODUTO,
                count(id) QUANTIDADE
        from itens_vendas
        group by produto_id
        having count(produto_id) >= 2
        order by QUANTIDADE;

select retorna_nome_produto(produto_id) PRODUTO,
		count(id) QUANTIDADE
	from itens_vendas
	group by produto_id
	having count(produto_id) >= 2
	order by QUANTIDADE;


