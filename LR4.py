class graf:
    def  __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def depth(graf, l):
    if graf.name not in l:
        l.append(graf.name)
    for i in graf.children:
        if i.name not in l:
            l.append(i.name)
        depth(i, l)
    return l

def width(graf):
    l1 = []
    l2 = []
    if graf.name not in l1:
        l1.append(graf.name)
        l2.append(graf)
    for i in l2:
        for x in i.children:
            if x.name not in l1:
                l1.append(x.name)
                l2.append(x)
    return l1

root = graf("A")
b = graf("B")
c = graf("C")
d = graf("D")
e = graf("E")
f = graf("F")
g = graf("G")
h = graf("H")
i = graf("I")
root.add_child(b)
root.add_child(c)
root.add_child(d)
b.add_child(e)
b.add_child(f)
c.add_child(g)
d.add_child(h)
g.add_child(i)
h.add_child(i)

print('Обход графа в глубину:', depth(root, []))
print('Обход графа в ширину:', width(root))