# Summing a list with recursion

def list_sum(num_list):
    if len(num_list) == 1: # Base Case
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1,2,3,4,5,6,7,8,9,10]))
