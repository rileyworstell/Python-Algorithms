# return array with all the zeros at the end and the other numbers in the original order

# O(2n) ~ O(n) time O(1) space
# The two loops are not nested so it is not O(n^2) just O(2n)
def zeros(arr):
    lPointer = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[lPointer] = arr[i]
            lPointer += 1
    for i in range(lPointer, len(arr)):
        arr[i] = 0
    return arr


print(zeros([0, 1, 0, 3, 4, 0, 12]))
