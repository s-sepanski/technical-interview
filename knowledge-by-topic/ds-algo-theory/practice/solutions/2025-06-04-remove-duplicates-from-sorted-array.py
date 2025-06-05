"""
suppose we have 

let s be slow writer, f be fast reader

[1, 1, 2]
    s
    f

[1, 1, 2]
    s. f
set value at s as value at f
because val @f is different than val@s

return s


----------

[1, 2, 2]
    s. f

return s

[1, 2, 2, 4]
    s. f

[1, 2, 2, 4]
       s. f

for each iteration:
if vals at f and s are not equal, set val at s as val at f
I suppose s should move only when it is NOT equal to the number to its left (because it should always be at the next write position)
f should move each time

    
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        s = 1
        for f, num in enumerate(nums):
            if nums[f] != nums[s]:
                nums[s] = nums[f]
                if nums[s] != nums[s - 1]:
                    s += 1
        return s
        