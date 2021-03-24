"""virus contain / transmission range / Time to live / Power to decrease host's hp"""
"""Node contain / position is list contain [x, y] / infected state / hp / virus inside"""

from module import *
from random import randint
from random import randrange

# set default virus status
tran_range, ttl, kill_power = 300, 250, 1
virus = Virus(tran_range, ttl, kill_power)

# set node information
node_amount = 1000


node_s, node_i, node_r, node_d  = list(), list(), list(), list() #SIDR = can infected/ infected / recovery immune / dead
# set default node status
# position in range 0-10000 square meter each person space 1 square meter
for node in range(1, node_amount):
    pos_x, pos_y = randint(0, 10000), randint(0, 10000)
    node_s.append(Node([pos_x, pos_y], "S", randint(10, 30), virus.ttl))

area_w, area_h = 5000, 5000
pos_x, pos_y = randint(0, area_w), randint(0, area_h)
node_i.append(Node([pos_x, pos_y], "S", randint(10, 30), virus.ttl)) #infected No.0


turn = 0
run = True
while run:
    
    #state I can change state to R or D
    last_infect_index = -1
    for index in range(len(node_i) - 1, -1, -1):
        node_i[index].move()
        node_i[index].life -= 0.1 + randrange(virus.kill_power)
        node_i[index].dead()
        node_i[index].virus_ttl -= 1
        node_i[index].recovery()
        if node_i[index].state == "R":
            node_r.append(node_i[index])
            node_i[index], node_i[last_infect_index] = node_i[last_infect_index], node_i[index]
            last_infect_index -= 1
        elif node_i[index].state == "D":
            node_d.append(node_i[index])
            node_i[index], node_i[last_infect_index] = node_i[last_infect_index], node_i[index]
            last_infect_index -= 1
    if last_infect_index < -1:
        del node_i[last_infect_index + 1::]


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
    print(len(node_s), len(node_i), len(node_r), len(node_d), len(node_s)+len(node_i)+len(node_r)+len(node_d))

    # for i in node_i:
    #     print(i.state)
    
    if len(node_i) == 0:
        run = False

