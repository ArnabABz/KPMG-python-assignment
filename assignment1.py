lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	element = int(input())
	lst.append(element)
print(lst)
if (lst[0] == lst[-1]):
    print ("result is true")
else:
    print ("result is false")
