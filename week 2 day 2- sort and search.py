#Bubble sort
''''f=input("Enter list: ")
l=list(map(int, f.split(',')))
n=len(l)
for i in range (n):
    swapped=False
    for j in range (n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            swapped=True
    if not swapped:
            break
print ('Sorted list= ',l)'''

#Linear Search
'''def lin_search(x,arr):
    for i in range (len(arr)):
        if x==arr[i]:
            return f'{x} found at {i}'
    return f"{x} not found"
f=input("Enter list: ")
l=list(map(int, f.split(',')))
n=int(input("Enter number to search: "))
print(lin_search(n,l))'''

#Binary Search
def binary_search(x,arr):
    arr.sort()
    n=len(arr)
    if x==arr[n//2]:
        return f'{x} found at {n//2}'
    elif x>arr[n//2]:
        for i in range (n//2,n):
            if x==arr[i]:
                return f'{x} found at {i}'
    elif x<arr[n//2]:
        for i in range (n//2):
            if x==arr[i]:
                return f'{x} found at {i}'
    return f'{x} not found'
f=input("Enter list: ")
l=list(map(int, f.split(',')))
n=int(input("Enter number to find: "))
print (binary_search(n,l))


