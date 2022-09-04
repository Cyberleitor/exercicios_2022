insert into cidades (nome, area, estado_id)
values ('Maceió', 510, (select id from estados where sigla = 'AL'));
insert into prefeitos (nome, cidade_id)
values ('Jane Doe', null);
select * from cidades c inner join prefeitos p on c.id = p.cidade_id;
select * from cidades c left join prefeitos p on c.id = p.cidade_id;
select * from cidades c right join prefeitos p on c.id = p.cidade_id;

select * from cidades c left 
join prefeitos p on c.id = p.cidade_id
union
select * from cidades c right join prefeitos p on c.id = p.cidade_id;
