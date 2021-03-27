"""this module will output standard SIR model graph with default virus setting"""
"""return healthy-infect-recover amount of population over time"""

from module import *
from random import randint
import matplotlib.pyplot as plt

def si_graph():
    # set default parameter
    tran_range, ttl = 24, 100
    node_amount = 500
    virus = Virus(tran_range, ttl)
    node_s, node_i  = list(), list() #SI = can infected/ infected
    # set default node status and position
    # position in range between 0 to area_w in x_axis and area_h in y_axis unit
    area_w, area_h = 1000, 1000
    for node in range(1, node_amount):
        pos_x, pos_y = randint(0, area_w), randint(0, area_h)
        node_s.append(Node([pos_x, pos_y], "S", virus.ttl))
    pos_x, pos_y = randint(0, area_w), randint(0, area_h)
    node_i.append(Node([400, 400], "I", virus.ttl)) #infected No.0
    #prepare list for this function return theese variable will use to plot graph
    g_infect_list = list()
    g_healthy_list = list()
    g_time_list = list()

    turn_count = 0 #time use
    while True:
        turn_count += 1

        #state I can change state to R or D
        for index in range(len(node_i) - 1, -1, -1):
            node_i[index].move()


        last_healthy_index = -1
        for index in range(len(node_s) - 1, -1, -1):
            node_s[index].move()
            node_s[index].infect(node_i, virus.tran_range)
            if node_s[index].state == "I":
                node_i.append(node_s[index])
                node_s[index], node_s[last_healthy_index] = node_s[last_healthy_index], node_s[index]
                last_healthy_index -= 1
        if last_healthy_index < -1:
            del node_s[last_healthy_index + 1::]

        g_infect_list.append(len(node_i))
        g_healthy_list.append(len(node_s))
        g_time_list.append(turn_count)
        
        if len(node_s) <= 0.02*node_amount:
            break

    return g_time_list, g_healthy_list, g_infect_list

