#Name: Parth Trehan
#RollNo.: 2010660

import os

clear = lambda: os.system('clear')
print 'Enter the number'
n = int(raw_input())
clear();
if (n<0):
    print 'no negative number, please enter a poisitive number'
else:
    while(n>=0):
        i = 10000000
        while(i>0):
            i = i-1
        print n
        n = n-1
        clear()
    print 'BLOWN'
