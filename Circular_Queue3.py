class Node:
    def __init__(node, data:int):  
        node.data = data  
        node.next = None

class CircularQueue:
    def __init__(circularqueue, MaxSize:int):  
        circularqueue.rear = None
        circularqueue.front = None
        circularqueue.MaxSize = MaxSize
        circularqueue.Size = 0

def CreateCircularQueuePY(size:int):
    error = False
    if size <= 0:
        error = True, error
        return None
    return CircularQueue(size), error

def is_emptyPY(cq):
    return cq.Size == 0
 
def is_fullPY(cq):
    return cq.Size == cq.MaxSize

def EnqueuePY(cq, element:int):
    newNode = Node(element)
    if is_emptyPY(cq):
        newNode.next = newNode
        cq.front = newNode
        cq.rear = newNode
        cq.Size = 1
    elif is_fullPY(cq):
        if cq.MaxSize == 1:
            cq.front = newNode
            cq.rear = newNode
            newNode.next = newNode
        else:
            nextNode = cq.front.next
            cq.front = nextNode
            newNode.next = cq.front
            cq.rear.next = newNode
            cq.rear = newNode
    else:
        newNode.next = cq.front
        cq.rear.next = newNode
        cq.rear = newNode
        cq.Size += 1

def DequeuePY(cq):
    error = False
    if is_emptyPY(cq):
        error = True
        return -1, error
    if cq.Size == 1:
        element = cq.front.data
        cq.front = None
        cq.rear = None
        cq.Size = 0
        return element, error
    else:
        nextNode = cq.front.next
        element = cq.front.data
        cq.front = nextNode
        cq.rear.next = nextNode
        cq.Size -= 1
        return element, error

def checkPY(cq):
    empty = False
    item = []
    if is_emptyPY(cq):
        empty = True
        return item, empty
    currentNode = cq.front
    for i in range(cq.Size):
        item.append(currentNode.data)
        currentNode = currentNode.next
    return item, empty

def DeleteCircularQueuePY(cq):
    if cq is not None:
        while cq.Size > 0:
            DequeuePY(cq)

def SizeCircularQueuePY(cq):
    return cq.Size