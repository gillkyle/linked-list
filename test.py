from linkedlist_api import LinkedList


###################
# MAIN


def test():
    ll = LinkedList()
    ll.add("a")
    ll.add("b")
    print(ll._get_node(0))
    print(ll._get_node(1))
    print(ll._get_node(2))
    # ll.add(0)
    # ll.insert(2, 1)
    # ll.add(2)
    ll.debug_print()


test()
