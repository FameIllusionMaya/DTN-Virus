"""this module will use SIR model compare transmission rate performance of node amoutnt/transmission range/TTL"""
"""find average transmission range"""

from module import *
from random import randint
import xlwt
from xlwt import Workbook

def test(node_amount, tran_range, ttl, test_round):

   
    for test in range(test_round):
        virus = Virus(tran_range, ttl)
        node_s, node_i, node_r  = list(), list(), list() #SIR = can infected/ infected / recovery immune
        # set default node status and position
        # position in range between 0 to area_w in x_axis and area_h in y_axis unit
        area_w, area_h = 1000, 1000
        for node in range(1, node_amount):
            pos_x, pos_y = randint(0, area_w), randint(0, area_h)
            node_s.append(Node([pos_x, pos_y], "S", virus.ttl))
        pos_x, pos_y = randint(0, area_w), randint(0, area_h)
        node_i.append(Node([400, 400], "I", virus.ttl)) #infected No.0

        turn_count = 0 #time use
        total_infect = 0

        while True:
            turn_count += 1
            #state I can change state to R or D
            last_infect_index = -1
            for index in range(len(node_i) - 1, -1, -1):
                node_i[index].move()
                node_i[index].recovery()

                if node_i[index].state == "R":
                    node_r.append(node_i[index])
                    node_i[index], node_i[last_infect_index] = node_i[last_infect_index], node_i[index]
                    last_infect_index -= 1
            if last_infect_index < -1:
                del node_i[last_infect_index + 1::]

            last_healthy_index = -1
            for index in range(len(node_s) - 1, -1, -1):
                node_s[index].move()
                node_s[index].infect(node_i, virus.tran_range)
                if node_s[index].state == "I":
                    total_infect += 1
                    node_i.append(node_s[index])
                    node_s[index], node_s[last_healthy_index] = node_s[last_healthy_index], node_s[index]
                    last_healthy_index -= 1
            if last_healthy_index < -1:
                del node_s[last_healthy_index + 1::]

            print(turn_count, total_infect)
            if len(node_i) == 0 or len(node_s) == 0:
                break

    print(turn_count, total_infect)

test(750, 24, 100, 1)
            

