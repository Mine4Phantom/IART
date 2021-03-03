from dataclasses import dataclass   
from copy import deepcopy

@dataclass
class Bucket:
    maximum : int
    value : int


class Node:
    def __init__(self, bucket1, bucket2, parent):
        self.b1 = bucket1
        self.b2 = bucket2
        self.parent = parent
        self.children = []
    
    def addChild(self, bucket1, bucket2):
        self.children.append(Node(bucket1, bucket2))
    
    def addChild(self, node):
        self.children.append(node)

    def print(self):
        if (self.parent != None):
            self.parent.print()
            print(self.b1, self.b2)

        

def emp(bucket):
    if bucket.value > 0:
        bucket.value = 0
        return True
    else:
        return False

def fill(bucket):
    bucket.value = bucket.maximum

def pour(bucket1, bucket2):
    if bucket1.value > 0 and bucket2.value < bucket2.maximum:
        if (bucket2.value + bucket1.value) <= bucket2.maximum:
            bucket2.value += bucket1.value
            bucket1.value = 0
        else:
            bucket1.value -= bucket2.maximum - bucket2.value
            bucket2.value = bucket2.maximum
        return True
    else:
        return False

def check(bucket1, value):
    return bucket1.value == value


queue = []
value = 2 #change for necessity

def breathFirstSearch():
    initial = queue.pop(0)
    i = 0
    while i < 6:
        bucket1 = deepcopy(initial.b1)
        bucket2 = deepcopy(initial.b2)
        if i == 0:
            fill(bucket1)
        elif i== 1:
            fill(bucket2)
        elif i== 2:
            emp(bucket2)
        elif i== 3:
            emp(bucket2)
        elif i== 4:
            pour(bucket1, bucket2)
        elif i== 5:
            pour(bucket2, bucket1)


        node = Node(bucket1, bucket2, initial)
        initial.addChild(node)
        
        if (check(bucket1, value)):
            node.print()
            return
        queue.append(node)
        i += 1
    breathFirstSearch()
        
size1 = input("First container size:")
size2 = input("Second container size:")


b1 = Bucket(int(size1), 0)
b2 = Bucket(int(size2), 0)

initial = Node(b1, b2, None)
queue.append(initial)

breathFirstSearch()

