#!/bin/bash

db.estados.insert({
	nome: "São Paulo",
	sigla: "SP",
	regiao: "Sudeste",
	cidade: [{
		_id: ObjectId(),
		nome: "Campinas",
		area: 795.7,
		prefeito: "Fulano Beltrano",
		populacao: 1081000
		}, {
		_id: ObjectId(),
		nome: "Guarulhos",
		populacao: 13225000
		}, {
		_id: ObjectId(),
		nome: "Sorocaba",
		distanciaCapital: 87,
		populacao: 644919
		}]
	})
