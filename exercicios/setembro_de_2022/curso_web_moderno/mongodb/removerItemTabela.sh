#!/bin/bash

db.estados.remove({sigla: "AC"})
db.estados.count()
db.estados.update({sigla: "RJ"}, {$set: {populacao: 167200000}})
db.estados.remove({popularidade: {$lt: 20000000}})
