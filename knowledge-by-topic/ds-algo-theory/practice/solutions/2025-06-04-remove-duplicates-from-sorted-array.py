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

"""
NIXXED THIS APPROACH
expanded description:
philisophically, what is going on here?
the fast reader is doing "discover". we want the writer to WRITE ONLY WHEN the fast reader DISCOVERS a number greater than the number that has been discovered before
so suppose we take an approach of keeping track of the largest number as of yet discovered. the slow writer could write only when a new greatest number is discovered
"""

"""
key realization: the slow writer should write EVERY TIME
because it will place a number in order in EVERY SPOT FROM LEFT TO RIGHT
so how about I move it only after it writes?
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        s = 1
        for f in range(len(nums)):
            if nums[f] > nums[s - 1]:
                # set the value at slow write to the value at fast reader
                nums[s] = nums[f]
                # move slow writer pointer since it has placed a correct number and now has a new spot to potentially write in
                s += 1
        return s
        