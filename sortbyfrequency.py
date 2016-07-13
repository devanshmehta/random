from operator import itemgetter

def sort_by_frequency(arr):
    '''Function to sort an array by frequency
       if the two different numbers have same frequency it sorts 
       by normal order of numbers'''
	freq = {}
	for i in arr:
		if i not in freq:
			freq[i] = 0
		freq[i] += 1
	items = freq.items()
	items = sorted(items, key=itemgetter(0))
	items = sorted(items, key=itemgetter(1), reverse=True)
	return [ item[0] for item in items ]

print sort_by_frequency([1, 2, 1, 5, 4, 6, 1, 4, 7, 9, 4, 10, 4])
