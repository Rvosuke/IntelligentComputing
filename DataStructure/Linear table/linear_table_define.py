# algrithm 2-1

def union(La: list, Lb: list) -> list:
    for i in range(len(Lb)):
        La.append(Lb[i]) if Lb[i] not in La else ...
    return La


def merge_list(La: list, Lb: list) -> list:
    """
    the key is to merge two ordered list
    we use two pointers to point the current element of La and Lb
    But we need to consider the situation that one of the list is empty
    in Python, empty is consider the index out of range

    Next attention: don't feel it complex when we define some if-else condition
    :param La:
    :param Lb:
    :return:
    """
    Lc = []
    pa, pb, pc = 0, 0, 0
    len_La = len(La)
    len_Lb = len(Lb)
    while pc < len_La + len_Lb:
        if pa < len_La and pb < len_Lb:
            if La[pa] < Lb[pb]:
                Lc.append(La[pa])
                pa += 1
            else:
                Lc.append(Lb[pb])
                pb += 1
        elif pa > len_La and pb < len_Lb:
            Lc.extend(Lb[pb:])
        elif pa < len_La and pb > len_Lb:
            Lc.extend(La[pa:])
        else:
            break
    return Lc


list1 = [1, 2, 3]
list2 = [1, 3, 5]

print(union(list1, list2))
print(merge_list(list1, list2))
