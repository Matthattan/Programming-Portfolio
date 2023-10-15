import time

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
		
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return
    
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        if sorted:
            break

arr = [8, 14, 6, 9, 10]
n = len(arr)


def stopwatch():
	while True:
		try:
			sortingAlgorithm = input("""Sorting Algorithm:
Mergesort
Bubblesort
Insertionsort \n""")
			
			if sortingAlgorithm == "Mergesort":
				startTime = time.time()
				mergeSort(arr, 0, n-1)
				endTime = time.time()
			elif sortingAlgorithm == "Bubblesort":
				startTime = time.time()
				bubbleSort(arr)
				endTime = time.time()
			elif sortingAlgorithm == "Insertionsort":
				startTime = time.time()
				insertionSort(arr)
				endTime = time.time()
			else:
				print("Invalid sorting method")

			return f'{arr} at {endTime-startTime}'
		except:
			print("Invalid Sorting Method")


		

	
startTime = time.time()
mergeSort(arr, 0, n-1)
endTime = time.time()
print(stopwatch())