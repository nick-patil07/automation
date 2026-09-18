# *Assiment operater
# = is an assiment operater,
# it will assing value to the variable


'''a=25
print(a)
a=a+25
print(a)


#shorthand 
a+=25
print(a)

a/=2
print(a)

a*=2
print(a)'''


# * logical operaters 
# AND
# true and true -> true
# true and false -> false
# false and true -> false
# false and false -> false 

'''age=30
print((age>20)and(age<40))

print(('Aakar'=='Aakar')and(-2<-3))'''


# OR
# true or ture -> true
# true or false -> true
# false or true -> true 
# false or false -> false 

'''print((2<3) or (2<4))
print(('Aakar' == 'aakar') or (-2<-3))'''

# Not or !=
#not true -> false 
#not false -> true

'''print(not('piyush'=='piyush'))'''


# *conditional statement 

'''m_comp = 120
m_culture = 'positive'
m_distance = 300

g_comp = 110
g_culture = 'positive'
g_distance = 30

if m_comp>80:
    print("microsoft criteria filled!!!")
elif g_comp>80:
    print("google criteria filled!!!")
else:
    print("sad life!!!")'''


#nested

'''m_comp = 110
m_culture = 'positive'
m_dis = 300

g_comp = 110
g_culture = 'positive'
m_dis= 3000

if m_comp>80 and g_comp>80:
    if m_dis> g_dis:
        print("go to google")
    else:
        print("go to microsoft")'''



# problem statement : traffic lights
# you have to ask about the colour of the traffic light from the user,
# if : it is green , then print go,
# it is yellow , then print wait,
# it is red , then print stop,
# green->go , yellow->wait , red-> stop 


'''light=input("enter the colour of light:")
if light=='green':
    print("goo")
elif light=="yellow":
    print("wait")
elif light=="red":
    print("stop")
else:
    print("invalid creadentials")'''