lst=[]
n=int(input("enter the number of elements : "))
for i in range (0,n):
    elements=int(input())
    lst.append(elements)
print(lst)
a=lst          
positive =0
negative =0
for num in a :
    if num >= 0:
        positive = positive + 1
    else :
        negative = negative +1

print("positive numbers : ",positive)
print("negative number : ",negative)

            

