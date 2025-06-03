# Arrays

Each item in an array is stored contiguously in memory. Static arrays stay the same size, whereas dynamic arrays can grow or shrink

## Terms
Array size - sometimes used to refer to capacity of the array
Array length - sometimes used to refer to count of actual values stored in the array 

## Random Notes
pushing and popping values from end are O(1) time ops

## Dynamic Arrays
When inserting a value that would make length greater than size, we can:
- allocate a new empty array of twice the previous size
- copy values from the original array into the new array
- deallocate memory associated with original array (to tidy)

Allocating space for a new array takes O(n) because you have to do a `2*n` operation to allocate a new array with size `2*n` AND then do an operation on all n items in the original array

Whereas inserting a new item at the end typically takes O(1) time, when the array must be resized, it takes O(n) time

Amortized time complexity of inserting a new item at the end will be O(1)

### Time Complexity for Dynamic Arrays

| Operation             | Time Complexity |
|-----------------------|----------------|
| Access (by index)     | O(1)           |
| Insert at end         | O(1) amortized |
| Insert at end (resize)| O(n)           |
| Insert at beginning   | O(n)           |
| Insert at middle      | O(n)           |
| Delete at middle      | O(n)           |
| Delete at end         | O(1)           |
| Delete at beginning   | O(n)           |
| Search (unsorted)     | O(n)           |
| Search (sorted)       | O(log n)       |