def rotate_left3(nums):
    return nums[1:] + [nums[0]]
def common_end(a, b):
    return (a[0] == b[0]) or (a[-1] == b[-1])
def has23(nums):
    for i in nums:
        if i == 2 or i == 3:
            return True
    return False

print "rotate_left3([1, 2, 3]) =", rotate_left3([1, 2, 3])
print "rotate_left3([5, 11, 9]) =", rotate_left3([5, 11, 9])
print "rotate_left3([7, 0, 0]) =", rotate_left3([7, 0, 0])
print "common_end([1, 2, 3], [7, 3]) =", common_end([1, 2, 3], [7, 3])
print "common_end([1, 2, 3], [7, 3, 2]) =", common_end([1, 2, 3], [7, 3, 2])
print "common_end([1, 2, 3], [1, 3]) =", common_end([1, 2, 3], [1, 3])
print "has23([2, 5]) =", has23([2, 5])
print "has23([4, 3]) =", has23([4, 3])
print "has23([4, 5]) =", has23([4, 5])
