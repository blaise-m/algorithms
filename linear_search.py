import time


def linear_search(list, target):
	'''
	Takes in a list and a target and
	Returns the index of the target if found
	Else it returns None
	'''	

	for i in range(len(list)):
		if list[i] == target:
			return i	
	
	return None


def verify(result):
	'''
	Takes in an index and prints it out if it's not None
	Else prints target not found
	'''

	if result.get('func_result') is not None:
		print(f"Target found at index: {result.get('func_result')} in: {result.get('time_taken')} seconds")
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
	
	
	verify(time_func(linear_search, numbers, 10000000))