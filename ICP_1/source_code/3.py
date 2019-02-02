inpstring = input("please input string:") #sample string  
letters = 0  # initiating the count of letters to 0
digits = 0  # initiating the count of numbers to 0

for i in inpstring:  
    if i.isdigit():      
        digits +=1      
    elif i.isalpha():    
        letters +=1    
    else:    
        pass  
print("Letters:",letters)
print("Digits:",digits)
