def rec(total, arr, i, mem):
    key = str(total) + ":" + str(i)
    if(mem.get(key) is not None):
        return mem.get(key)
    if total == 0:
        return 1
    if total < 0:
        return 0
    if i < 0:
        return 0
    if arr[i] > total:
        return rec(total, arr, i -1, mem)
    to_return = rec(total - arr[i], arr, i-1, mem) + rec(total, arr, i-1, mem)
    mem[key] = to_return
    return to_return


def count_subset_of_total(total, arr: []):
    mem = {}    
    return rec(total, arr, len(arr)-1, mem)

print(count_subset_of_total(10, [8,2,4,6,10]))