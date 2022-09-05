#!/bin/bash

db.estados.find({sigla: "RJ"}).pretty()
db.estados.find({$or: [{sigla: "RJ"}, {sigla: "AC"}]}).pretty()
db.estados.find({sigla: "SP"}, {"cidades.nome": 1, _id: 0})
