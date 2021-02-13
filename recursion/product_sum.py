"""
Takes in a special array and returns its product sum.
special array is an array that contains integers or other special arrays.
depth of special array is how far it is nested and that is the multiplier.
"""


def product_sum(array, n=1):
    answer = 0
    for i in range(len(array)):
        if isinstance(array[i], int):
            answer += array[i]
        else:
            answer += ((product_sum(array[i], n + 1)) * (n+1))
    return answer


# array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# array = [5, 2, [2, 1]]
array = [1, 2, [3], 4, 5]  # 18
array = [[1, 2], 3, [4, 5]]
print(product_sum(array, 1))
