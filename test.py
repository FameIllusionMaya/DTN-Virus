from module import *



virus = Virus(5, 5, 1)
node_s = list()
node_i = list()
for i in range(4):
    node_s.append(Node([1, 1], "S", i, virus))

for i in node_s:
    print(i.life)


node_i.append(node_s[0])
node_s[0], node_s[-1] = node_s[-1], node_s[0]
print("node_s")
for i in node_s:
    
    print(i.life)
del node_s[0::]
print("node_s")
for i in node_s:
    
    print(i.life)
print("node_i")
for i in node_i:
    print(i.life)

