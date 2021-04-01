def split(list):
	'''
	Divides the provided list at midpoint into two lists
	Returns the two lists - left_half and right_half
	Takes overall O(log n) time

	Note: Since we use slicing in this implementation,
	slicing does not take O(1) time but rather O(k) time
	where k is the size of the slice

	So we would have O(k log n) time.
	To overcome this, we would use an implementation similar to binary search
	instead of using slicing which more expensive
	'''

	mid_point = len(list) // 2
	left_half = list[:mid_point]
	right_half = list[mid_point:]

	return left_half, right_half


def merge(left, right):
	'''
	Merges two lists while sorting them in the process
	Returns a new merged list
	Takes overall O(n) time
	'''

	sorted_list = []
	left_index = 0
	right_index = 0

	while (left_index < len(left)) and (right_index < len(right)):
		if left[left_index] < right[right_index]:
			sorted_list.append(left[left_index])
			left_index += 1
		else:
			sorted_list.append(right[right_index])
			right_index += 1

	while left_index < len(left):
		sorted_list.append(left[left_index])
		left_index += 1

	while right_index < len(right):
		sorted_list.append(right[right_index])
		right_index += 1

	return sorted_list


def merge_sort(list):
	'''
	Sorts a list in ascending order
	Returns a new sorted list

	Divide: Find the midpoint of the list and divide into sublists
	Conquer: Recursively sort the sublists created in prev step
	Combine: Merge the sorted sublists from the prev step

	Takes overall O(n log n)
	'''

	if len(list) <= 1:
		return list

	left_half, right_half = split(list)

	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left, right)


def verify_sorted(list):
	'''
	Takes in a list
	Returns True if the list is sorted else it returns False
	'''

	if len(list) == 0 or len(list) == 1:
		return True

	return list[0] <= list[1] and verify_sorted(list[1:])


if __name__ == "__main__":
	# To be executed if the module is run directly

	alist = [6,3,4,2,5,7,9,6,4,3,2]

	sorted_list = merge_sort(alist)
	print(sorted_list)
	print(f'Is alist sorted? {"Yes" if verify_sorted(alist) else "No"}')
	print(f'Is sorted_list sorted? {"Yes" if verify_sorted(sorted_list) else "No"}')
