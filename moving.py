# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

blank=[[' ' for j in range (40)]for i in range (30)]
blank[19][13:31]='I',' ','c','a','n',' ','d','o',' ','a','l','l',' ','t','h','i','n','g','s'
#heart=[[' ' for j in range (9)]for i in range (8)]

sc=[[' ' for j in range (10)]for i in range (7)]
for j in [0,1,2,3,6,7,8,9]:
    sc[0][j]='*'
for j in [0,6]:
    sc[1][j]='*'
for j in [0,6]:
    sc[2][j]='*'
for i in [0,1,2,3,6]:
    sc[3][i]='*'
for i in [3,6]:
    sc[4][i]='*'
for i in [3,6]:
    sc[5][i]='*'
for i in [0,1,2,3,6,7,8,9]:
    sc[6][i]='*'
  
    f=open("sc.txt",'w')

for k in range(30):
    for i in range(7):
        for j in range(10):
            blank[i+10][j+k]=sc[i][j]

#    for i in range(4):
#        for j in range(k):
#            blank[i+10][j]=' '
                  
#output
    for i in range(30):
#     print 
         for j in range(40):
             f.write(str(blank[i][j]))
         f.write('\n')
#            print(blank[i][j],end="")
#         print('\n')


#clear
    for i in range(8):
        for j in range(9):
            blank[i+10][j+k]=' '

import os
m = os.system('cls')

f.close()
