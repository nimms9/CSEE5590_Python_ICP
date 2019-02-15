l=[( 'John', ('Physics', 80)) , ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
di={}
for key,value in l:
    di.setdefault(key,[]).append(value)#appending tuples to the dictionary using setdefault method
print("Dictionary:",di)
sorted_di=sorted(di.items(), key=lambda x:x[0])#soritng the key value pairs using lambda and sorted method
print("Sorted:",dict(sorted_di))