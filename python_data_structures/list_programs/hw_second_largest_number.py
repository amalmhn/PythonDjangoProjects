# list1 = [10, 20, 4, 45, 99]
#
# max = max(list1[0], list1[1])
# secondmax = min(list1[0], list1[1])
#
# for i in range(2, len(list1)):
#     if list1[i] > max:
#         secondmax = max
#         max = list1[i]
#     else:
#         if list1[i] > secondmax:
#             secondmax = list1[i]
#
# print("Second highest number is : ", str(secondmax))

list1 = [10,9,8,11,12,5,6]


list1.sort()

print("Second largest element is:", list1[-2])