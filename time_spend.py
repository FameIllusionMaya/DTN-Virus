"""this module will use SIR model compare transmission rate performance of node amoutnt/transmission range/TTL"""
"""find average transmission range"""

from module import *
from random import randint
import xlwt
from xlwt import Workbook
import xlrd

def time_use(node_amount, tran_range, ttl, test_round):
    wb = Workbook()
  
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, "Time use(units)")
   
    for test in range(test_round):
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

        turn_count = 0 #time use
        while True:
            turn_count += 1
            #state I can change state to R or D
            last_infect_index = -1
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

            print(turn_count, len(node_s))
            if len(node_s) <= 0.01*node_amount:
                break

        sheet1.write(test+1, 0, turn_count)

    file_name = 'TimeUse' + str(node_amount) + '_' + str(tran_range) + '_' + "area" + ".xls"
    wb.save(file_name)
            
def time_use_cal():
    """use infomation from excel to calculate transmission rate of each parameter"""
    avg_result = {
        "default": 0,
        "node_amount": 0,
        "tran_range": 0,
        "area": 0
    }

    inventory_path = ["result/TimeUse_default.xls", "result/TimeUse_node.xls", "result/TimeUse_tranrange.xls",\
     "result/TimeUse_area.xls"]
    dict_key = ["default", "node_amount", "tran_range", "area"]

    for i in range(len(inventory_path)):
        time_use = list()
        loc = (inventory_path[i])
        w = xlrd.open_workbook(loc)
        sheet = w.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for row in range(1, sheet.nrows):
            time_use.append(int(sheet.cell_value(row, 0)))

        average_time_use = sum(time_use)/len(time_use)
        avg_result[dict_key[i]] = average_time_use

    return avg_result


