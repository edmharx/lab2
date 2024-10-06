## EXERCISE 1
### Recursion

I used recursion here by passing the number and its exponent to the func `power(num, eponent)` and here is the explanation for this exercise:

* Calling the base and exponent first.
* If the exponent is 0 then it will return 1 as every integer with 0 exponent is 1.
* Multiply the num to itself while the exponent is being reduced by 1 per call.
* Recursion stops upon reaching the case where exponent is 0 as it will return 1 stopping the code.

## EXERCISE 2

### Array

This utilizes the an array variable and the functions `list` and `map`, here is the explanation:

* Ask for the number of array and the integers itself.
* Split the integers through spaces then converts them back to integers using `map` since split converts the integers to strings.
* Use list function to list all the elements the iterating them while getting their cube.

## EXERCISE 3
### Range

I used iteration to display the hollow box, here is the explanation:

* Get the desired length of the sides.
* Iterate depending on the length of the side to display the 2 vertical sides.
* Put a condition where it displays the "x" depending on the length on the top and bottom side.
* Make the box hollow by printing " " in the midle of two vertical sides.

## EXERCISE 4
### Iteration Part 2

Used iteration again to display the height of the right triangle:

* Get the height of the height of the right triangle
* Print "*" depending on iteration
* Get the decreasing number of "*" per iteration by subtracting 1 every iteration to height
* Since 0 is counted as 1 iteration, I added + 1 on `new_height` var to display a * on the last iteration
