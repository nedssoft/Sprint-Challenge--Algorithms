#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The running time is infinity for all value of n>=0. This is because for every value of n=>0 the while  loop condition returns true and as long as the condition is true, the loop will continue to execute

b)

```
b)  sum = 0
    for i in range(n): # O(n)* O(log(n))
      j = 1
      while j < n: # O(log(n))
        j *= 2
        sum += 1
```

The running time is O(n*log(n))

c)

The running time is O(n) since it increases linearly with increase in bunnies

## Exercise II

```
# Define the inputs (n storeys and a list of eggs)
# Convert the n storeys to a list
# Get the least and highest floor 
# While the least floor is less than or equal to the highest floor
    # Get the middle of the building
    # If the egg breaks at the middle
    # Set the highest floor as the middle floor minus 1 and repeat the process until the egg does not break
    # Else if the egg does not break at the middle return the middle as f
 
The algorithm uses a binary search strategy, therefore the complexity is O(log(n))
```





