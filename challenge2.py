# 1) Store the given values:

# `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.

# 2) Calculate the total sum using the wrong mean:

# - Multiply `mean1` by `total_number`

# - Store it in `sum`

# - Print the sum.

# 3) Fix the sum to get the correct total:

# - Remove the wrong number (subtract `wrong_number`)

# - Add the correct number (add `correct_number`)

# - Store the corrected total in `num2`

# - Print the corrected sum.

# 4) Find the correct mean:

# - Divide `num2` by `total_number`

# - Store it in `mean2`

# - Print `mean2`.
"""The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.
"""
wrong_number=36
correct_number=56
total_number=40
mean1=38
sum=mean1*total_number
print("The mean is ", sum)
sum2=sum+(correct_number-wrong_number)
print("The sum is ",sum2)
mean2=sum2/total_number
print("The correct mean is ",mean2)