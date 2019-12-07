import operator

def line_to_array(line):
	return [int(n) for n in line.split(',')]

int_code = []
with open("./input/2.txt") as file:
	for line in file:
		int_code = line_to_array(line)


class Intcode():
	def __init__(self, intcode, alarm=False, from_result=None):
		self.intcode = intcode
		self.original_intcode = intcode.copy()
		self.from_result = from_result

		if (alarm):
			self.alarm(12, 2)

		self.current = 0;

	def run(self):
		if(self.from_result == None):
			self.normal()
		else:
			for x in range(100):
				for y in range(100):
					self.find(x,y)
					self.current = 0
					self.reset()
	
	def normal(self):
		op_code = self.next()
		while op_code:

			if (op_code == 1):
				self.calc(self.current + 1, self.current + 2, self.current + 3, operator.add)
			if (op_code == 2):
				self.calc(self.current + 1, self.current + 2, self.current + 3, operator.mul)
			if (op_code == 99):
				self.result()
				break
			
			self.current += 4
			op_code = self.next()
	
	def find(self, pos1, pos2):
		self.alarm(pos1, pos2)

		op_code = self.next()
		while op_code:
			
			if (op_code == 1):
				try:
					self.calc(self.current + 1, self.current + 2, self.current + 3, operator.add)
				except IndexError:
					break
				
			if (op_code == 2):
				try:
					self.calc(self.current + 1, self.current + 2, self.current + 3, operator.mul)
				except IndexError:
					break

			if (op_code == 99):
				if (self.intcode[0] == self.from_result):
					self.find_result()
				break

			
			self.current += 4
			op_code = self.next()


	def next(self):
		next_op_code = self.intcode[self.current]
		return next_op_code

	def result(self):
		return print(f"result: {self.intcode[0]}")
	
	def find_result(self):
		return print(f"noun: {self.intcode[1]}, verb: {self.intcode[2]}, result: {100 * self.intcode[1] + self.intcode[2]}")

	def reset(self):
		self.intcode = self.original_intcode.copy()

	def alarm(self, pos1, pos2):
		self.intcode[1] = pos1
		self.intcode[2] = pos2

	def calc(self, pos1, pos2, pos_result, op):
		
		pos1 = self.intcode[pos1]
		pos2 = self.intcode[pos2]
		pos_result = self.intcode[pos_result]
		result = op(self.intcode[pos1], self.intcode[pos2])
		self.intcode[pos_result] = result

intCode = Intcode(int_code, from_result=19690720)
intCode.run()

	