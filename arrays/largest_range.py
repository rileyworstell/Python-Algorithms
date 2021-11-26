
# O(n) time | O(n) space
def largestRange(array):
    my_set = set()
    largestRange = [-1, -1]
    for i in array:
        my_set.add(i)
    already_viewed = set()
    i = 0
    while i < len(array):
        if i in already_viewed:
            i += 1
        else:
            curRange = 1
            already_viewed.add(i)
            # go left
            L = array[i] - 1
            while L in my_set:
                curRange += 1
                already_viewed.add(L)
                L -= 1
            # go right
            R = array[i] + 1
            while R in my_set:
                curRange += 1
                already_viewed.add(R)
                R += 1
            if curRange > largestRange[1] - largestRange[0]:
                largestRange = [L+1, R-1]
    return largestRange



array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array)) # [0, 7]
