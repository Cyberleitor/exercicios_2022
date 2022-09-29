#!/usr/bin/bash

create user "nome do usuário" superuser; # nesta linha e nas seguintes substituí o real nome de usuário por algo para ocultar a informação (o nick deve ser digitado sem aspas e a senha deve ser delimitada por aspas).
alter user "nome do usuário" password 'senha do usuário';
psql -U "nome do usuário" postgres -h localhost # comando na shell do sistema operacional
create database newbase;
\c newbase "nome do usuário";


