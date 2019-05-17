from single_cycle_link_list import  SingleCycleLinkList



l1 = SingleCycleLinkList()
print(l1.is_empty())
print(l1.length())

l1.append(1)
print(l1.is_empty())
print(l1.length())
l1.append(2)
l1.add(8)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.insert(-1, 9)
l1.travel()
l1.insert(2, 100)
l1.travel()
l1.insert(10, 200)
l1.travel()
print(l1.search(100))
l1.remove(9)
l1.travel()
l1.remove(200)
l1.travel()