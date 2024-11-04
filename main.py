number=int(input("Enter a number to check palindrome or not:"))

originalno=number
reverse=0

while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number//=10
    
if originalno==reverse:
    print("Number is palindrome")
else:
    print("Number is not palindrome")