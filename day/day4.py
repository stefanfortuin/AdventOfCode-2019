range_start = 248345
range_end = 746315
from re import finditer

def hasDouble(password):
	for i in range(0,5):
		if(int(password[i]) == int(password[i+1])):
			return True

def hasMultipleDouble(password):
	for match in finditer(r'(\d)\1+', password):
		if len(match.group(0)) == 2:
			return True

	# from internet, interpreted the criteria wrong
	# return any(len(match.group(0)) == 2 for match in finditer(r'(\d)\1+', password))
	
def isIncreasing(password):
	for n in range(0,5):
		if (int(password[n]) > int(password[n+1])):
			return False

	return True


total = 0
first_pass = []
for password in range(range_start, range_end):
	if (hasDouble(str(password)) and isIncreasing(str(password))):
		first_pass.append(password)
		total += 1

print(f"result 1: {total}")

total2 = 0
for password in first_pass:
	if hasMultipleDouble(str(password)):
		total2 += 1

print(f"result 2: {total2}")