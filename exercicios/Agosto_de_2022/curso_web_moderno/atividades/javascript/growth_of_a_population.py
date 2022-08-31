#!/usr/bin/env python3

def population_growthing(population, growth_per_year, incoming_habitants, max_population):
	time_to_reach_max_population = 0
	while population < max_population:
		population += int(population * growth_per_year / 100) + incoming_habitants
		time_to_reach_max_population += 1
	print(time_to_reach_max_population)

population_growthing(1500, 5, 100, 5000)
population_growthing(1500000, 2.5, 10000, 2000000)
