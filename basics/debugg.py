from icecream import ic


def function(nums):
    for i in range(len(nums)):
        x = abs(nums[i] - 1)
        if nums[x] < 0:
            ic(f"iter{i} {nums} and x={x}")
            return x + 1
        else:
            nums[x] = -nums[x]
            ic(f"iter{i} {nums} and x={x}")


ic(function([1,2,3,4,5,6,3,8,9]))
ic(function([1,2,3,3,5]))
ic(function([3,2,1,4,2,6]))

# ic(function([5, 20, 50, 4, 5]))
# ic(function([4, 3, 2, 7, 8, 2, 3, 1]))
# ic(function([1, 1, 1, 1, 1, 1, 1, -1]))
# ic(function([0, 0, 0, 0]))
# ic(function([2, 3, 1, 0, -2, 5, 3]))
ic(function([-3,-2,-3,-1,-2]))
# ic(function([[1,2,4],[2,5,7],[1,4]]))
# ic(function([]))


# Goal of the function:
# it's trying to mark accessed elements to negative at the value related to index
# If loop access a negative number in the nums list, it means that it has seen this index value before.
# function then returns that index + 1, which was made negative in previous iteration.

# Issues with code in achieving the goal
# input supports only list of integers
# length of list and maximum element in list should be in sync
# When x > len(list)
# When list elements are not integers



