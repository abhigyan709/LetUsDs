# in python list is dynamic data type used to creatdynamic array and it grows and shrinks on the requirements
# lets create an empty list in pythyon

import sys


def list_details(lst):
    # number of the elements that can be stored in the list
    print("Capacity: ", (sys.getsizeof(lst)-36)//4)

    # number of the elements in the list
    print("Size: ", len(lst))

    # number of elements that can be accomodated in the space left
    print("Space Left: ", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

    # formula changes based on the system architecture
    # (size-36)/4 for 32 bit machines
    # (size-64)/4 for 64 bit machines

    # 36, 64, size of an empty list based upon machine
    # 4, 8, size of a single element in the list based on machine


marias_lst = []
print("Empty list created!!")
print("List details: ")
list_details(marias_lst)


# for thi sprogram the capacity is increasing and decreasing dynamically on requirements
# initially it is started with certain capacity then its size get increased when we added a grocery item to the list

