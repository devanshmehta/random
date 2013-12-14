from itertools import combinations
from Queue import Queue

"""
   This is a puzzle. There are 3 Men, 1 Big Monkey, 1 Small Monkey.
   All the players are on the one side of the river. The goal of the 
   puzzle is to move all the players to other side of the river.
   Constraints are there is only one boat. Only 3 men and 1 big monkey
   can row the boat. Only 2 players can use the boat at one time. 
   If there are more monkeys than man on any side of the river at any 
   point of time, then monkeys will eat man.
"""

class Player:

    def is_man(self):
        pass

    def is_driver(self):
        pass

class Man(Player):

    def is_man(self):
        return True

    def is_driver(self):
        return True

    def __hash__(self):
        return 1
    
    def __str__(self):
        return "M"

class BigMonkey(Player):

    def is_man(self):
        return False

    def is_driver(self):
        return True

    def __hash__(self):
        return 2

    def __str__(self):
        return "BM"

class SmallMonkey(Player):

    def __hash__(self):
        return 3

    def is_man(self):
        return False

    def is_driver(self):
        return False

    def __str__(self):
        return "SM"

class Move:

    def __init__(self):
        self.players = []
        self.side = -1

    def __str__(self):
        if self.side == 1:
            return " ".join(map(str, self.players)) + " 1->2"
        else:
            return " ".join(map(str, self.players)) + " 2->1"

class Node:

    def __init__(self):
        self.side_1 = []
        self.side_2 = []
        self.chance = -1
        self.moves = []

    def __eq__(self, other):
        for i in self.side_1:
            if i not in other.side_1:
                return False
        for i in self.side_2:
            if i not in other.side_2:
                return False
        if self.chance != other.chance:
            return False
        return True

    def __hash__(self):
        hash = 0
        for i in self.side_1:
            hash += i.__hash__()
        for i in self.side_2:
            hash += i.__hash__()
        hash += self.chance.__hash__()
        return hash


    def __str__(self):
        return ("side1:" + " ".join(map (str, self.side_1)) + " side2:" + " ".join(map(str, self.side_2)) +
                "\nmoves:\n\t" +  "\n\t".join(map(str,self.moves)))

    def is_legal(self):
        if len(self.side_2) == 0:
            return False
        mon_side1 = 0
        man_side1 = 0
        for p in self.side_1: 
            if p.is_man():
                man_side1 += 1
            else:
                mon_side1 += 1
        if man_side1 > 0 and man_side1 < mon_side1:
            return False
            
        mon_side2 = 0
        man_side2 = 0
        for p in self.side_2: 
            if p.is_man():
                man_side2 += 1
            else:
                mon_side2 += 1
        if man_side2 > 0 and man_side2 < mon_side2:
            return False
        return True

    def moves_1(self):
        for i in combinations(self.side_1, 2):
            node = Node()
            p1, p2 = i            
            node.side_1 = [ j for j in self.side_1]
            node.side_2 = [ j for j in self.side_2]
            node.chance = 2
            node.moves = [ j for j in self.moves]
            node.side_1.remove(p1)
            node.side_1.remove(p2)
            node.side_2.append(p1)
            node.side_2.append(p2)
            if node.is_legal() and (p1.is_driver() or p2.is_driver()):
                move = Move()
                move.players.append(p1)
                move.players.append(p2)
                move.side = 1
                node.moves.append(move)
                yield node

        for i in combinations(self.side_1, 1):
            node = Node()
            p1 = i[0]
            node.side_1 = [ j for j in self.side_1]
            node.side_2 = [ j for j in self.side_2]
            node.chance = 2
            node.moves = [ j for j in self.moves]
            node.side_1.remove(p1)
            node.side_2.append(p1)
            if node.is_legal() and p1.is_driver():
                move = Move()
                move.players.append(p1)
                move.side = 1
                node.moves.append(move)
                yield node
        
    def moves_2(self):
        for i in combinations(self.side_2, 2):
            node = Node()            
            p1, p2 = i
            node.side_1 = [ j for j in self.side_1]
            node.side_2 = [ j for j in self.side_2]
            node.chance = 1
            node.moves = [ j for j in self.moves]
            node.side_2.remove(p1)
            node.side_2.remove(p2)
            node.side_1.append(p1)
            node.side_1.append(p2)
            if node.is_legal() and (p1.is_driver() or p2.is_driver()):
                move = Move()
                move.players.append(p1)
                move.players.append(p2)
                move.side = 2
                node.moves.append(move)
                yield node

        for i in combinations(self.side_2, 1):
            node = Node()            
            p1 = i[0]
            node.side_1 = [ j for j in self.side_1]
            node.side_2 = [ j for j in self.side_2]
            node.chance = 1
            node.moves = [ j for j in self.moves]
            node.side_2.remove(p1)
            node.side_1.append(p1)
            if node.is_legal() and p1.is_driver():
                move = Move()
                move.players.append(p1)
                move.side = 2
                node.moves.append(move)
                yield node

start_node = Node()
start_node.chance = 1
start_node.side_1.append(Man())
start_node.side_1.append(Man())
start_node.side_1.append(Man())
start_node.side_1.append(BigMonkey())
start_node.side_1.append(SmallMonkey())
start_node.side_1.append(SmallMonkey())

visited = {}
queue = Queue()
queue.put(start_node)
while not queue.empty():
    node = queue.get()
    if node in visited:
        continue
    visited[node] = ''
    if len(node.side_2) == 6:
        print node
    if node.chance == 1:
        for node in node.moves_1():
            queue.put(node)
    else :
        for node in node.moves_2():
            queue.put(node)
