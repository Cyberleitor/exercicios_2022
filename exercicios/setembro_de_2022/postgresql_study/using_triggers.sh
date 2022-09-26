#!/usr/bin/bash

create table logs_produtos(
	id int not null primary key,
	data_alteracao timestamp,
	alteracao varchar(10),
	id_old int,
	produto_codigo_old varchar(20),
	produto_nome_old varchar(60),
	produto_valor_old real,
	produto_situacao_old varchar(1) default 'A',
	data_criacao_old timestamp,
	data_atualizacao_old timestamp,
	id_new int,
	produto_codigo_new varchar(20),
	produto_nome_new varchar(60),
	produto_valor_new real,
	produto_situacao_new varchar(1) default 'A',
	data_criacao_new timestamp,
	data_atualizacao_new timestamp);

create sequence logs_produto_id_seq;

alter table logs_produtos
	alter column id set default
	nextval('logs_produto_id_seq');

create or replace function gera_log_produtos()
returns trigger as
$$
begin
	if TG_OP = 'INSERT' then
		insert into logs_produtos(
			alteracao,
			data_alteracao,
			id_new,
			produto_codigo_new,
			produto_nome_new,
			produto_valor_new,
			produto_situacao_new,
			data_criacao_new,
			data_atualizacao_new)
		values(
			TG_OP,
			now(),
			new.id,
			new.produto_codigo,
			new.produto_nome,
			new.produto_valor,
			new.produto_situacao,
			new.data_criacao,
			new.data_atualizacao);
		return new;

	elsif TG_OP = 'UPDATE' then
		insert into logs_produtos(
			alteracao,
			data_alteracao,
			id_old,
			produto_codigo_old,
			produto_nome_old,
			produto_valor_old,
			produto_situacao_old,
			data_criacao_old,
			data_atualizacao_old,
			id_new,
			produto_codigo_new,
			produto_nome_new,
			produto_valor_new,
			produto_situacao_new,
			data_criacao_new,
			data_atualizacao_new)
		values(
			TG_OP,
			now(),
			old.id,
			old.produto_codigo,
			old.produto_nome,
			old.produto_valor,
			old.produto_situacao,
			old.data_criacao,
			old.data_atualizacao,
			new.id,
			new.produto_codigo,
			new.produto_nome,
			new.produto_valor,
			new.produto_situacao,
			new.data_criacao,
			new.data_atualizacao);
		return new;

	elsif TG_OP = 'DELETE' then
		insert into logs_produtos(
			alteracao,
			data_alteracao,
			id_old,
			produto_codigo_old,
			produto_nome_old,
			produto_valor_old,
			produto_situacao_old,
			data_criacao_old,
			data_atualizacao_old)
		values(
			TG_OP,
			now(),
			old.id,
			old.produto_codigo,
			old.produto_nome,
			old.produto_valor,
			old.produto_situacao,
			old.data_criacao,
			old.data_atualizacao);
		return new;

	end if;
end;
$$
language plpgsql;

create trigger tri_log_produtos
	after insert or update or delete on produtos
		for each row execute
			procedure gera_log_produtos();

insert into produtos(produto_codigo,
		produto_nome,
		produto_valor,
		produto_situacao,
		data_criacao,
		data_atualizacao)
	values('15121',
		'LAZANHA',
		46,
		'A',
		'1/1/2016',
		'1/1/2016');

insert into produtos(produto_codigo,
		produto_nome,
		produto_valor,
		produto_situacao,
		data_criacao,
		data_atualizacao)
	values('1613',
		'PANQUECA',
		38,
		'A',
		'1/1/2016',
		'1/1/2016');

insert into produtos(produto_codigo,
		produto_nome,
		produto_valor,
		produto_situacao,
		data_criacao,
		data_atualizacao)
	values('733',
		'CHURRASCO',
		72,
		'A',
		'1/1/2016',
		'1/1/2016');

select alteracao,
	data_alteracao,
	id_new,
	produto_codigo_new,
	produto_nome_new,
	produto_valor_new,
	produto_situacao_new,
	data_criacao_new,
	data_atualizacao_new
from logs_produtos;

update produtos set produto_valor = 99
	where produto_nome = 'CHURRASCO';

select * from logs_produtos;

delete from produtos where produto_nome = 'PANQUECA';



