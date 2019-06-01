


def linear_search(L, obj):
    for i in L:
        if obj == i:
            return True
    return False


def bisect_search1(L: list, e):
    """works only for sorted L list"""
    if not L:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        mid = len(L) // 2
        if e < L[mid]:
            return bisect_search1(L[:mid], e)
        else:
            return bisect_search1(L[mid:], e)


def bisect_search2(L: list, E):
    """works only for sorted L list"""
    def bisect_search_helper(l, e, low, high):
        if high == low:
            return l[low] == e
        mid = (low + high) // 2
        if e == l[mid]:
            return True
        elif e < l[mid]:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(l, e, low, mid-1)
        else:
            return bisect_search_helper(l, e, mid+1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, E, 0, len(L)-1)


def bubble_sort(L: list):
    flag = False
    while not flag:
        flag = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                flag = False
    return L


def selection_sort(L: list):
    """always gets the smaller for each position"""
    for position in range(len(L)):
        for i in range(position, len(L)):
            if L[i] < L[position]:
                L[i], L[position] = L[position], L[i]
    return L


# merge sorts
def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    if l < len(left):
        result.extend(left[l:])
    elif r < len(right):
        result.extend(right[r:])
    return result


def merge_sort(L: list):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)



listz = [1,2,3,5,6,15,99,55,12]
listz = merge_sort(listz)
print(listz)
print(bisect_search2(listz, 55))











