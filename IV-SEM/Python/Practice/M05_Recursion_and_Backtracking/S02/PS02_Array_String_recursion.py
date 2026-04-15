def Array_sum(nums):
    s=0
    for i in range(len(nums)-1,-1,-1):
        s += nums[i]
    return s
print