print(3*10/2)
print((3*10)/2)
print(45%10/2)
print(True and not False)


a=5
if a>10:
    print(a)
    if a%5==2:
        print("bla")
else:
    print(a)
    print(1234)


'''
variable initialization
while (condition)
{
action
update variable 
}
'''
#while
#print numbers from 1 to 15

count=1
while(count<=15):
    print(count)
    count+=1

#break
count=1
while(count<=15):
    if count==10:
        break
    print(count)
    count+=1


#continue
count=0
while(count<=15):
    count+=1
    if count==10:
        continue
    print(count)


count=0
while count <= 5: #5<=5
    count += 1 #6
    if count == 3: #6==3
        continue
    print(count)#5


#while else

count=0
while count<=15:
    count+=1
    print(count)
    if count==10:
        break
else:
    print("complete")
    print("yay")
    