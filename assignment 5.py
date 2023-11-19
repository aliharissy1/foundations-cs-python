# insertionSort exercise:

# list= ["aA", "b", "BD", "Bc","D"]
#
# def insertion(arr):
#     for i in range(1, len(list)):
#         j = i
#         while list[j-1].lower() > list[j].lower() and j > 0:
#             list[j-1], list[j] = list[j], list[j-1]
#             j -= 1
#
# insertion(list)
# print(list)
#

# -----------------------------------------------------

# mergeSort exercise:

# list= [44, 2, 8, 3, 1, 41, 22, 8]
#
# def mergelist(arr):
#     if len(arr) <= 1:
#         return
#
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     mergelist(left)
#     mergelist(right)
#
#     l_idx = r_idx = k_idx = 0
#
#     while l_idx < len(left) and r_idx < len(right):
#         if left[l_idx] < right[r_idx]:
#             arr[k_idx] = right[r_idx]
#             r_idx += 1
#
#         else:
#             arr[k_idx] = left[l_idx]
#             l_idx += 1
#
#         k_idx += 1
#
#     while l_idx < len(left):
#         arr[k_idx] = left[l_idx]
#         l_idx += 1
#         k_idx += 1
#
#     while r_idx < len(right):
#         arr[k_idx] = right[r_idx]
#         r_idx += 1
#         k_idx += 1
#
#
# mergelist(list)
# print(list)

