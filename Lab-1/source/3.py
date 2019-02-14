lp=[]
l=''
while l!='q':
    l=input("Enter Student names in python class, enter 'q' to stop:\n")#taking input values and appending to the list for python class
    if l=='q':
        break
    else:
        lp.append(l)
sp=set(lp)
lw=[]
w=''
while w!='q':
    w=input("Enter student names in web application class, enter 'q' to stop:\n")#taking input values and appending to the list for webapplication class
    if w=='q':
        break
    else:
        lw.append(w)
sw=set(lw)#converting list to set to do set operations
print("Python class list:\n",lp)
print("Web application class list:\n",lw)
print("These are the Student names who are attending both the classes:\n",','.join(sp & sw))#Intersection
print("These are the students who are not common in both the classes:\n",','.join(sp ^ sw))#Symmetric difference
