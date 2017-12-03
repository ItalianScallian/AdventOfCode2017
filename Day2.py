#found partially on reddit solutions after attempting to do the same thing in Java and failing miserably

import re
inp = [i.strip() for i in open('input.txt', 'r').readlines()]

s1 = 0
s2 = 0

for line in inp:
    nums = [int(u) for u in re.split('\s+', line)]

    s1 += max(nums) - min(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j: continue
            if nums[i] % nums[j] == 0:
                s2 += nums[i] / nums[j]


print "Part 1:", s1
print "Part 2:", s2
