# import functions_program.mathOperation
# resAdd=functions_program.mathOperation.add(150,100)
# print(resAdd)
#
# resSub=functions_program.mathOperation.sub(150,100)
# print(resSub)
#
# resMul=functions_program.mathOperation.mul(10,2)
# print(resMul)
#
# resDiv=functions_program.mathOperation.div(10,2)
# print(resDiv)

from functions_program.mathOperation import *

resAdd=add(150,100)
print(resAdd)

resSub=sub(150,100)
print(resSub)

resMul=mul(10,2)
print(resMul)

resDiv=div(10,2)
print(resDiv)

#anothe method is giving a nicname to the import file

import functions_program.mathOperation as fun
