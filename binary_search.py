# implememtation of binary search algorithm

# we will prove that binary search os faster than naive search

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# binary search used divide and conquer!
# we will leverage the fact that our list is SORTED