
# valid mountain array
# return true if it is an increasing subarray folled by a decreasing subarray

def is_mountain(arr):
    if arr[1] < arr[0]:
        return False
    going_up = 1
    pointer = 0
    while pointer < len(arr) - 2:
        if (arr[pointer] < arr[pointer + 1] and going_up == 1) or (arr[pointer] > arr[pointer + 1] and going_up == 0):
            pointer += 1
        else:
            if going_up == 0:
                return False
            going_up = 0
            pointer += 1
    return True


print(is_mountain([1, 2, 3, 4, 5, 6, 7, 8, 7, 5, 4, 2]))
