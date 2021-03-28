"""this module will use SIR model compare transmission rate performance of node amoutnt/transmission range/TTL"""
"""find average transmission range"""

from module import *
from random import randint
import xlwt
from xlwt import Workbook
import xlrd

def tran_rate(node_amount, tran_range, ttl, test_round):
    wb = Workbook()
  
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, "Time use(units)")
    sheet1.write(0, 1, "Total infect")
    sheet1.write(0, 2, "highest infect")
   
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
        max_infect = 0

        while True:
            turn_count += 1
            #state I can change state to R or D
            last_infect_index = -1
            for index in range(len(node_i) - 1, -1, -1):
                node_i[index].move(area_w, area_h)
                node_i[index].recovery()

                if node_i[index].state == "R":
                    node_r.append(node_i[index])
                    node_i[index], node_i[last_infect_index] = node_i[last_infect_index], node_i[index]
                    last_infect_index -= 1
            if last_infect_index < -1:
                del node_i[last_infect_index + 1::]

            last_healthy_index = -1
            for index in range(len(node_s) - 1, -1, -1):
                node_s[index].move(area_w, area_h)
                node_s[index].infect(node_i, virus.tran_range)
                if node_s[index].state == "I":
                    node_i.append(node_s[index])
                    node_s[index], node_s[last_healthy_index] = node_s[last_healthy_index], node_s[index]
                    last_healthy_index -= 1
                    total_infect += 1
                    max_infect = max(max_infect, len(node_i))
            if last_healthy_index < -1:
                del node_s[last_healthy_index + 1::]

            print(turn_count, total_infect)
            if len(node_i) == 0 or len(node_s) == 0:
                break

        sheet1.write(test+1, 0, turn_count)
        sheet1.write(test+1, 1, total_infect)
        sheet1.write(test+1, 2, max_infect)

    file_name = 'TranRate_' + str(node_amount) + '_' + str(tran_range) + '_' + str(ttl) + ".xls"
    wb.save(file_name)
            
def tran_rate_cal():
    """use infomation from excel to calculate transmission rate of each parameter"""
    avg_result = {
        "default": [0, 0, 0, 0],
        "node_amount": [0, 0, 0, 0],
        "tran_range": [0, 0, 0, 0],
        "ttl": [0, 0, 0, 0]
    }

    inventory_path = ["result/TranRate_default.xls", "result/TranRate_node.xls", "result/TranRate_tranrange.xls",\
     "result/TranRate_ttl.xls"]
    dict_key = ["default", "node_amount", "tran_range", "ttl"]

    for i in range(len(inventory_path)):
        time_use = list()
        total_infect = list()
        max_infect = list()
        loc = (inventory_path[i])
        w = xlrd.open_workbook(loc)
        sheet = w.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for row in range(1, sheet.nrows):
            time_use.append(int(sheet.cell_value(row, 0)))
            total_infect.append(int(sheet.cell_value(row, 1)))
            max_infect.append(int(sheet.cell_value(row, 2)))

        average_time_use = sum(time_use)/len(time_use)
        average_total_infect = sum(total_infect)/len(total_infect)
        average_max_infect = sum(max_infect)/len(max_infect)

        avg_result[dict_key[i]][0] = average_total_infect
        avg_result[dict_key[i]][1] = average_time_use
        avg_result[dict_key[i]][2] = average_total_infect/average_time_use
        avg_result[dict_key[i]][3] = average_max_infect

    return avg_result


