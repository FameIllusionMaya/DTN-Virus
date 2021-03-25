"""virus contain / transmission range / Time to live / Power to decrease host's hp"""
"""Node contain / position is list contain [x, y] / infected state / hp / virus inside"""

from module import *
from random import randint
import matplotlib.pyplot as plt


# set default virus status
for test in range(2):
    tran_range, ttl = 25, 90
    virus = Virus(tran_range, ttl)

    # set node information
    node_amount = 500


    node_s, node_i, node_r  = list(), list(), list() #SIR = can infected/ infected / recovery immune
    # set default node status
    # position in range 0-10000 square meter each person space 1 square meter


    area_w, area_h = 1000, 1000
    for node in range(1, node_amount):
        pos_x, pos_y = randint(0, area_w), randint(0, area_h)
        node_s.append(Node([pos_x, pos_y], "S", virus.ttl))
    pos_x, pos_y = randint(0, area_w), randint(0, area_h)
    node_i.append(Node([500, 500], "I", virus.ttl)) #infected No.0


    turn = 0
    run = True
    turn_count = 0
    s_i = 0
    i_r = 0

    g_infect_list = [0]*1000
    g_healthy_list = [0]*1000
    g_recover_list = [0]*1000
    g_time_list = []
    for i in range(1000):
        g_time_list.append(i)



    while run:
        

        #state I can change state to R or D
        last_infect_index = -1
        for index in range(len(node_i) - 1, -1, -1):
            node_i[index].move()
            node_i[index].recovery()

            if node_i[index].state == "R":
                node_r.append(node_i[index])
                node_i[index], node_i[last_infect_index] = node_i[last_infect_index], node_i[index]
                last_infect_index -= 1
                i_r += 1
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
                s_i += 1
        if last_healthy_index < -1:
            del node_s[last_healthy_index + 1::]
        print(len(node_s), len(node_i), len(node_r), len(node_s)+len(node_i)+len(node_r))

        g_infect_list[turn_count] += len(node_i)

        g_healthy_list[turn_count] += len(node_s)
        g_recover_list[turn_count] += len(node_r)


        turn_count += 1
        
        if len(node_i) == 0:
            run = False

for i in range(1000):
    g_infect_list[i] /= 2
    g_healthy_list[i] /= 2
    g_recover_list[i] /= 2


plt.plot(g_time_list, g_healthy_list, label = "healthy")
plt.plot(g_time_list, g_infect_list, label = "infected")
plt.plot(g_time_list, g_recover_list, label = "recover")
plt.xlabel('turn')
# naming the y axis
plt.ylabel('population')
# giving a title to my graph
plt.title('healthy/infected amount')
  
# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()

