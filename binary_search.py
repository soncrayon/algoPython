# given an array of integers and a target, find the index of the target in the array using binary search; if the target does not exist, return -1

def binarySearch(array, target):
    # the idea behind binary search is to start with the entire array, then halve the array each time to form a subarray of either lesser or greater values,
    # so we need to set the initial start and end indexes/bounds for the entire array first
    # to do that we set a start index for the beginning of the array
	start = 0
    # and an end index for the last number in the array
	end = len(array)- 1
    # these indexes create the bounds of the first subarray we'll want to search (the entire original array) and will change at each of the below iterations, based on whether
    # the target is less than or greater than the number at the middle index
    # we'll stop searching once the start is greater than the end because at that point, we're either out of bounds or the size of our subarray is zero (no more integers to check)
	while start <= end:
        # the middle index is calculated by adding the upper bound (end) to the lower bound (start) indexes of our current subarray and dividing by 2 to get the midpoint
		middleIdx = (end + start)//2
        # now we check the value at the mid to see if is equal to the target; if so, return the mid index and we're done
		if array[middleIdx] == target:
			return middleIdx
        # else if the target is less than the value at the mid idx, move the end idx to the mid idx - 1 (the number just before the mid) to isolate a subarray of equal or lesser values
		elif array[middleIdx] > target:
			end = middleIdx - 1
        # or if the target is greater, move the start idx to the mid idx + 1 (the number just after the mid) to isolate a subarray of greater than or equal values
		else:
			start = middleIdx + 1
    # if we get to the end of the while loop without finding the target, return -1 to indicate the searched for value does not have a valid idx in the array 
	return -1