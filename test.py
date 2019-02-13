from linkedlist_api import LinkedList


###################
# MAIN


def test():
    ll = LinkedList()
    ll.add("a")
    ll.add("b")
    ll.debug_print()
    ll.set(1, "B")
    ll.debug_print()
    ll.add("c")
    ll.debug_print()
    # ll.delete(3)
    ll.swap(0, 2)
    ll.debug_print()

    # print(ll.get(2))
    # ll.set(2, "C")
    # print(ll._get_node(2))
    # ll.add(0)
    # ll.insert(2, 1)
    # ll.add(2)


test()
