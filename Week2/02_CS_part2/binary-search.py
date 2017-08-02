import pudb

def binary_search(my_list, num):
    #Take the length / 2
    n = int(len(my_list)/2)
    # pu.db
    #go to list[n], if it != num, slice all elements to the side of the list w/o num
    if my_list[n] == num:
        return True
    elif my_list[n] < num:
        my_list = my_list[n:]
        return binary_search(my_list,num)
    elif my_list[n] > num:
        my_list = my_list[0:n]
        return binary_search(my_list,num)
    elif len(my_list) == 1:
        return False
        

  




##sample dataset
arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122]

print(binary_search(arr, 9))