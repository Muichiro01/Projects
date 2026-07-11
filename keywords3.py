"""# 1) Initialize a variable `var` with the value 10.

# 2) Use a `while` loop that runs as long as `var` is greater than 0.

# 3) Inside the loop, decrease the value of `var` by 1.

# 4) Check if `var` is equal to 5:

# a) If `var == 5`, use `continue`.

# b) `continue` skips the remaining statements in the current iteration

# and moves to the next iteration of the loop.

# 5) If `var` is not equal to 5, print the current value of `var`.

# 6) After the loop finishes, print "Good bye!"."""
var=20
while var>0:
    var=var-1
    if var==5:
        continue
    else:
        print(var)
print("Good bye!")