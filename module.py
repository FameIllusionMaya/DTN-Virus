"""This file contain Class for Virus and Node object"""

class Virus:
    def __init__(self, tran_range, ttl, kill_power):
        """virus contain / transmission range / Time to live / Power to decrease host's hp"""
        self.tran_range = tran_range
        self.ttl = ttl
        self.kill_power = kill_power

class Node:
    def __init__(self, position, state, life, virus):
        """position is list contain [x, y] / infected state / hp / virus inside"""
        self.position = position
        self.state = state
        self.life = life
        self.virus = virus