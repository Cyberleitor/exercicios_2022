#!/bin/bash

db.empresas.aggregate([
	{$match: {nome: "Lalalala"}},
	{$lookup: {
		from: "estados",
		localField: "estadoId",
		foreignField: "_id",
		as: "estado"
	}}
]).pretty()
