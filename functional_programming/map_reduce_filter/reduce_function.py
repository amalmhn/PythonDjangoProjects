from functools import *
lst=[10,11,12,13,14,15]

sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)

max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)

#Sum of even numbers
sum_even=reduce(lambda no1,no2:no1+no2,list(filter(lambda no:no%2==0,lst)))
print(sum_even)

even_mini=reduce(lambda no1,no2:no1 if no1<no2 else no2,list(filter(lambda no:no%2==0,lst)))
print(even_mini)