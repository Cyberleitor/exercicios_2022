#!/bin/bash

use matrix
db.estados.insert({nome: "Acre", sigla: "AC", regiao: "Norte"})
show collections
show dbs
db.estados.save({nome: "Alagoas", sigla: "AL", regiao: "Nordeste", populacao: 3322000})
db.estados.find()
