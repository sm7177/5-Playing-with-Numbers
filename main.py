number=int(input("Enter a number to check pallindrom or not:"))

originalno=number
reverse=0

while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number//=10
    
if originalno==reverse:
    print("Number is pallindrom")
else:
    print("Number is not pallindrom")