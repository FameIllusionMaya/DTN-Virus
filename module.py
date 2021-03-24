"""This file contain Class for Virus and Node object"""
from random import randint

class Virus:
    def __init__(self, tran_range, ttl, kill_power):
        """virus contain / transmission range / Time to live / Power to decrease host's hp"""
        self.tran_range = tran_range
        self.ttl = ttl
        self.kill_power = kill_power

class Node:
    def __init__(self, position, state, life, virus_ttl):
        """position is list contain [x, y] / infected state / hp / virus inside"""
        self.position = position
        self.state = state
        self.life = life
        self.virus_ttl = virus_ttl

    def move(self):
        """node randomly move"""
        move_x, move_y = randint(-100, 100), randint(-50, 50)

        if self.position[0] + move_x < 0 or self.position[0] + move_x > 10000:
            move_x = -move_x
        elif self.position[1] + move_y < 0 or self.position[1] + move_y > 10000:
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
        # print("--", self.virus_ttl)
        if self.virus_ttl <= 0:
            self.state = "R"
    
    def dead(self):
        if self.life <= 0:
            self.state = "D"
