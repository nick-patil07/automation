#reverse program 
'''T=int(input("enter a single digit:"))
while T>0:
    N=int(input("enter a digit:"))
    if N<0:
      copy=N*-1
    else:
        copy=N
    rev=0
    while copy>0:
        d=copy%10 #last digit
        rev=rev*10+d
        copy//=10
    if N<0:
        rev=rev*-1
    print (rev)
    T-=1'''

#pattern program 
'''for _ in range(5):
    print('*'*5)'''


'''for i in range (1,6):
    print('*'*i)'''


#Home work

'''for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)'''



###############################

#LECTURE 7

#Need function
#bankig system

'''
**************************
transaction complete
thank you for visiting
**************************
''' 

'''#code:
print('*'*25)
print('transaction complete.')
print('thank you for visiting.')
print('*'*25)
'''


#DRY-DO NOT REPEAT YOUR SELF
'''
*************************
transaction complete.
thank you for visiting.
*************************
'''


#syntax of defining functions
#defining a function

'''
def function_name():
    #action
'''

# to call the function

'''
function_name()
'''
