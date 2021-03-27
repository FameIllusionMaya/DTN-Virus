"""DTN virus simulation project main file"""
"""input choice to show result graph for our experiment"""

from SI_standard import *
from SIR_standard import *
from TransmissionRate_compare import *

while True:
    print("----DTN virus simulator main page----")
    print("1 : show default SI graph")
    print("2 : show default SIR graph")
    print("3 : show transmission rate SIR model graph compare /node amount/transmission range/TTL")
    print("q : quit the program")
    choice = input("Please select method: ")
    if choice == "1":
        g_time_list, g_healthy_list, g_infect_list = si_graph()
        plt.plot(g_time_list, g_healthy_list, label = "healthy")
        plt.plot(g_time_list, g_infect_list, label = "infected")
        plt.xlabel('turn')
        plt.ylabel('population')
        plt.title('healthy/infected amount')
        plt.legend()
        plt.show()
    elif choice == "2":
        g_time_list, g_healthy_list, g_infect_list, g_recover_list = sir_graph()
        plt.plot(g_time_list, g_healthy_list, label = "healthy")
        plt.plot(g_time_list, g_infect_list, label = "infected")
        plt.plot(g_time_list, g_recover_list, label = "recover")
        plt.xlabel('turn')
        plt.ylabel('population')
        plt.title('healthy/infected/recover amount')
        plt.legend()
        plt.show()
    elif choice == "3":
        result = tran_rate_cal()
        left = [1, 2, 3, 4]
        height = [result["default"][2], result["node_amount"][2], result["tran_range"][2], result["ttl"][2]]
        tick_label = ['Default', '1.5x_NodeAmount', '1.5x_TranRange', '1.5x_TTL']
        plt.bar(left, height, tick_label = tick_label,
                width = 0.5, color = ['red', 'orange', "blue", "purple"])
        plt.xlabel('parameter')
        plt.ylabel('transmission rate')
        plt.title('transmission rate compare with SIR model')
        plt.show()
    elif choice == "4":
        result = tran_rate_cal()

    elif choice == "99":
        node_amount = int(input("Input Node amount: "))
        tran_range = float(input("Input transmission range: "))
        ttl = int(input("Input TTL: "))
        test_round = int(input("Input test round amount: "))
        tran_rate(node_amount, tran_range, ttl, test_round)
        pass
    elif str.lower(choice) == "q":
        break
    else:
        continue