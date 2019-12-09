import re
main_planet = None

class Planet():
	def __init__(self, name):
		self.name = name
		self.children = []
	
	def add(self, planet):
		self.children.append(planet)

	def direct(self):
		if len(self.children) == 1:
			return 1
	
	def indirect(self, from_planet):
		for child in children:
			if child == from_planet:
				return True		

	def children(self):
		return self.children	

i = 0
with open("./input/6_test.txt") as file:
	for line in file:
		match = re.search(r"(.+)\)(.+)", line)

		planet = Planet(match.group(2))
		
		diagram.append(Planet(match.group(2)))

for planet in diagram:
	print(planet.name)



