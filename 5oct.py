#* Scope of variable 

'''a=1 #global scope
def area_circle(radius):
    area= 3.14 * radius * radius #area is having a local scope
    return area
b = area_circle(10) #global 
print(a) #print 1
print(b) #314.0
print(area) #error '''


'''a = 1 #global
def abc():
    a = 2
    print(a) #2
abc() #2
print(a) #print 1'''


'''a = 1 #global
def abc():
    global a
    a = 2 #local scope
    print(a) #2
abc() #2
print(a) #print 2'''


# def foo(a):
#     if(a):
#         return 100
#     a += 20 #0+20
#     return a
# print(foo(0)) #20


# def solve(a,b):
#     print('function started')
#     return 0
#     c = a+ b
#     print('function ended')
# c = solve(2,3) #0
# print(c)


#Quiz 1

# foo() 1
# foo() 2
# for i in range(1,5):
#     foo()


#Quiz 2
# def area_rectangle(l,b):
#     area = l*b
# area_circle(3,4) #error
# print(area) #error


#simpal interest
#method 1
# p=int(input("enter the principle amount:"))
# r=int(input("enter the rate of interest:"))
# t=int(input("enter the time in years:"))

# simple_intrest=(p*r*t)/100

# print("the simple intrest is:",simple_intrest)


#method 2
# p=float(input("enter the principle amount:"))
# r=float(input("enter the rate of interest:"))
# t=float(input("enter the time in years:"))

# def simple_intrest(p,r,t):
#     return(p*r*t)/100

# simple_intrest_value=simple_intrest(p,r,t)
# print("the value of simple intrest is:",simple_intrest_value)




#*positional arguments

# def bio_data(name,age,gender):
#     print("name:",name)
#     print("age:",age)
#     print("gender:",gender)

# bio_data(name="nick",age=20,gender="male")

#* default and nondefault argument 
# def bio_data(name,age,gender="unspecified"):
#     print("name:",name)
#     print("age:",age)
#     print("gender:",gender)

# bio_data(name="aakar")



# def bio_data(name,age=0,gender=None):
#     print("name:",name)
#     print("age:",age)
#     print("gender:",gender)

# bio_data(name="aakar")


# print(round(3.6546546,3)) #3.655
# def abc(name,gender,age=0):
#     print(name,gender,age)
# abc(name = 'aakar', gender = 'male')

# def abc(a,b,c=10):
#     return a,b,c
# print(abc(1,2))