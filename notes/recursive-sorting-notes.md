### Finding a pivot

The pivot is off on it's own, then you find the values to the left, and to the right of the pivot.

The pivot would be the first sorted value.

You then recursively sort the left and right arrays. Pick the first element in each and evaluate those against the other values. The pivot will move to the end, and the other values will shift down. You stop if you have one index in the arrays because there are no other shifts. You can then concat the singular arrays and create the sorted array.

Runtime is O(n log n). This has been the best possible runtime for general purpose sorting algorithms. There hasn't been an algorithm that can sort faster than that.

### When writing a recusive algorithm

* What is the break/base case?
* If we aren't in the base case, how are we moving towards the break/base case?