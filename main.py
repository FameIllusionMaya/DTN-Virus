"""DTN virus simulation project main file"""
"""input choice to show result graph for our experiment"""

from SI_standard import *
from SIR_standard import *

while True:
    print("----DTN virus simulator main page----")
    print("1 : show default SI graph")
    print("2 : show default SIR graph")
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
    elif str.lower(choice) == "q":
        break
    else:
        continue