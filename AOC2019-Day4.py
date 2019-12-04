# Advent of Code Day 4

# search range
input_range_start = 372304
input_range_end = 847060


def increasing_digits(split_n):
	# passed in list of digits
	# compare each digit with following digit to if less than
	# return false if number decreases
	for i in range(len(split_n)-1):
		if split_n[i+1]<split_n[i]:
			return False
	return True

def get_count(split_n):
	# passed in list of digits
	# create set with number of occurances for each digit
	# return set of unique values and how many times they appear
	set_n = {}	
	for num in split_n:
		count = split_n.count(num)
		set_n.setdefault(num, count)
	return set_n

def repeated_digits(split_n):
	# passed in list of digits
	# get set of occurences
	# return boolean if contains number of times repeated is more than 2
	set_n = get_count(split_n)
	for key, val in set_n.items():
		if val >= 2:
			return True 
	return False

def has_double(split_n):
	# take in list of digits
	# get set of occurences
	# return boolean is number of times repeated is 2.
	set_n = get_count(split_n)
	for key, val in set_n.items():
		if val == 2:
			return True
	return False


count_partA = 0
count_partB = 0

for n in range(input_range_start,input_range_end+1,1):
	split_n = [int(d) for d in str(n)]
	if repeated_digits(split_n) and increasing_digits(split_n):
		count_partA +=1
		if has_double(split_n):
			count_partB += 1
			print(n)


print("Part A",count_partA)
print("Part B",count_partB)


	

