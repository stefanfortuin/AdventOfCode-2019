import re

class Grid():
	def __init__(self, paths):
		self.paths = self.split_paths(paths)
		self.grid = []
		self.currentPath = 0
		self.currentPoint = 
		self.regex = re.compile('([R|U|D|L])(\d+)')
		self.generateIntersections()
	
	def split_paths(self, paths):
		return [p.split(',') for p in paths]

	def generateIntersections(self):
		for path in self.paths:
			for instruction in path:

				match = self.regex.match(instruction)
				if (match.group(1) == 'U'):
					self.up(match.group(2))
				if (match.group(1) == 'D'):
					self.down(match.group(2))
				if (match.group(1) == 'R'):
					self.right(match.group(2))
				if (match.group(1) == 'L'):
					self.left(match.group(2))

	def up(self, amount):
		print("up")
		self.grid.append()

	def down(self, amount):
		print("down")

	def right(self, amount):
		print("right")

	def left(self, amount):
		print("left")

paths = []
with open("./input/3.txt") as file:
	for line in file:
		paths.append(line)

grid= Grid(paths)