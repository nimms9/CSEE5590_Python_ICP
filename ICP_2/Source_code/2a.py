stack=[]

def push():
    apd=input("enter word/element to push:")
    stack.append(apd)
    print("pushed stack is:",stack)
    switcher = {
        1: push,
        2: top,
        3: pop,
        4: exit
    }
    print(switcher)
    k = input("Enter from the above displayed options:")
    print(switch(int(k)))
def top():
    print("top element is:", stack[-1])
    switcher = {
        1: push,
        2: top,
        3: pop,
        4: exit
    }
    print(switcher)
    k = input("Enter from the above displayed options:")
    print(switch(int(k)))
def pop():
    stack.pop()
    print("updated stack after pop:",stack)
    switcher = {
        1: push,
        2: top,
        3: pop,
        4: exit
    }
    print(switcher)
    k=input("Enter from the above displayed options:")
    print(switch(int(k)))


switcher ={
    1:push,
    2:top,
    3:pop,
    4:exit
}

def switch(x):
    return switcher.get(x)()
print(switcher)
k=input("Enter from the above displayed options:")
print(switch(int(k)))