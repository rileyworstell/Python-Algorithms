# return the largest sum of increasing subsequences and the values that added up to that.

# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    highest = [0 for _ in range(len(array))]
    locations = [[] for _ in range(len(array))]
    highest[0] = array[0]
    locations[0] = [array[0]]
    for i in range(1, len(array)):
        pointer = i - 1
        while array[pointer] >= array[i] and pointer >= 0:
            pointer -= 1
        pointer = selectIndex(array[:i], highest[:i], array[i])
        if array[pointer] < array[i]:
            if array[i] > array[i] + highest[pointer]:
                highest[i] = array[i]
                locations[i] = [array[i]]
            else:
                highest[i] = highest[pointer] + array[i]
                locations[i] = [x for x in locations[pointer]]
                locations[i].append(array[i])
        else:
            highest[i] = array[i]
            locations[i] = [array[i]]
    x = highest.index(max(highest))
    return [max(highest), locations[x]]


def selectIndex(array, highest, val):
    for i in range(len(array)):
        x = highest.index(max(highest))
        if array[x] < val:
            return x
        else:
            highest[x] = float('-inf')
    return 0
