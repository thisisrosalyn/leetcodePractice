# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order

# insert from the largest value since inserting to the front will make the array needs to be shifted

# def merge(A, B):
#     indexA = len(A)-1
#     indexB = len(B)-1
#     indexC = len(A) + len(B) - 2

#     while indexA >= 0 and indexB >= 0:
#         if A[indexA] > B[indexB]:
#             A[indexC] = A[indexA]
#             indexA -= 1
#         else:
#             A[indexC] = B[indexB]
#             indexB -= 1
#         indexC -= 1
    
#     while indexA > 0:
#         A[indexC] = A[indexA]
#         indexC -= 1
#         indexA -= 1
    
#     while indexB > 0:
#         A[indexC] = B[indexB]
#         indexC -= 1
#         indexB -= 1
    
#     print(A)

# merge([1, 4, 5, 6, 7, 9, 14], [2, 4 ,5, 6, 8, 12, 17])

# Problem
# indexC give out of range for array A --> need to specify the number of items in array A

def merge(A, B, lastA, lastB):
    indexA = lastA-1
    indexB = lastB-1
    indexC = len(A) - 1
    print(indexC)

    while indexA >= 0 and indexB >= 0:
        print(indexA, indexB, indexC)
        if A[indexA] > B[indexB]:
            A[indexC] = A[indexA]
            indexA -= 1
        else:
            A[indexC] = B[indexB]
            indexB -= 1
        indexC -= 1
        
    
    while indexA >= 0:
        A[indexC] = A[indexA]
        indexC -= 1
        indexA -= 1
    
    while indexB >= 0:
        A[indexC] = B[indexB]
        indexC -= 1
        indexB -= 1
    
    print(A)

# Problem
# No need to copy A because A is already in place.

# def merge(A, B, lastA, lastB):
#     indexA = lastA-1
#     indexB = lastB-1
#     indexC = len(A) - 1
#     print(indexC)

#     while indexB >= 0 and indexC >= 0:
#         print(indexA, indexB, indexC)
#         if A[indexA] > B[indexB]:
#             A[indexC] = A[indexA]
#             indexA -= 1
#         else:
#             A[indexC] = B[indexB]
#             indexB -= 1
#         indexC -= 1
    
#     print(A)

merge([1, 4, 5, 6, 7, 9, 14, None, None, None, None, None, None, None, None], [2, 4 ,5, 6, 8, 11, 12, 17], 7, 8)