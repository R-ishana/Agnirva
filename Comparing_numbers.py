#Code to find the largest number
max=int(input("Enter maximum numbers to compare: "))
l=list()
for i in range (max):
    n=int(input("Enter a number: "))
    l.append(n)
a=l[0]
for i in l:
    if a<i:
        a=i
print ("Largest Number is: ",a)

#Code to count maximum number of even integers
max=int(input("Enter maximum numbers to compare: "))
l=list()
for i in range (max):
    n=int(input("Enter a number: "))
    l.append(n)
c=0
for i in l:
    if i%2==0:
        c=c+1
print ('The number of even numbers are: ',c)

#Code to remove duplicates
l=[1,2,2,4,5,5,9]
d=list()
for i in range (len(l)):
    if l[i] in d:
        continue
    else:
        d.append(l[i])
print("List without duplicates: ",d)

#Code to reverse list
max=int(input("Enter maximum numbers to compare: "))
l=list()
for i in range (max):
    n=int(input("Enter a number: "))
    l.append(n)
d=list()
f=len(l)-1
for i in range (f,-1,-1):
    d.append(l[i])
print("Reveresed List: ",d)
        
'''please copy code block carefully'''
