#naming canvention
#the nameing convention for a function is the same as variables.
 #   *it should be composed of alphabets,numbers and underscores sholud start with an alphabet or underscore

#->snake_case
#->camelCase
#->TitleCase
#* return statement


#function example

'''def area_of_circle():
    print(3.14*5*5)
    
area_of_circle()'''
#print (area_of_circle()+10)


#return statement 

#*above is how define a function and call it now we went to add 1 to it or 2 to it Can't we take it to a variable ?
#* this is what return statements are for. It is like black box where you want some task to be done . But after the task is done want it to return somr value as well.

'''def abc():
    return 5

print (abc())

a=abc()
print (a)'''

#2.
'''def area_of_circle():
    return 3.14*5*5

print(area_of_circle())
print(area_of_circle()+10)'''

#Note : functions execution ends at return. once a return statement is found rest of the line of the code will not be ecxecuted.
#it is just like Break in loops

#* if you do return without any value, it will return none.

'''def abc():
    print("hello")
    return
    print("world")
    print("tops")
print(abc())'''


'''def even_odd():
    a=int(input("enter a number: "))
    if a%2==0:
        return "even"
    else:
        return "odd"
print(even_odd())'''


#Parameter and Argument in function

'''def area_of_circle_5():
    return 3.14*5*5
print(area_of_circle_5())'''

'''def area_of_circle_20():
    return 3.14*20*20
print(area_of_circle_20())'''


'''def area_of_circle(radius):
    return 3.14*radius*radius
print(area_of_circle(10))'''


'''def sum(a,b):
    return a+b
print(sum(10,20))'''


#* if you want multiple perameters you can simply sperate them by comma , their types are not required.
#* if the fuction is not resturning anything, then by default it will return none.
#* in python, a peramter is variable used in a function defination, while an argument is an actual value passed to the funtion during a call.
#* in the above function, radius, variable in the area_circle() function is a perameter , wheres the  passed to it while calling, ia an argument.

#***functions 

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def calculate_salary(base_monthly,bonus,equity):
    yearly_base=mul(base_monthly,12)
    yearly_base_bonus=sum(yearly_base,bonus)
    total_salary=sum(yearly_base_bonus,equity)
    return total_salary


a=calculate_salary(10000,5000,10000)
print(a+1000)




