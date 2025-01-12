n = int(input("Enter a number: "))
i = 0
temp = n
while temp>0:
    digit=temp%10
    i+=digit**3
    temp//=10
if n==i:
    print("The number is an armstrong number.")
else:
    print("The number isn't an armstrong. ")