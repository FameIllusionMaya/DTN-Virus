"""virus contain / transmission range / Time to live / Power to decrease host's hp"""
"""Node contain / position is list contain [x, y] / infected state / hp / virus inside"""

from module import *
from random import randint



# set default virus status
tran_range, ttl, kill_power = 5,  5, 1
virus = Virus(tran_range, ttl, kill_power)

# set node amount
node_amount = 1000

node_list = list()
# set default node status
# position in range 0-10000 square meter each person space 1 square meter
for node in range(node_amount):
    pos_x, pos_y = randint(0, 10000), randint(0, 100000)
    node_list.append(Node([pos_x, pos_y], "S", randint(10, 30), virus))



