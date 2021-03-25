"""This file contain Class for Virus and Node object"""
from random import randint
from random import randrange

class Virus:
    def __init__(self, tran_range, ttl):
        """virus contain / transmission range / Time to live"""
        self.tran_range = tran_range
        self.ttl = ttl

class Node:
    def __init__(self, position, state, virus_ttl):
        """position is list contain [x, y] / infected state/ virus inside"""
        self.position = position
        self.state = state
        self.virus_ttl = virus_ttl

    def move(self):
        """node randomly move"""
        move_x, move_y = randint(-10, 10), randint(-10, 10)

        if self.position[0] + move_x < 0 or self.position[0] + move_x > 10000:
            move_x = -move_x
        if self.position[1] + move_y < 0 or self.position[1] + move_y > 10000:
            move_y = -move_y
        self.position[0] += move_x
        self.position[1] += move_y
        
    def infect(self, node_i, tran_range):
        """ S node close to I node infect S turn to I"""
        for node in node_i:
            diff_x = abs(self.position[0] - node.position[0])
            diff_y = abs(self.position[1] - node.position[1])
            if (diff_x**2 + diff_y**2)**0.5 <= tran_range:
                self.state = "I"
    
    def recovery(self):
        """if TTL = 0 node is recover and immune to virus"""
        self.virus_ttl -= 1
        if self.virus_ttl <= 0:
            self.state = "R"
