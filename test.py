from module import *

virus = Virus(5, 5, 1)
x = list()
for i in range(5):
    x.append(Node([1, 1], "S", 10, virus))

x[0].state = "I"
x[1].state = "R"
x[2].state = "D"

x[0], x[1] = x[1], x[0]

for i in x:
    print(i.state)
