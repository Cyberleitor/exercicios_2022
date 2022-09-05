#!/bin/bash

db.estados.aggregate([
	{ $project: {nome: 1, "cidade.nome": 1, _id: 0} }
])
db.estados.aggregate([
	{ $project: {populacao: {$sum: "cidade.populacao"}, sigla: 1, _id: 0},
	{ $group: {_id: null, populacaoTotal: {$sum: "$populacao" }} },
])
db.estados.aggregate([
	{ $match: {"cidade.nome": "Sorocaba"} },
	{ $unwind: "$cidade"},
	{ $match: {"cidade.nome": "Sorocaba"} },
	{ $project: {_id: "$cidade._id"} }
]).pretty()
