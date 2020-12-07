# import operator
f=open('complete.csv')

dict={}
for lines in f:

    data=lines.rstrip('\n').split(',')

    state=data[1]
    confirmed_cases=int(data[4])

    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state] = confirmed_cases


for k,v in dict.items():
    print(k,v)
##############################################################
#highest=max(dict,key=dict.get)
#min=min(dict,key=dict.get)


sorted_list=sorted(dict, key=dict.get)
print(sorted_list)

print("The state which have lowest confirmed cases is ",sorted_list[0])

print("The state which have highest confirmed cases is ",sorted_list[-1])



#working but only printing the key values





# sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
# print(sorted_dict[0][1])
# print(sorted_dict)
# print(len(sorted_dict))
#
# for i in sorted_dict:
#     data=i[1]
#     print(data)




#find state which have highest confirmed cases
#find state which have lowest confirmed cases
#sort the states depend on confirmed cases
#