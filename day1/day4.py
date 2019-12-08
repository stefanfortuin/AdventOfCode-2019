range_start = 248345
range_end = 746315

def hasDouble(password):
	for i in range(0,6):
		if (i+1 > 5):
			return False

		if(int(password[i]) == int(password[i+1])):
			return True

def hasMultipleDouble(password):
	doubles = []
	for i in range(0,6):
		if (i+1 > 5):
			break

		if(int(password[i]) == int(password[i+1])):
			if (len(doubles) > 0 and doubles[int(password[i])] == int(password[i])):
				doubles[int(password[i])][1] += 1
			else:
				doubles.append([int(password[i]), 1])
	
	print(doubles)
	test = all(doubles[i][1] % 2 != 0 for i in doubles)
	print(test)

	return False

def isIncreasing(password):
	for n in range(0,6):
		if ( n == 5):
			return True

		if (int(password[n]) > int(password[n+1])):
			return False
	
	return True

password = 111122
if (hasMultipleDouble(str(password)) and isIncreasing(str(password))):
	print("yes")
else:
	print("no")
# total = 0
# for password in range(range_start, range_end):
# 	if (hasDouble(str(password)) and isIncreasing(str(password))):
# 		total += 1

# print(f"result 1: {total}")

# total2 = 0
# for password in range(range_start, range_end):
# 	if (hasMultipleDouble(str(password)) and isIncreasing(str(password))):
# 		total2 += 1

# print(f"result 2: {total2}")