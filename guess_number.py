MAX_NUM = 1000

def guess_number(x):
	guesses = 0
	low = 1
	high = MAX_NUM

	while low < high:

		guesses += 1
		mid = (low + high) // 2
		if mid == x:
			return guesses
		if x > mid:
			low = mid + 1
		else:
			high = mid - 1
	return guesses + 1

guesses = []
for i in range(1, MAX_NUM + 1):
	guesses.append(guess_number(i))

print("Average")
print(sum(guesses) / MAX_NUM)

print("Max")
print(max(guesses))

# OUTPUT
# Average
# 8
# Max
# 10
