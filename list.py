comm_ord = [n.split() for n in [input() for x in range(int(input()))]]
# print(comm_list)
comm_list = []

for comm in comm_ord:
    # print (comm)
    if comm[0] == "insert":
        comm_list.insert(int(comm[1]), int(comm[2]))
    elif comm[0] == "print":
        print(comm_list)
    elif comm[0] == "remove":
        comm_list.remove(int(comm[1]))
    elif comm[0] == "append":
        comm_list.append(int(comm[1]))
    elif comm[0] == "sort":
        comm_list.sort()
    elif comm[0] == "pop":
        comm_list.pop()
    elif comm[0] == "reverse":
        comm_list.reverse()
