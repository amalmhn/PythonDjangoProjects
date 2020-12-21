# for row in range(1,5):
#     for col in range(1,(row+1)):
#         print(col,end=" ")
#     print()
#
# -------------------------------


for row in range(1,5): #1
    for col in range(1,8): #1 2
        if row==4 or row+col==5 or col-row==3:
            print("*", end="")
        else:
            print(end=" ") #
    print()