# num=int(input('Enter a number'))
#
# sum=0
# rt=1
# while(rt<=num):
#     result=num**rt
#     sum=sum+result
#     rt+=1
#
# print(sum)


number=input("enter a num")

i=1
sum=0
while (i<=int(number)): #1<=3

    data=number*i #"2"*1="2"
    sum=sum+int(data) #0+2=2
    i+=1

print(sum)



















# x=int(input("Enter a number"))
# def digit_sum(x):
#     lst = [str(x)*i for i in range(1,x+1)]
#     print ('+'.join(lst))
#     return sum(map(int, lst))
#
# print (digit_sum(x))


# digit = 4
# n = 3
# # 1, 11, 111
# ones = [ int("1" * i) for i in range(1, n+1)]
# # 4 + 44 + 444 = 4 * (1 + 11 + 111)
# answer = digit * sum(ones)
#
# print(answer)


