def partition(low, high, arr):
  pivot = arr[high]
  i = low -1

  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      arr[j], arr[i] = arr[i], arr[j]
  arr[i+1], arr[high] = arr[high], arr[i+1]

  return i+1

def quickSort(low, high, arr):
  if low < high:
    partition_index = partition(low, high, arr)

    quickSort(low, partition_index-1, arr)
    quickSort(partition_index+1, high, arr)

arr = [10, 7, 8, 9, 1, 5]
print(arr)
quickSort(0, len(arr)-1, arr)
print(arr)

arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(arr)
quickSort(0, len(arr)-1, arr)
print(arr)




def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

arr = [10, 80, 30, 90, 40, 50, 70]
print(arr)
mergeSort(arr)
print(arr)