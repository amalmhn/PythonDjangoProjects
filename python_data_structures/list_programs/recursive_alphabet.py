# alp=['A','B','A','B']
#
# for i in alp:
#     for j in alp:
#         if (str(alp[i])==str(alp[j])):
#             print(alp[i])
#
#
#
letters = 'ababa'
found_dict = {}
for i in letters:
    if i in found_dict:
        print(i)
        break
    else:
        found_dict[i]= 1




