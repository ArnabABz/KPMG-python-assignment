element = int(input("Enter number : "))

while(element > 0):
    reminder = element % 10
    
    element = element // 10
    print(reminder,end= " ")
