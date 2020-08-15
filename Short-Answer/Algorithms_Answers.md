# Please add your answers to the ***Analysis of  Algorithms*** exercises here

## Exercise I

a) O(n*3) -> O(n)
There's a single loop which multiples input n 3 times, but since the 3 is less significant than the 1 loop, we throw it away and are left with O(n).
The bigger n is, the  more times the loop will run, but the increase is linear.

b) O(n^2)
While loop inside for loop. The outer for loop will iterate over all input data, and the inner while loop will execute at least once if n > 1. Larger inputs seem to run increasingly longer.

c) O(n)
This recursive function is called as many times as there are bunnies input, no more, no less. It would be much simpler and less resource intensive to just multiply the input bunnies * 2.

## Exercise II
