lower = 10
upper = 50

for num in range(lower, upper + 1): #10 11

   if num > 1: #10>1    11>1
       for i in range(2, num): #2,10    2,11
           if (num % i) == 0: #10%2==0  11%2==0
               break
       else:
           print(num)