amount=0
d=int(input("Enter number of Deposit/Withdraw tansactions you want to enter:"))#taking input from the user for number of Depost/withdraw transactions
for i in range(d):
    sd=input().split(" ")
    if "Deposit" in sd:#If deposited it is an addition
        amount+=int(sd[1])
    elif "Withdraw" in sd:
        amount-=int(sd[1])#If withdraw it is a subtraction
    else:
        pass
print("Total amount - $"+str(amount))#displaying final amount
