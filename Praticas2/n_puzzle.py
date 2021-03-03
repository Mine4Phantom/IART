#a)
from copy import deepcopy
import sys



#end_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

end_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] 

class Node:
    def __init__(self, currentPos, parent):
        self.matrix = currentPos
        self.parent = parent
        self.children = []
        if parent != None:
            self.cost = parent.getCost() + 1
        else:
            self.cost = 0

    def getCost(self):
        return self.cost


    def addChild(self, new_matrix):
        self.children.append(Node(new_matrix))

    
    def addChild(self, node):
        self.children.append(node)

    def compareAncient(self, parentnode):
        if self.matrix == parentnode.matrix:
            return False
        elif parentnode.parent == None:
            return True
        else:
            return self.compareAncient(parentnode.parent)


def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] == 0):
                return [j,i]

def up(matrix):
    pos = find_empty(matrix)
    xs = pos[0]
    ys = pos[1]
    if ys < 1:
        return False
    matrix[ys][xs]  = matrix[ys - 1][xs]
    matrix[ys - 1][xs] = 0
    ys -= 1


def down(matrix):
    pos = find_empty(matrix)
    xs = pos[0]
    ys = pos[1]
    if ys > len(matrix) - 2:
        return False
    matrix[ys][xs]  = matrix[ys + 1][xs]
    matrix[ys + 1][xs] = 0
    ys += 1 


def left(matrix):
    pos = find_empty(matrix)
    xs = pos[0]
    ys = pos[1]
    if xs < 1:
        return False
    matrix[ys][xs]  = matrix[ys][xs - 1]
    matrix[ys][xs - 1] = 0
    xs -= 1


def right(matrix):
    pos = find_empty(matrix)
    xs = pos[0]
    ys = pos[1]
    if xs > len(matrix) - 2:
        return False
    matrix[ys][xs]  = matrix[ys][xs + 1]
    matrix[ys][xs + 1] = 0
    xs += 1


def check (matrix, end_matrix):
    return matrix == end_matrix


queue = []


def breadth_first_search():
    initial = queue.pop(0)
    '''
    x = input()
    print("\n")
    print(initial.matrix)
    print("\n")
    '''
    i = 0
    while i < 4:
        matrix = deepcopy(initial.matrix)
        if i == 0:
            down(matrix)
        elif i == 1:
            right(matrix)
        elif i == 2:
            up(matrix)
        elif i == 3:
            left(matrix)

        print(matrix)
        
        node = Node(matrix, initial)
        initial.addChild(node)

        if (check(matrix, end_matrix)):     
            return 1
        queue.append(node)
        i += 1
    return breadth_first_search() + 1

def greedy_search(heuristic):
    children = []
    initial = queue.pop(0)
    i = 0
    while i < 4:
        matrix = deepcopy(initial.matrix)
        if i == 0:
            up(matrix)
        elif i == 1:
            left(matrix)
        elif i == 2:
            down(matrix)
        elif i == 3:
            right(matrix)

        node = Node(matrix, initial)
        initial.addChild(node)

        if (check(matrix, end_matrix)):     
            return 1
        children.append(node)
        i += 1

    # Applies our heuristic to sort the children by cost
    children.sort(key = heuristic)
    for childrennode in children:
        if childrennode.compareAncient(childrennode.parent):
            #print(childrennode.matrix)
            queue.append(childrennode)
    return greedy_search(heuristic) + 1


def heuristic1(node):
    off_pos = 0
    matrix = node.matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[j][i] == end_matrix[j][i]):
                continue
            else:
                off_pos += 1
    return node.getCost() + off_pos


def heuristic2(node):
    manhattan_sum = 0
    matrix = node.matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[j][i] == end_matrix[j][i]):
                continue
            else:
                for a in range(len(matrix)):
                    for b in range(len(matrix)):
                        if (matrix[b][a] == end_matrix[j][i]):
                            manhattan_sum += abs(a-i)+ abs(b-j)
    return manhattan_sum + node.getCost()

       

sys.setrecursionlimit(10000)

initial1 = Node([[1, 3, 6], [5, 2, 0], [4, 7, 8]], None)
initial2 = Node([[1, 6, 2], [5, 7, 3], [0, 4, 8]], None)
initial3 = Node([[5, 1, 3, 4], [2, 0, 7, 8], [10, 6, 11, 12], [9, 13, 14, 15]], None)
#initial4 = Node([[2, 11, 5, 4], [1, 6, 3, 10], [9, 14, 8, 15], [13, 12, 0, 7]], None)
#initial5 = Node([[13, 9, 4, 0], [6, 15, 1, 8], [10, 11, 3, 5], [14, 12, 7, 2]], None)

#print("Breadth first search : " + str(breadth_first_search()))

queue.clear()
queue.append(initial3)
print( "Test 1 with Greedy Search with H1: " + str(greedy_search(heuristic1)))
queue.clear()
queue.append(initial3)
print( "Test 1 with Greedy Search with H2: " + str(greedy_search(heuristic2)))
'''
queue.clear()
queue.append(initial2)
print( "Test 2 with Greedy Search with H1: " + str(greedy_search(heuristic1)))
queue.clear()
queue.append(initial2)
print( "Test 2 with Greedy Search with H2: " + str(greedy_search(heuristic2)))

'''
