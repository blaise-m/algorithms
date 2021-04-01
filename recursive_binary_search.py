import time


def binary_search(list, target):
	'''
	Takes in a list and a target and
	Returns the index of the target if found
	Else it returns None
	'''

	if len(list) == 0:
		return False
	else:
		mid_point = len(list) // 2

		if list[mid_point] == target:
			return True
		elif list[mid_point] > target:
			return binary_search(list[:mid_point], target)
		else:
			return binary_search(list[mid_point+1:], target)


def verify(result):
	'''
	Takes in a boolean and prints it target found if true
	Else prints target not found and the time it takes to run the func
	'''

	if result.get('func_result') is not False:
		print(f"Target found in: {result.get('time_taken')} seconds")
	else:
		print(f"Target not found in: {result.get('time_taken')} seconds")


def time_func(func, *args):
	'''
	Takes in a function with it's arguments
	Runs the function while timing it and
	Returns the result of the function and 
	the time it took to obtain the result
	'''

	start_time = time.time()
	func_result = func(*args)
	end_time = time.time()

	time_taken = end_time - start_time

	return {'func_result': func_result, 'time_taken': time_taken}


if __name__ == "__main__":
	# To be executed if the module is run directly

	numbers = [x for x in range(1,10000000)]
	
	
	verify(time_func(binary_search, numbers, 10000000))
