# Write a recursive method, range, that takes a start and an end
# and returns an list of all numbers between. If end < start,
# you can return the empty list.

def range(start, end):
    if end < start:
        return []

    result = range(start, end - 1)
    result.insert(len(result), end)
    return result

# print range(1,100)

# Write both a recursive and iterative version of sum of an list.

def sum_iter(list):
    sum = 0

    for num in list:
        sum += num

    return sum

# print sum_iter([1,2,3,4,5])

def sum_rec(list):
    if len(list) == 0:
        return 0

    num = list.pop()
    result = sum_rec(list) + num
    return result

# print sum_rec([1,2,3,4,5])

# Write a recursive and an iterative Fibonacci method. The method should
# take in an integer n and return the first n Fibonacci numbers in an list.

# You shouldn't have to pass any lists between methods; you should be
# able to do this just passing a single argument for the number of Fibonacci
# numbers requested.

def fib_iter(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        result = [1, 1]

    while len(result) < n:
        result.append(result[-2] + result[-1])

    return result

# print fib_iter(1)
# print fib_iter(2)
# print fib_iter(3)
# print fib_iter(4)
# print fib_iter(5)

def fib_rec(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    result = fib_rec(n - 1)
    result.insert(len(result), (result[-2] + result[-1]))
    return result

# print fib_rec(1)
# print fib_rec(2)
# print fib_rec(3)
# print fib_rec(4)
# print fib_rec(5)

# Write a recursive binary search: bsearch(array, target). Note that binary
# search only works on sorted arrays. Make sure to return the location of the
# found object (or nil if not found!). Hint: you will probably want to use
# subarrays.

def bsearch(list, target):
    if len(list) == 0:
        return None

    mid = len(list) / 2

    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return bsearch(list[0:mid], target)
    elif list[mid] < target:
        result = bsearch(list[(mid + 1):(len(list))], target)
        if result == None:
            result = None
        else:
            result += (mid + 1)
        return result

# print bsearch([1, 2, 3], 1) # => 0
# print bsearch([2, 3, 4, 5], 3) # => 1
# print bsearch([2, 4, 6, 8, 10], 6) # => 2
# print bsearch([1, 3, 4, 5, 9], 5) # => 3
# print bsearch([1, 2, 3, 4, 5, 6], 6) # => 5
# print bsearch([1, 2, 3, 4, 5, 6], 0) # => nil
# print bsearch([1, 2, 3, 4, 5, 7], 6) # => nil
