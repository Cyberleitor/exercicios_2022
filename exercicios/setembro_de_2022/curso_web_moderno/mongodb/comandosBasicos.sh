#!/bin/bash

use matrix
show dbs
db.createCollection('estados')
db.createCollection('Estados')
show collections
db.Estados.drop()
show collections
