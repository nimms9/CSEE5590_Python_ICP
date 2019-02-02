from collections import deque

#Creating queue
queue = deque([])

def Enqueue():
    #enqueuing elements to the Queue
    sd=input("enter word/element to enqueue:")
    queue.append(sd)
    print("Updated queue:",queue)
    switcher={1:Enqueue,
              2:Deque,
              3:exit}
    print(switcher)
    k=input("Enter number from the displayed options above:")
    print(switch(int(k)))
def Deque():
    #Dequeuing elements from the queue
    print("Dequed element is:",queue.popleft())
    print("Updated queue:",queue)
    switcher = {1: Enqueue,
                2: Deque,
                3:exit}
    print(switcher)
    k = input("Enter number from the displayed options above:")
    print(switch(int(k)))


switcher = {1:Enqueue,
            2:Deque,
            3:exit}
def switch(x):
    return switcher.get(x)()
print(switcher)
k=input("Enter from the above displayed options:")
print(switch(int(k)))


