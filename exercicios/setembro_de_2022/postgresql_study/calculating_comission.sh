#!/usr/bin/psql

create or replace function
	calc_comissao(data_inicial timestamp,
		data_fim timestamp)
	returns void as $$
	declare
		total_comissao real := 0;
		porcent_comissao real := 0;
		reg record;
		cursor_porcent cursor(func_id int) is
			select rt_valor_comissao(func_id);
		begin
			for reg in(
				select vendas.id id,
					funcionario_id,
					venda_total
				from vendas
				where data_criacao >= data_inicial
				and data_criacao <= data_fim
				and venda_situacao = 'A')loop
			open cursor_porcent(reg.funcionario_id);
			fetch cursor_porcent into porcent_comissao;
			close cursor_porcent;

			total_comissao := (reg.venda_total * porcent_comissao)/100;

			insert into comissoes(
				funcionario_id,
				comissao_valor,
				comissao_situacao,
				data_criacao,
				data_atualizacao)
			values(reg.funcionario_id,
				total_comissao,
				'A',
				now(),
				now());
			update vendas set venda_situacao = 'C'
				where id = reg.id;
				total_comissao := 0;
				porcent_comissao := 0;
			end loop;
		end
		$$ language plpgsql;

select calc_comissao('1/1/2016','1/1/2016');
select comissao_valor, data_criacao from comissoes;

