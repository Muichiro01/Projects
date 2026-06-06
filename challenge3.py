# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.

# 2) Calculate the average of `a`, `b`, and `c`:

# - Add them and divide by 3

# - Store the result in `avg`

# - Print `avg`

# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:

# - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.

# - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.

# - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.

# - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.

# - Else if `avg` is greater than only `a`, print that it is just higher than `a`.

# - Else if `avg` is greater than only `b`, print that it is just higher than `b`.

# - Else if `avg` is greater than only `c`, print that it is just higher than `c`.

# 4) If none of the above conditions match, print "invalid input".
"""Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?
"""
a=int(input("Enter the 1st cyclist's speed"))
b=int(input("Enter the 2nd cyclist's speed"))
c=int(input("Enter the 3rd cyclist's speed"))
avg=(a+b+c)/3
print("Average=",avg)
if avg>a and avg>b and avg>c:
    print("Average is greater than all the speeds")
elif avg>a and avg>b:
    print("Average is greater than 1st and 2nd speed")
elif avg>a and avg>c:
    print("Average is greater than 1st and 3rd speed")
elif avg>b and avg>c:
    print("Average is greater than 2nd and 3rd speed")
elif avg>a:
    print("Average is greater than the 1st speed")
elif avg>b:
    print("Average is greater than the 2nd speed")
elif avg>c:
    print("Average is greater than the 3rd speed")
else:
    print("Invalid input")



    