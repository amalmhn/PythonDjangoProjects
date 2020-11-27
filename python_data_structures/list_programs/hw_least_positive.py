# lst=[-2,-1,0,2,3,4] #find least positive missing integer from list 1
#
# #lst[10 11 12 13 14] searching for an element
# #lst [10 9 8 11 12 5 6] find second largest number,
# # ascending and descending order
#
# lst=[-2,-1,0,2,3,4]

lst=[-2,-1,0,2,3,4]
cnt=1

for i in range(0,len(lst)):
    if cnt in lst:
        cnt+=1
        pass
    else:
        print(cnt, 'is the least +ve missing integer')
        break

