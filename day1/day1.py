import math

def mass_to_fuel(mass):
	return math.floor(int(mass) / 3) - 2


part_one_total = 0

with open("./input/1.txt") as file:
	for line in file:
		fuel = mass_to_fuel(line)
		part_one_total += fuel

print(f"1: {part_one_total}")

part_two_total = 0
with open("./input/1.txt") as file:
	for line in file:
		module_total = 0

		fuel = mass_to_fuel(line)
		module_total += fuel

		while fuel > 0:
			fuel = mass_to_fuel(fuel)

			if (fuel <= 0):
				break

			module_total += fuel

		part_two_total += module_total

print(f"2: {part_two_total}")
		


