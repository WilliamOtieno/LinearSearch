def search(x, my_list):
    for k in range(len(my_list)):
        if my_list[k] == x:
            return k
    return -1

nums = [7,4,88,35,7,33,89]
print(search(88, nums))
