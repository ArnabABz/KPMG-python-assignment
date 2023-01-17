element=int(input("Enter a number:"))
temp=element
reverse=0
while(element>0):
    rem=element%10
    reverse=reverse*10+rem
    element=element//10
if(temp==reverse):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
