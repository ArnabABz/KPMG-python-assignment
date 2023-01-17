lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	element = int(input())
	lst.append(element)
print(lst)
print("divisable by 5:")
for i in range(0, n):
    if (lst[i]%5==0):
        print (lst[i])
