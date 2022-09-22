#!/usr/bin/psql

# In this script I delete one table and recreate her without constraints. I made this with the goal to configure constraints after the creation.

drop table comissoes
create table comissoes (
	id int not null,
	funcionario_id int,
	comissao_valor real,
	comissao_situacao varchar(1) default 'A',
	data_criacao timestamp,
	data_atualizacao timestamp
	);
alter table comissoes
	add constraint comissoes_pkey primary key(id);
alter table comissoes
	add foreign key (funcionario_id) references funcionarios(id);
alter table vendas add check (venda_total > 0);
alter table funcionarios add check (funcionario_nome <> null);
create sequence mesa_id_seq;
create sequence vendas_id_seq;
create sequence itens_vendas_id_seq;
create sequence produtos_id_seq;
create sequence funcionario_id_seq;
create sequence comissoes_id_seq;
alter table mesas
	alter column id set default nextval('mesa_id_seq');
alter table vendas
	alter column id set default nextval('vendas_id_seq');
alter table itens_vendas
	alter column id set default nextval('itens_vendas_id_seq');
alter table produtos
	alter column id set default nextval('produtos_id_seq');
alter table funcionarios
	alter column id set default nextval('funcionario_id_seq');
alter table comissoes
	alter column id set default nextval('comissoes_id_seq');
