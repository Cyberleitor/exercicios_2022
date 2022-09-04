insert into cidades (nome, area, estado_id)
values (
	'Campinas',
	795,
	(select id from estados where sigla = 'SP')
), (
	'Niterói',
	133.9,
	(select id from estados where sigla = 'RJ')
), (
	'Caruaru',
	920.6,
	(select id from estados where sigla = 'PE')
), (
	'Juazeiro do Norte',
	248.2,
	(select id from estados where sigla = 'CE')
);
