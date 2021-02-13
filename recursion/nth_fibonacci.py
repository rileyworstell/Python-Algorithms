"""
write a function that returns the the nth fibonacci number
"""


# O(n) Time & O(1) Space - where n is the input number
def get_nth_fib(n):
    if n == 1 or n == 2:
        return n - 1
    else:
        return (get_nth_fib(n-1) + get_nth_fib(n-2))


print(get_nth_fib(6))  # 0, 1, 1, 2, 3, 5
