# Given a stream of incoming numbers, find average or mean of the stream at every point.

def stream_average(arr):
	"""Find average or mean of the stream at every point."""
	running_sum = 0
	averages = []
	
	for i, num in enumerate(arr):
		running_sum += num
		averages.append(running_sum / (i + 1))
		
	return averages

# Testing the function with the provided example
test_array = [10, 20, 30, 40, 50]
averages_result = stream_average(test_array)
print(averages_result)